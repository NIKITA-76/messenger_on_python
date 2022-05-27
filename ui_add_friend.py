from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddFriend(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 461)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                 "\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(12, 24, 411, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "background-color: rgb(100, 100, 100);\n"
                                    "color: rgb(35, 35, 35);\n"
                                    "border-radius: 6px;\n"
                                    "font: 25 18pt \"Microsoft YaHei\";\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus{\n"
                                    "color: rgb(35, 35, 35);\n"
                                    "border-radius: 6px;\n"
                                    "\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(-1, 82, 518, 331))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                      "color: rgb(158, 158, 158);\n"
                                      "font: 25 18pt \"Microsoft YaHei\";\n"
                                      "\n"
                                      "")
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(55, 422, 410, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(100, 100, 100);\n"
                                      "color: rgb(35, 35, 35);\n"
                                      "border-radius: 6px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(130, 130, 130);\n"
                                      "color: rgb(35, 35, 35);\n"
                                      "border-radius: 6px;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton_sign")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(433, 24, 75, 35))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "background-color: rgb(100, 100, 100);\n"
                                        "color: rgb(35, 35, 35);\n"
                                        "border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(130, 130, 130);\n"
                                        "color: rgb(35, 35, 35);\n"
                                        "border-radius: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_toReg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Поиск"))
