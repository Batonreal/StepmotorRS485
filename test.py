import serial
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst

try:
    serial_port = serial.Serial(port="COM4", baudrate=19200, bytesize=8, parity="E", stopbits=1, xonxoff=0)
    master = modbus_rtu.RtuMaster(serial_port)
    master.set_timeout(5.0)

    # Запись значения 123 в регистр 0x4000 (16384 в десятичной системе) для slave ID 10
    master.execute(10, cst.WRITE_SINGLE_REGISTER, 0x4000, output_value=123)
    print("Запись прошла успешно")

except Exception as e:
    print(f"Ошибка: {e}")
finally:
    if hasattr(master, 'close'):
        master.close()
    if serial_port.is_open:
        serial_port.close()