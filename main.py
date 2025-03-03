import sys
import time
import traceback
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QSpinBox, QLabel, QMessageBox)
from PySide6.QtCore import Qt, QTimer
import serial
import struct
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

class RS485StepperControl(QWidget):
    def __init__(self):
        super().__init__()

        self.slave_id = 10
        self.serial_port = "COM4"  # Замените на ваш COM-порт!
        self.baudrate = 19200
        self.data_bits = 8
        self.stop_bits = 1
        self.parity = serial.PARITY_EVEN
        self.master = None
        self.serial_connection = None # Добавляем атрибут для serial.Serial

        self.init_serial()
        self.init_ui()

    def init_serial(self):
        try:
            # Создаем serial connection
            self.serial_connection = serial.Serial(
                port=self.serial_port,
                baudrate=self.baudrate,
                bytesize=self.data_bits,
                parity=self.parity,
                stopbits=self.stop_bits,
                xonxoff=0
            )
            if not self.serial_connection.is_open:
                self.serial_connection.open()

            # Создаем Modbus master только если он еще не создан
            if self.master is None:
                self.master = modbus_rtu.RtuMaster(self.serial_connection)
                self.master.set_timeout(5.0)
                self.master.set_verbose(True)

            # Небольшая задержка после открытия порта
            time.sleep(0.1)
            print(f"Успешно подключено к {self.serial_port}")
        except serial.SerialException as e:
            print(f"Ошибка подключения к serial port: {e}")
            print(traceback.format_exc())  # Выводим полную трассировку
            self.master = None
            self.serial_connection = None # Сбрасываем connection тоже
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть COM-порт: {e}") # Показываем ошибку пользователю

    def init_ui(self):
        self.setWindowTitle("RS485 Stepper Motor Control")

        # Кнопки
        self.forward_button = QPushButton("Вперед")
        self.backward_button = QPushButton("Назад")
        self.brake_button = QPushButton("Тормоз")
        self.set_button = QPushButton("Установить")

        # SpinBox
        self.spinbox = QSpinBox()
        self.spinbox.setRange(1, 16)

        # Связываем кнопки с функциями
        self.forward_button.clicked.connect(self.forward)
        self.backward_button.clicked.connect(self.backward)
        self.brake_button.clicked.connect(self.brake)
        self.set_button.clicked.connect(self.set_value)

        # Layout
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Значение:"))
        hbox.addWidget(self.spinbox)

        vbox = QVBoxLayout()
        vbox.addWidget(self.forward_button)
        vbox.addWidget(self.backward_button)
        vbox.addWidget(self.brake_button)
        vbox.addLayout(hbox)
        vbox.addWidget(self.set_button)

        self.setLayout(vbox)

    def send_coil_command(self, register_address):
        """Отправляет команду установки и сброса coil."""
        if self.master is None:
            print("Ошибка: Master Modbus не инициализирован.")
            QMessageBox.warning(self, "Предупреждение", "Master Modbus не инициализирован.")
            return

        try:
            print(f"Запись coil {register_address} в 1...")
            self.master.execute(self.slave_id, cst.WRITE_SINGLE_COIL, register_address, output_value=1) # Исправлено
            print(f"Coil {register_address} успешно установлен в 1.")
            QTimer.singleShot(1000, lambda: self.reset_coil(register_address))  # Через 1 секунду сброс
        except Exception as e:
            print(f"Ошибка записи coil {register_address}: {e}")
            print(traceback.format_exc())
            QMessageBox.critical(self, "Ошибка", f"Ошибка записи coil {register_address}: {e}")

    def reset_coil(self, register_address):
        """Сбрасывает coil в 0."""
        if self.master is None:
            print("Ошибка: Master Modbus не инициализирован.")
            QMessageBox.warning(self, "Предупреждение", "Master Modbus не инициализирован.")
            return

        try:
            print(f"Сброс coil {register_address} в 0...")
            self.master.execute(self.slave_id, cst.WRITE_SINGLE_COIL, register_address, output_value=0)  # Исправлено
            print(f"Coil {register_address} успешно сброшен в 0.")
        except Exception as e:
            print(f"Ошибка сброса coil {register_address}: {e}")
            print(traceback.format_exc())
            QMessageBox.critical(self, "Ошибка", f"Ошибка сброса coil {register_address}: {e}")

    def forward(self):
        self.send_coil_command(0x2008)

    def backward(self):
        self.send_coil_command(0x2009)

    def brake(self):
        self.send_coil_command(0x200A)

    def set_value(self):
        """Устанавливает значение регистра."""
        if self.master is None:
            print("Ошибка: Master Modbus не инициализирован.")
            QMessageBox.warning(self, "Предупреждение", "Master Modbus не инициализирован.")
            return

        value = self.spinbox.value()

        try:
            print(f"Запись значения {value} в регистр 0x4000...")
            self.master.execute(self.slave_id, cst.WRITE_SINGLE_REGISTER, 0x4000, output_value=value)  # Исправлено
            print(f"Значение {value} успешно записано в регистр 0x4000")
        except Exception as e:
            print(f"Ошибка записи в регистр 0x4000: {e}")
            print(traceback.format_exc())
            QMessageBox.critical(self, "Ошибка", f"Ошибка записи в регистр 0x4000: {e}")

    def closeEvent(self, event):
        """Закрытие порта при закрытии окна."""
        if self.master:
            try:
                self.master.close()
                print("Modbus master закрыт.")
            except Exception as e:
                print(f"Ошибка закрытия Modbus master: {e}")
                print(traceback.format_exc())
        if self.serial_connection and self.serial_connection.is_open:
            try:
                self.serial_connection.close()
                print("Serial port закрыт.")
            except Exception as e:
                print(f"Ошибка закрытия serial port: {e}")
                print(traceback.format_exc())

        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RS485StepperControl()
    window.show()
    sys.exit(app.exec())