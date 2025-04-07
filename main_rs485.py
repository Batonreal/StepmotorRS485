# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_rs485.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(470, 304)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(18)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/stepmotor.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(35, 35))
        self.exit = QAction(MainWindow)
        self.exit.setObjectName(u"exit")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/powercircleandlinesymbol_118369.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit.setIcon(icon1)
        font1 = QFont()
        self.exit.setFont(font1)
        self.refresh = QAction(MainWindow)
        self.refresh.setObjectName(u"refresh")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/reload_update_refresh_icon_143703.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh.setIcon(icon2)
        self.About = QAction(MainWindow)
        self.About.setObjectName(u"About")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/help_information_chat_bubble_info_about_communications_speech_icon_258982.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.About.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.com_port = QComboBox(self.centralwidget)
        self.com_port.setObjectName(u"com_port")

        self.verticalLayout.addWidget(self.com_port)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        self.label.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label)

        self.select_button = QPushButton(self.centralwidget)
        self.select_button.setObjectName(u"select_button")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.select_button.setFont(font3)
        self.select_button.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 80);\n"
"}")

        self.horizontalLayout_4.addWidget(self.select_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.backward_button = QPushButton(self.centralwidget)
        self.backward_button.setObjectName(u"backward_button")
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(17)
        self.backward_button.setFont(font4)
        self.backward_button.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 80);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/arrow_circle_left_icon_155799.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backward_button.setIcon(icon4)
        self.backward_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.backward_button)

        self.forward_button = QPushButton(self.centralwidget)
        self.forward_button.setObjectName(u"forward_button")
        self.forward_button.setFont(font4)
        self.forward_button.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 80);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/arrow_circle_right_icon_155798.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.forward_button.setIcon(icon5)
        self.forward_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.forward_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinbox = QSpinBox(self.centralwidget)
        self.spinbox.setObjectName(u"spinbox")
        self.spinbox.setEnabled(True)
        self.spinbox.setStyleSheet(u"QSpinBox {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                 stop:0 #ffffff, stop:1 #f0f0f0);\n"
"    border: 1px solid #b0b0b0;\n"
"    padding: 10px;\n"
"    font-size: 22px;\n"
"    color: #333;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox:focus {\n"
"    border: 1px solid #4da6ff;\n"
"    outline: none;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"    border-left: 1px solid #b0b0b0;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 25px;\n"
"    height: 25px;\n"
"    border-left: 1px solid #b0b0b0;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    image: url(:/icons/icons/arrow_circle_up_arrow_icon_253879.svg);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    image: url(:/icons/icons/c"
                        "ircle_down_arrow_arrow_icon_253893.svg);\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: #d0d0d0;\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: #d0d0d0;\n"
"}")
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(10)

        self.horizontalLayout.addWidget(self.spinbox)

        self.set_button = QPushButton(self.centralwidget)
        self.set_button.setObjectName(u"set_button")
        self.set_button.setFont(font4)
        self.set_button.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 80);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/row_height_icon_154882.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.set_button.setIcon(icon6)
        self.set_button.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.set_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.brake_button = QPushButton(self.centralwidget)
        self.brake_button.setObjectName(u"brake_button")
        self.brake_button.setFont(font4)
        self.brake_button.setStyleSheet(u"QPushButton {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 40);\n"
"border: 2px solid rgba(0, 0, 0, 50);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 80);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/Private-80_icon-icons.com_57286.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.brake_button.setIcon(icon7)
        self.brake_button.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.brake_button)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 470, 28))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(12)
        self.menubar.setFont(font5)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(10)
        self.menu.setFont(font6)
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.refresh)
        self.menu.addSeparator()
        self.menu.addAction(self.exit)
        self.menu_2.addAction(self.About)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AlternativaRS485", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.refresh.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a COM-\u043f\u043e\u0440\u0442\u043e\u0432", None))
#if QT_CONFIG(tooltip)
        self.refresh.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.About.setText(QCoreApplication.translate("MainWindow", u"About", None))
#if QT_CONFIG(tooltip)
        self.select_button.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0432\u044b\u0431\u043e\u0440 COM-\u043f\u043e\u0440\u0442\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.select_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.backward_button.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0430\u0449\u0430\u0442\u044c \u0448\u0430\u0433\u043e\u0432\u044b\u0439 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u0432 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u043c \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.backward_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
#if QT_CONFIG(tooltip)
        self.forward_button.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0430\u0449\u0430\u0442\u044c \u0448\u0430\u0433\u043e\u0432\u044b\u0439 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c \u0432 \u043f\u0440\u044f\u043c\u043e\u043c \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.forward_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0435\u0434", None))
#if QT_CONFIG(tooltip)
        self.spinbox.setToolTip(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0448\u0430\u0433\u043e\u0432", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.set_button.setToolTip(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0448\u0430\u0433\u043e\u0432 \u0448\u0430\u0433\u043e\u0432\u043e\u0433\u043e \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f", None))
#endif // QT_CONFIG(tooltip)
        self.set_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.brake_button.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0442\u043e\u0440\u043c\u043e\u0437, \u0443\u0431\u0440\u0430\u0442\u044c \u0438\u0437 \u0440\u0435\u0436\u0438\u043c\u0430 \u0443\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u044f", None))
#endif // QT_CONFIG(tooltip)
        self.brake_button.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0440\u043c\u043e\u0437", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438", None))
    # retranslateUi

