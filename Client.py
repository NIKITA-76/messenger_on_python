import pickle
import socket
import sys
import threading

from PyQt5 import QtCore, QtWidgets, QtGui

from AddFriend import Ui_AddFriend
from LandP import Ui_LandP
from Reg import Ui_Reg

"""
v0.4.0 - Добавлена возможность общаться не через локальный айпи а полноценно 
         через интернет ВНЕ локального роутера

v0.4.5 - Переработан дизайн (из-за утери старого) в лучшую сторону. 
         Добалена возможность видеть кол-во пользователей онлайн

v0.4.7 - Ипсравлен костылями баг, теперь можно нормально закрывать программу и будет все ок

v0.4.9 - Убрана возможность отсылать пустые пробелы. 
         Так же, больше нельзя отсылать сообщения с пробелами в начале и в концах

v0.5.0 - Реализовано окно входа.
         При попытке запуска программы вторым экземпляром,
         пользователь не сможет отправлять сообщения
         анти спам (доработать(ну желательно). 

         После запуска каждое последнее окно дает СОР, но не первое )
"""


class Client(socket.socket):
    def __init__(self):  # Connect to server
        super().__init__()
        self.connect(("178.69.39.227", 9090))

    def send_data(self, data_text):  # Send data on server
        self.send(data_text)


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self):
        self.canLoad = True
        self.user_is_sign = False
        self.can_write = False
        self.cl = Client()

        self.roomsForLoad = []
        global ChildWindow

        ChildWindow = QtWidgets.QMainWindow()
        self.LPForm = Ui_LandP()
        self.LPForm.setupUi(ChildWindow)

        self.thr = threading.Thread(target=self.get_text).start()

        self.AddFRNDWindow = QtWidgets.QMainWindow()
        self.AddFRNDForm = Ui_AddFriend()
        self.AddFRNDForm.setupUi(self.AddFRNDWindow)

        self.RegWindow = QtWidgets.QMainWindow()
        self.RegForm = Ui_Reg()
        self.RegForm.setupUi(self.RegWindow)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1291, 865)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(451, 0, 841, 866))
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
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.listWidget_chat = QtWidgets.QListWidget(self.page_1)
        self.listWidget_chat.setGeometry(QtCore.QRect(0, 40, 902, 411))
        self.listWidget_chat.setStyleSheet("color: rgb(158, 158, 158);")
        self.listWidget_chat.setObjectName("listWidget_chat")

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.listWidget_msgRoom = QtWidgets.QListWidget(self.page_4)
        self.listWidget_msgRoom.setGeometry(QtCore.QRect(0, 50, 840, 651))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.listWidget_msgRoom.setFont(font)
        self.listWidget_msgRoom.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                              "color: rgb(158, 158, 158);\n"
                                              "border:0px;\n"
                                              "border-top:1px solid rgb(158, 158, 158);")
        self.listWidget_msgRoom.setObjectName("listWidget_msgRoom")
        self.frame_2 = QtWidgets.QFrame(self.page_4)
        self.frame_2.setGeometry(QtCore.QRect(0, 680, 841, 191))
        self.frame_2.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                   "\n"
                                   "border:0px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit_room = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_room.setGeometry(QtCore.QRect(50, 40, 671, 95))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit_room.setFont(font)
        self.textEdit_room.setMouseTracking(False)
        self.textEdit_room.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                         "font: 14pt \"Candara\";\n"
                                         "color: rgb(158, 158, 158);\n"
                                         "border:0px;\n"
                                         "border-radius: 12px;\n"
                                         "")
        self.textEdit_room.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_room.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit_room.setOverwriteMode(False)
        self.textEdit_room.setPlaceholderText("")
        self.textEdit_room.setObjectName("textEdit_room")
        self.pushButton_room = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_room.setGeometry(QtCore.QRect(740, 40, 71, 95))
        self.pushButton_room.setStyleSheet(
                                            "\n\nQPushButton{\nbackground-color: rgb(50, 50, 50);\nborder-radius: 12px;\n"
                                            "color:rgb(158, 158, 158);\n\n}\n\nQPushButton:hover{\n"
                                            "background-color: rgb(65, 65, 65);\ncolor:rgb(158, 158, 158);\n"
                                            "border-radius: 12px;\n}\n\n\n\n")
        self.pushButton_room.setObjectName("pushButton_room")
        self.listWidget_title = QtWidgets.QListWidget(self.page_4)
        self.listWidget_title.setGeometry(QtCore.QRect(0, 0, 841, 51))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(22)
        self.listWidget_title.setFont(font)
        self.listWidget_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_title.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                            "color: rgb(158, 158, 158);\n"
                                            "border:0px;\n"
                                            "")
        self.listWidget_title.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget_title.setObjectName("listWidget_title")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget_title.addItem(item)
        self.frame_2.raise_()
        self.listWidget_title.raise_()
        self.listWidget_msgRoom.raise_()
        self.stackedWidget.addWidget(self.page_4)
        self.listWidget_people = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_people.setGeometry(QtCore.QRect(0, 60, 451, 806))
        self.listWidget_people.setAutoFillBackground(False)
        self.listWidget_people.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                             "font: 25 18pt \"Microsoft YaHei\";\n"
                                             "color: rgb(158, 158, 158);\n"
                                             "border:0px;\n"
                                             "")
        self.listWidget_people.setObjectName("listWidget_people")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 461, 80))
        self.frame.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.pushButton_search = QtWidgets.QPushButton(self.frame)
        self.pushButton_search.setGeometry(QtCore.QRect(10, 14, 427, 31))
        self.pushButton_search.setStyleSheet(
            "\n\nQPushButton{\nbackground-color: rgb(100, 100, 100);\n"
            "\ncolor: rgb(50, 50, 50);\nborder:0px;\nborder-radius: 6px;\n"
            "}\n\nQPushButton:hover{\nbackground-color: rgb(130, 130, 130);\n"
            "color: rgb(50, 50, 50);\nborder-radius: 6px;\n}\n\n\n\n")
        self.pushButton_search.setObjectName("pushButton_search")
        self.frame.raise_()
        self.stackedWidget.raise_()
        self.listWidget_people.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.RegForm.pushButton_2.clicked.connect(lambda: self.RegWindow.close())

        # self.pushButton_2.clicked.connect(self.searchPeople)
        self.LPForm.pushButton.clicked.connect(self.Sign_in)
        self.LPForm.pushButton_2.clicked.connect(lambda: self.RegWindow.show())
        self.RegForm.pushButton.clicked.connect(self.Reg_in)

        self.pushButton_search.clicked.connect(lambda: self.AddFRNDWindow.show())
        self.AddFRNDForm.pushButton_2.clicked.connect(self.searchPeople)
        self.AddFRNDForm.pushButton.clicked.connect(self.addNewFriend)

        self.pushButton_room.clicked.connect(self.roomMessage)

        self.listWidget_people.clicked.connect(self.loadMSG)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        __sortingEnabled = self.listWidget_msgRoom.isSortingEnabled()
        self.listWidget_msgRoom.setSortingEnabled(False)
        self.listWidget_msgRoom.setSortingEnabled(__sortingEnabled)
        self.textEdit_room.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Candara\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_room.setText(_translate("MainWindow", "Отправить"))
        __sortingEnabled = self.listWidget_title.isSortingEnabled()
        self.listWidget_title.setSortingEnabled(False)
        item = self.listWidget_title.item(0)
        item.setText(_translate("MainWindow", ""))
        self.listWidget_title.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_people.isSortingEnabled()
        self.listWidget_people.setSortingEnabled(False)
        self.listWidget_people.setSortingEnabled(__sortingEnabled)
        self.pushButton_search.setText(_translate("MainWindow", "Найти друзей"))

    def get_text(self):
        # We receive text from the server USING the client (Client)

        while True:
            try:

                data = self.cl.recv(2048)
                data = pickle.loads(data)
                print(f"Данные от сервера --- >{data}")

                if data[0] == "USER IS SIGN":  # Login check (Server confirmed login with a message)

                    print("YOU GOT IN")
                    self.can_write = True
                    self.user_is_sign = True
                    try:
                        for item in data[1]:
                            self.roomsForLoad.append(item)

                    except IndexError:
                        pass

                    self.nickName = self.LPForm.lineEdit.text()
                    ChildWindow.close()
                    self.load()

                elif data[0] == "USER_IS_REG":
                    self.RegWindow.close()

                elif data[0] == "HAVE_THIS_USER":
                    self.RegForm.label_4.setText("Пользователь с таким Логином уже сущестует")

                elif data[0] == "USER_IS_NOT_SIGN":
                    self.LPForm.label.setText("Неправлиьный логин или пароль")
                    self.LPForm.lineEdit.setStyleSheet("border: 1px solid rgb(94, 0, 1);")
                    self.LPForm.lineEdit_2.setStyleSheet("border: 1px solid rgb(94, 0, 1);")
                    print("USER_IS_NOT_SIGN")

                elif data[0] == "MSGROOM":
                    print(f"MSG FROM SRV FOR ROOM ---> {data[0]}")
                    x = " ".join(data[-1])
                    self.listWidget_msgRoom.addItem(f"{data[1]}: {x}")

                elif data[0] == "CRT_ROOM":
                    try:
                        self.roomsForLoad[0].update(data[1])
                        print(f"self.roomsForLoad --- >{self.roomsForLoad}")
                    except IndexError:
                        print(data[1])
                        for key, value in data[1].items():

                            self.listWidget_people.addItem(value)
                        self.roomsForLoad.append(data[1])
                        print(f"self.roomsForLoad --- >{self.roomsForLoad}")

                elif data[0] == "LOADMSG":
                    if data[1] == "NOMSG":
                        self.listWidget_msgRoom.clear()
                    else:
                        self.listWidget_msgRoom.clear()
                        x = data[1]
                        print(f"x--->{x}")
                        self.listWidget_msgRoom.addItems(x)

                elif data[1][0] == "SEARCH":

                    x = data[1][1]
                    y = pickle.loads(x)
                    print(y)
                    self.AddFRNDForm.listWidget.clear()
                    for item in y:
                        try:
                            if item != self.nickName and (item not in self.listWidget_people.items()):
                                self.AddFRNDForm.listWidget.addItem(item)
                        except TypeError as error:
                            if item != self.nickName:
                                self.AddFRNDForm.listWidget.addItem(item)
                            print(error)


            except EOFError or KeyError:
                """
                Curve check to run the program more than once o n one pc, 
                so that one user cannot run the client many times
                """

                print("EOFError")
                self.label_countUser.setText("!ВЫ ЗАПУСТИЛИ !")
                self.pushButton.setEnabled(False)

                input()

    def Reg_in(self):
        login_reg = self.RegForm.lineEdit.text()
        if self.RegForm.lineEdit_2.text().strip() == self.RegForm.lineEdit_3.text().strip():
            password_reg = self.RegForm.lineEdit_3.text().strip()
            data_of_reg = ["TRY_TO_REG", login_reg, password_reg]
            data_of_reg = pickle.dumps(data_of_reg)
            self.cl.send_data(data_of_reg)

        else:
            self.RegForm.label_4.setText("Пороли не совпадают!")

    def Sign_in(self):  # ChildWindow

        login = self.LPForm.lineEdit.text()
        password = self.LPForm.lineEdit_2.text()

        data_of_sign = ["TRY_TO_ENTRY", login, password]
        data_of_sign = pickle.dumps(data_of_sign)

        self.cl.send_data(data_of_sign)

    # def send_text_with_enter(
    #        self):  # Sending text to the client by pressing Enter NOT A CRAWLER BUT A TEMPORARY MEASURE
    #
    #       while True:
    #          keyboard.wait('Enter')
    #         if (self.textEdit.toPlainText()).strip() != "" and self.can_write:
    #            text = (self.nickName).strip() + ": " + (self.textEdit.toPlainText()).strip()
    #           text = pickle.dumps(text)
    #          self.cl.send_data(text)
    #         self.textEdit.setText("")

    def shotdown(self):  # К хренам обрумаем ему все его костыли и прога умирает от нажатия на Крестик
        print("ОКНО ЗАКРЫТО ПО ЖЕЛАНИЮ ПОЛЬЗОВАТЕЛЯ")
        msgError = ["USER_OUT", self.nickName]

        self.cl.send_data(pickle.dumps(msgError))
        raise Exception

    def load(self):
        try:
            print(self.roomsForLoad[0])
            if self.canLoad:
                for item in self.roomsForLoad[0].values():
                    self.listWidget_people.addItem(item)
            self.canLoad = False
        except IndexError:
            pass

    def send_text(self):  # Sending text to client on button click

        if (self.textEdit.toPlainText()).strip() != "" and self.can_write:
            text = (self.nickName).strip() + ": " + (self.textEdit.toPlainText()).strip()
            text = pickle.dumps(text)
            print(f"Сообщение отправленное на сервер в байтах ---> {text}")
            self.cl.send_data(text)
            self.textEdit.setText("")

    def correctItemInList(self):
        list_item = ["ITEM", self.listWidget_people.currentItem().text()]
        list_item = pickle.dumps(list_item)
        print(list_item)
        self.cl.send_data(list_item)

    def searchPeople(self):
        self.AddFRNDWindow.show()
        if self.AddFRNDForm.lineEdit.text().strip() != "":
            men = ["SEARCH", self.AddFRNDForm.lineEdit.text()]
            men = pickle.dumps(men)
            self.cl.send_data(men)

    def crtRoom(self):
        usersInNewRoom = self.listWidget.selectedItems()
        newRoom = [self.nickName]
        for item in usersInNewRoom:
            item = item.text()
            newRoom.append(item)
        newRoom.insert(0, "CRT_ROOM")
        newRoom.insert(1, self.lineEdit_2.text())
        print(newRoom)
        newRoom = pickle.dumps(newRoom)
        self.cl.send_data(newRoom)
        self.listWidget_rooms.addItem(self.lineEdit_2.text())

    def loadMSG(self):
        try:
            for IDRoom, nameRoom in self.roomsForLoad[0].items():
                self.listWidget_title.clear()
                self.listWidget_title.addItem(nameRoom)
                print(f"self.IDRoom --- >{IDRoom}")
                if self.listWidget_people.currentItem().text() == nameRoom:
                    msgRoom = ["LOADMSG", IDRoom]
                    print(msgRoom)
                    msgRoom = pickle.dumps(msgRoom)
                    self.cl.send_data(msgRoom)
                    break
        except IndexError:
            print("IndexError")

    def roomMessage(self):
        if self.can_write:
            for IDRoom, nameRoom in self.roomsForLoad[0].items():
                print(f"self.roomsForLoad --- >{self.roomsForLoad}")
                print(f"self.IDRoom --- >{IDRoom}")
                if self.listWidget_people.currentItem().text() == nameRoom:
                    list = ["MSGROOM", IDRoom, self.nickName, self.listWidget_people.currentItem().text(),
                            self.textEdit_room.toPlainText()]
                    print(f"list to server --- >{list}")
                    list = pickle.dumps(list)
                    self.cl.send_data(list)
                    self.textEdit_room.clear()

    def addNewFriend(self):
        friend = self.AddFRNDForm.listWidget.currentItem()
        self.listWidget_people.addItem(friend.text())
        newRoom = [self.nickName]
        newRoom.insert(0, "CRT_ROOM")
        newRoom.insert(1, self.AddFRNDForm.listWidget.currentItem().text())
        print(newRoom)
        newRoom = pickle.dumps(newRoom)
        self.cl.send_data(newRoom)
        self.listWidget_people.addItem(friend)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    MainWindow.show()
    ChildWindow.show()
    app.lastWindowClosed.connect(ui.shotdown)
    sys.exit(app.exec_())
