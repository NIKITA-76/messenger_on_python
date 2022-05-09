from PyQt5 import QtCore, QtWidgets, QtGui

from ui_add_friend import Ui_AddFriend
from ui_users_login import Ui_LandP_Reg


class UI_ForMain(object):
    def setupUi(self, MainWindow, ChildWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1291, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1291, 866))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 74, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 74, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(167, 167, 167))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(74, 74, 74))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(50, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(111, 111, 111))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                         "")
        self.stackedWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setMidLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_sign = QtWidgets.QWidget()
        self.page_sign.setObjectName("page_sign")
        self.label_2 = QtWidgets.QLabel(self.page_sign)
        self.label_2.setGeometry(QtCore.QRect(450, 424, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_toReg = QtWidgets.QPushButton(self.page_sign)
        self.pushButton_toReg.setGeometry(QtCore.QRect(660, 490, 141, 31))
        self.pushButton_toReg.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_toReg.setObjectName("pushButton_toReg")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_sign)
        self.lineEdit_2.setGeometry(QtCore.QRect(522, 420, 281, 31))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.page_sign)
        self.label.setGeometry(QtCore.QRect(460, 332, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(158, 158, 158);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.page_sign)
        self.lineEdit.setGeometry(QtCore.QRect(522, 330, 281, 31))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_sign = QtWidgets.QPushButton(self.page_sign)
        self.pushButton_sign.setGeometry(QtCore.QRect(514, 490, 81, 31))
        self.pushButton_sign.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_sign.setObjectName("pushButton_sign")
        self.line_4 = QtWidgets.QFrame(self.page_sign)
        self.line_4.setGeometry(QtCore.QRect(-3, 50, 1291, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_10 = QtWidgets.QLabel(self.page_sign)
        self.label_10.setGeometry(QtCore.QRect(580, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.page_sign)
        self.page_reg = QtWidgets.QWidget()
        self.page_reg.setObjectName("page_reg")
        self.label_8 = QtWidgets.QLabel(self.page_reg)
        self.label_8.setGeometry(QtCore.QRect(428, 500, 451, 20))
        self.label_8.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.page_reg)
        self.label_7.setGeometry(QtCore.QRect(450, 400, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.page_reg)
        self.label_5.setGeometry(QtCore.QRect(450, 300, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_log")
        self.pushButton_reg = QtWidgets.QPushButton(self.page_reg)
        self.pushButton_reg.setGeometry(QtCore.QRect(512, 530, 81, 31))
        self.pushButton_reg.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_reg.setObjectName("pushButton_reg")
        self.pushButton_backToSign = QtWidgets.QPushButton(self.page_reg)
        self.pushButton_backToSign.setGeometry(QtCore.QRect(710, 530, 81, 31))
        self.pushButton_backToSign.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_backToSign.setObjectName("pushButton_backToSign")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_reg)
        self.lineEdit_5.setGeometry(QtCore.QRect(560, 460, 281, 31))
        self.lineEdit_5.setObjectName("lineEdit_pass")
        self.label_6 = QtWidgets.QLabel(self.page_reg)
        self.label_6.setGeometry(QtCore.QRect(400, 460, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_pass")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_reg)
        self.lineEdit_7.setGeometry(QtCore.QRect(560, 300, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_reg)
        self.lineEdit_6.setGeometry(QtCore.QRect(560, 400, 281, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.page_reg)
        self.label_9.setGeometry(QtCore.QRect(580, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.line_3 = QtWidgets.QFrame(self.page_reg)
        self.line_3.setGeometry(QtCore.QRect(-3, 50, 1291, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.stackedWidget.addWidget(self.page_reg)
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.listWidget_msgRoom = QtWidgets.QListWidget(self.page_main)
        self.listWidget_msgRoom.setGeometry(QtCore.QRect(450, 48, 840, 651))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_msgRoom.setFont(font)
        self.listWidget_msgRoom.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                              "color: rgb(158, 158, 158);\n"
                                              "border:0px;")
        self.listWidget_msgRoom.setObjectName("listWidget_msgRoom")
        self.listWidget_title = QtWidgets.QLabel(self.page_main)
        self.listWidget_title.setGeometry(QtCore.QRect(450, 0, 837, 51))
        self.listWidget_title.setMaximumSize(QtCore.QSize(16777215, 16777214))

        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget_title.setFont(font)
        self.listWidget_title.setStyleSheet("color: rgb(158, 158, 158);\n"
                                            "background-color: rgb(30, 30, 30);")
        self.listWidget_title.setAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_title.setObjectName("listWidget_title")
        self.listWidget_people = QtWidgets.QListWidget(self.page_main)
        self.listWidget_people.setGeometry(QtCore.QRect(0, 65, 450, 821))
        self.listWidget_people.setAutoFillBackground(False)
        self.listWidget_people.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                             "font: 25 18pt \"Corbel Light\";\n"
                                             "color: rgb(158, 158, 158);\n"
                                             "border:0px;\n"
                                             "")
        self.listWidget_people.setObjectName("listWidget_people")
        self.pushButton_menu = QtWidgets.QPushButton(self.page_main)
        self.pushButton_menu.setGeometry(QtCore.QRect(38, 20, 400, 31))
        self.pushButton_menu.setStyleSheet("\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "background-color: rgb(100, 100, 100);\n"
                                           "\n"
                                           "color: rgb(50, 50, 50);\n"
                                           "border:0px;\n"
                                           "border-radius: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgb(130, 130, 130);\n"
                                           "color: rgb(50, 50, 50);\n"
                                           "border-radius: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "")
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.textEdit_room = QtWidgets.QTextEdit(self.page_main)
        self.textEdit_room.setGeometry(QtCore.QRect(500, 730, 671, 95))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_settings = QtWidgets.QPushButton(self.page_main)
        self.pushButton_settings.setGeometry(QtCore.QRect(3, 19, 31, 36))
        self.pushButton_settings.setStyleSheet("background-color: rgb(41, 41, 41);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/free-icon-menu-1828859.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_settings.setIcon(icon)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.textEdit_room.setFont(font)
        self.textEdit_room.setMouseTracking(False)
        self.textEdit_room.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                         "font: 14pt \"Cantarell\";\n"
                                         "color: rgb(158, 158, 158);\n"
                                         "border:0px;\n"
                                         "border-radius: 12px;\n"
                                         "")
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.pushButton_quit = QtWidgets.QPushButton(self.page_setting)
        self.pushButton_quit.setGeometry(QtCore.QRect(480, 470, 301, 36))
        self.pushButton_quit.setStyleSheet("background-color: rgb(41, 41, 41);")
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.pushButton_back_tomain = QtWidgets.QPushButton(self.page_setting)
        self.pushButton_back_tomain.setGeometry(QtCore.QRect(6, 19, 35, 36))
        self.pushButton_back_tomain.setStyleSheet("background-color: rgb(41, 41, 41);")
        self.pushButton_back_tomain.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/free-icon-back-130882.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back_tomain.setIcon(icon1)
        self.pushButton_back_tomain.setObjectName("pushButton_back_tomain")
        self.textEdit_room.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_room.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit_room.setOverwriteMode(False)
        self.textEdit_room.setPlaceholderText("")
        self.textEdit_room.setObjectName("textEdit_room")
        self.line = QtWidgets.QFrame(self.page_main)
        self.line.setGeometry(QtCore.QRect(450, 530, 841, 331))
        self.line.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_room = QtWidgets.QPushButton(self.page_main)
        self.pushButton_room.setGeometry(QtCore.QRect(1190, 730, 91, 91))
        self.label_of_creator = QtWidgets.QLabel(self.page_setting)
        self.label_of_creator.setGeometry(QtCore.QRect(483, 520, 451, 20))
        self.label_of_creator.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_of_creator.setObjectName("label_of_creator")
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_room.setFont(font)
        self.pushButton_room.setStyleSheet("QPushButton{\n"
                                           "font: 11pt ;\n"
                                           "background-color: rgb(50, 50, 50);\n"
                                           "\n"
                                           "color: rgb(158, 158, 158);\n"
                                           "border:0px;\n"
                                           "border-radius: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "font: 11pt ;\n"
                                           "background-color: rgb(70, 70, 70);\n"
                                           "color: rgb(158, 158, 158);\n"
                                           "border-radius: 6px;\n"
                                           "}\n"
                                           "")
        self.pushButton_room.setObjectName("pushButton_room")
        self.pushButton_room.hide()

        self.line.raise_()
        self.listWidget_msgRoom.raise_()
        self.listWidget_people.raise_()
        self.listWidget_title.raise_()
        self.pushButton_menu.raise_()
        self.textEdit_room.raise_()
        self.pushButton_room.raise_()
        self.stackedWidget.addWidget(self.page_main)
        self.stackedWidget.addWidget(self.page_setting)

        MainWindow.setCentralWidget(self.centralwidget)
        self.LP_RForm = Ui_LandP_Reg()
        self.LP_RForm.setupUi(ChildWindow)

        self.AddFRNDWindow = QtWidgets.QMainWindow()
        self.AddFRNDForm = Ui_AddFriend()
        self.AddFRNDForm.setupUi(self.AddFRNDWindow)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # НИЖЕ КНОПКИ ОКНА ВХОДА
        self.LP_RForm.pushButton.clicked.connect(self.Sign_in)
        # self.RegForm.pushButton_settings.clicked.connect(self.Reg_in)

        # НИЖЕ КНОПКИ ДОБАВЛЕНИЯ В ДРУЗЬЯ
        self.pushButton_menu.clicked.connect(lambda: self.AddFRNDWindow.show())
        self.AddFRNDForm.pushButton_2.clicked.connect(self.searchPeople)
        self.AddFRNDForm.pushButton.clicked.connect(self.addNewFriend)

        # НИЖЕ КНОПКА ОТПРАВКИ СООБЩЕНИЯ
        self.pushButton_room.clicked.connect(self.roomMessage)

        self.listWidget_msgRoom.verticalScrollBar().valueChanged.connect(self.adding_load)

        # НИЖЕ КНОПКИ С ОКНАМИ НАСТРОЙКИ
        self.pushButton_settings.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_quit.clicked.connect(self.quit)
        self.pushButton_back_tomain.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        # НИЖЕ ПРИ КЛИКЕ НА ИМЯ КОМНАТЫ ПРОИСХОДИТ ЗАГРУЗКА СООБЩЕНИЙ
        self.listWidget_people.clicked.connect(self.loadMSG)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_menu.hide()
        self.pushButton_settings.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.pushButton_toReg.setText(_translate("MainWindow", "Создать аккаунт"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.pushButton_sign.setText(_translate("MainWindow", "Войти"))
        self.label_10.setText(_translate("MainWindow", "Вход"))
        self.label_7.setText(_translate("MainWindow", "Пароль"))
        self.label_5.setText(_translate("MainWindow", "Логин"))
        self.pushButton_reg.setText(_translate("MainWindow", "Готово"))
        self.pushButton_backToSign.setText(_translate("MainWindow", "Отмена"))
        self.label_6.setText(_translate("MainWindow", "Повторите пароль"))
        self.label_9.setText(_translate("MainWindow", "Регистрация"))
        self.listWidget_title.setText(_translate("MainWindow", ""))
        __sortingEnabled = self.listWidget_people.isSortingEnabled()
        self.listWidget_people.setSortingEnabled(False)
        self.listWidget_people.setSortingEnabled(__sortingEnabled)
        self.pushButton_menu.setText(_translate("MainWindow", "Найти друзей"))
        self.textEdit_room.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Candara\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_room.setText(_translate("MainWindow", "Отправить"))
        self.pushButton_quit.setText(_translate("MainWindow", "Выйти"))
        self.label_of_creator.setText(
            _translate("MainWindow", "The_messenger             |               Nikita Tarasov"))