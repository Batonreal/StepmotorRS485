"Описание: Разработано для управления шаговым двигателем по протоколу RS-485 Modbus RTU."

Создание виртуального окружения: venv (Windows)

python -m venv venv

venv\Scripts\activate

pip install pyinstaller PySide6 pyserial modbus-tk

---------------------------------------------------------------------------------------------------

Сборка .exe через pyinstaller:

pyinstaller --onefile --noconsole --name AlternativaRS485 --icon=icons/stepmotor.jpg --add-data "icon_rc.py;." main.py
