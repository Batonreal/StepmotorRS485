import sys
import traceback
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
import serial.tools.list_ports
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from main_rs485 import Ui_MainWindow


class RS485StepperControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.slave_id = 10
        self.baudrate = 19200
        self.data_bits = 8
        self.stop_bits = 1
        self.parity = serial.PARITY_EVEN
        self.master = None
        self.serial_connection = None

        self.populate_com_ports()
        self.init_ui_connections()

    def populate_com_ports(self):
        """Заполняет QComboBox доступными COM-портами."""
        ports = serial.tools.list_ports.comports()
        self.ui.com_port.clear()
        for port in ports:
            print(f"Найден порт: {port.device}")
            self.ui.com_port.addItem(port.device)

    def init_serial(self):
        """Инициализация подключения к выбранному COM-порту."""
        selected_port = self.ui.com_port.currentText()
        print(f"Выбранный порт: {selected_port}")
        if not selected_port:
            QMessageBox.warning(self, "Предупреждение", "Выберите COM-порт.")
            return

        if self.serial_connection and self.serial_connection.is_open:
            print(f"Закрытие порта: {self.serial_connection.port}")
            self.serial_connection.close()

        try:
            self.serial_connection = serial.Serial(
                port=selected_port,
                baudrate=self.baudrate,
                bytesize=self.data_bits,
                parity=self.parity,
                stopbits=self.stop_bits,
                xonxoff=0
            )
            if not self.serial_connection.is_open:
                self.serial_connection.open()

            if self.master is None:
                self.master = modbus_rtu.RtuMaster(self.serial_connection)
                self.master.set_timeout(5.0)
                self.master.set_verbose(True)

            print(f"Modbus успешно инициализирован на порту {selected_port}")
        except serial.SerialException as e:
            print(f"Ошибка подключения к serial port: {e}")
            print(traceback.format_exc())
            QMessageBox.critical(self, "Ошибка", f"Не удалось открыть COM-порт: {e}")
            self.master = None
            self.serial_connection = None

    def init_ui_connections(self):
        self.ui.forward_button.clicked.connect(self.forward)
        self.ui.backward_button.clicked.connect(self.backward)
        self.ui.brake_button.clicked.connect(self.brake)
        self.ui.set_button.clicked.connect(self.set_value)
        self.ui.com_port.currentIndexChanged.connect(self.on_com_port_changed)
        self.ui.select_button.clicked.connect(self.select_com_port)
        self.ui.refresh.triggered.connect(self.populate_com_ports)
        self.ui.exit.triggered.connect(self.close)

    def select_com_port(self):
        """Обработчик кнопки выбора COM-порта."""
        selected_port = self.ui.com_port.currentText()
        if not selected_port:
            print("Нет доступного COM-порта.")
            self.ui.label.setText("Нет COM-порта")
            return

        print(f"Выбранный порт подтверждён пользователем: {selected_port}")
        try:
            self.init_serial()
            self.ui.label.setText("Подключено к " + selected_port)
        except Exception as e:
            print(f"Ошибка при выборе порта: {e}")
            self.ui.label.setText("Error")

    def on_com_port_changed(self):
        print("COM-порт изменён")
        self.init_serial()

    def send_coil_command(self, register_address):
        if self.master is None:
            QMessageBox.warning(self, "Предупреждение", "Master Modbus не инициализирован.")
            self.ui.label.setText("Не инициализировано")
            return

        try:
            self.master.execute(self.slave_id, cst.WRITE_SINGLE_COIL, register_address, output_value=1)
            self.ui.label.setText("Отправлено в " + str(hex(register_address)))
            QTimer.singleShot(2000, lambda: self.reset_coil(register_address))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка записи coil {hex(register_address)}: {e}")
            self.ui.label.setText("Error")


    def reset_coil(self, register_address):
        if self.master is None:
            QMessageBox.warning(self, "Предупреждение", "Master Modbus не инициализирован.")
            self.ui.label.setText("Не инициализировано")
            return

        try:
            self.master.execute(self.slave_id, cst.WRITE_SINGLE_COIL, register_address, output_value=0)
            self.ui.label.setText("Запись в " + str(hex(register_address)))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка сброса coil {hex(register_address)}: {e}")
            self.ui.label.setText("Error")

    def forward(self):
        self.send_coil_command(0x2008)

    def backward(self):
        self.send_coil_command(0x2009)

    def brake(self):
        self.send_coil_command(0x200A)

    def set_value(self):
        if self.master is None:
            QMessageBox.warning(self, "Предупреждение", "Master Modbus не инициализирован.")
            return

        value = self.ui.spinbox.value()
        try:
            self.master.execute(self.slave_id, cst.WRITE_SINGLE_REGISTER, 0x4000, output_value=value)
            self.ui.label.setText("Запись в " + str(hex(0x4000)))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка записи в регистр 0x4000: {e}")

    def closeEvent(self, event):
        if self.master:
            try:
                self.master.close()
            except Exception:
                pass
        if self.serial_connection and self.serial_connection.is_open:
            try:
                self.serial_connection.close()
            except Exception:
                pass
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RS485StepperControl()
    window.show()
    sys.exit(app.exec())