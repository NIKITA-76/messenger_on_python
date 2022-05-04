from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_LandP_Reg(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(556, 427)
        MainWindow.setMinimumSize(QtCore.QSize(435, 253))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 541, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(8, 0))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page_setting")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(147, 218, 245, 20))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(147, 130, 245, 20))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_toReg = QtWidgets.QPushButton(self.page)
        self.pushButton_toReg.setGeometry(QtCore.QRect(249, 268, 145, 23))
        self.pushButton_toReg.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_toReg.setObjectName("pushButton_toReg")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(148, 108, 241, 20))
        self.label.setStyleSheet("color: rgb(158, 158, 158);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(145, 268, 75, 23))
        self.pushButton.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton.setObjectName("pushButton_settings")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(143, 198, 251, 20))
        self.label_2.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_info = QtWidgets.QLabel(self.page_2)
        self.label_info.setGeometry(QtCore.QRect(130, 258, 279, 20))
        self.label_info.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_info.setText("")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.lineEdit_log = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_log.setGeometry(QtCore.QRect(180, 78, 271, 20))
        self.lineEdit_log.setObjectName("lineEdit_log")
        self.label_pass2 = QtWidgets.QLabel(self.page_2)
        self.label_pass2.setGeometry(QtCore.QRect(20, 219, 131, 20))
        self.label_pass2.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_pass2.setObjectName("label_pass2")
        self.label_log = QtWidgets.QLabel(self.page_2)
        self.label_log.setGeometry(QtCore.QRect(25, 80, 106, 20))
        self.label_log.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_log.setAlignment(QtCore.Qt.AlignCenter)
        self.label_log.setObjectName("label_log")
        self.pushButton_ready = QtWidgets.QPushButton(self.page_2)
        self.pushButton_ready.setGeometry(QtCore.QRect(126, 290, 81, 31))
        self.pushButton_ready.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_ready.setObjectName("pushButton_ready")
        self.pushButton_back = QtWidgets.QPushButton(self.page_2)
        self.pushButton_back.setGeometry(QtCore.QRect(330, 290, 81, 31))
        self.pushButton_back.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_back.setObjectName("pushButton_back")
        self.lineEdit_pass2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_pass2.setGeometry(QtCore.QRect(180, 219, 271, 20))
        self.lineEdit_pass2.setObjectName("lineEdit_pass2")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_pass.setGeometry(QtCore.QRect(180, 163, 271, 20))
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.label_pass = QtWidgets.QLabel(self.page_2)
        self.label_pass.setGeometry(QtCore.QRect(29, 166, 101, 20))
        self.label_pass.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pass.setObjectName("label_pass")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_toReg.setText(_translate("MainWindow", "Создать аккаунт"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label_pass2.setText(_translate("MainWindow", "Повторите пароль"))
        self.label_log.setText(_translate("MainWindow", "Логин"))
        self.pushButton_ready.setText(_translate("MainWindow", "Готово"))
        self.pushButton_back.setText(_translate("MainWindow", "Отмена"))
        self.label_pass.setText(_translate("MainWindow", "Пароль"))
