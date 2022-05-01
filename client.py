import pickle
import socket
import sys
import time
import threading
import ui_client

from configparser import ConfigParser
from PyQt5 import QtWidgets


class Client(socket.socket):
    def __init__(self):  # Connect to server
        configfile = "config.ini"
        config = ConfigParser()
        config.read(configfile)
        super().__init__()
        self.connect((config["client"]["ip"], int(config["client"]["port"])))

    def send_data(self, data_text):  # Send data on server
        self.send(data_text)


class Ui_MainWindow(ui_client.UI_ForMain):
    def __init__(self, MainWindow, ChildWindow):
        super().setupUi(MainWindow, ChildWindow)
        self.cl = Client()
        self.thr = threading.Thread(target=self.get_text).start()
        self.canLoad = True
        self.can_write = False
        self.roomsForLoad = []

    def get_text(self,):
        # We receive text from the server USING the client (Client)
        while True:
            data = self.cl.recv(2048)
            data = pickle.loads(data)
            print(f"Данные от сервера --- >{data}")
            if data[0] == "USER IS SIGN":  # Login check (Server confirmed login with a message)
                print("YOU GOT IN")
                self.can_write = True
                print(self.roomsForLoad)
                try:
                    for item in data[1]:
                        self.roomsForLoad.append(item)
                except IndexError:
                    pass
                self.nickName = self.LP_RForm.lineEdit.text()
                ChildWindow.close()
                self.load()

            elif data[0] == "USER_IS_REG":

                self.LP_RForm.stackedWidget.setCurrentIndex(0)
            elif data[0] == "HAVE_THIS_USER":

                self.RegForm.label_4.setText("Пользователь с таким Логином уже сущестует")
            elif data[0] == "USER_IS_NOT_SIGN":
                self.LP_RForm.label.setText("Неправлиьный логин или пароль")
                self.LP_RForm.lineEdit.setStyleSheet("border: 1px solid rgb(94, 0, 1);")
                self.LP_RForm.lineEdit_2.setStyleSheet("border: 1px solid rgb(94, 0, 1);")
                print("USER_IS_NOT_SIGN")

            elif data[0] == "MSGROOM":
                if self.listWidget_people.currentItem().text() == data[3]:
                    self.listWidget_msgRoom.addItem(f"{data[1]}: {' '.join(data[2])}")
                    time.sleep(0.01)
                    self.listWidget_msgRoom.verticalScrollBar().setValue(
                        self.listWidget_msgRoom.verticalScrollBar().maximum())

            elif data[0] == "CRT_ROOM":
                try:
                    self.roomsForLoad[0].update(data[1])
                except IndexError:
                    self.roomsForLoad.append(data[1])
                for _, value in data[1].items():
                    self.listWidget_people.addItem(value)

            elif data[0] == "LOADMSG_ADD":
                data[1].reverse()
                self.listWidget_msgRoom.verticalScrollBar().setValue(3)
                self.listWidget_msgRoom.insertItems(0, data[1])

            elif data[0] == "LOADMSG":
                if data[1] == "NOMSG":
                    self.listWidget_msgRoom.clear()
                else:
                    self.listWidget_msgRoom.clear()
                    bankOfMessage = data[1]
                    bankOfMessage.reverse()
                    print(f"Банк сообщений с сервера --->{bankOfMessage}")
                    self.listWidget_msgRoom.addItems(bankOfMessage)
                    time.sleep(0.01)
                    self.listWidget_msgRoom.verticalScrollBar().setValue(
                        self.listWidget_msgRoom.verticalScrollBar().maximum())

            elif data[0] == "SEARCH":
                matchOfPeople = pickle.loads(data[1])
                self.AddFRNDForm.listWidget.clear()
                for item in matchOfPeople:
                    try:
                        if item != self.nickName and (item not in self.listWidget_people.items()):
                            self.AddFRNDForm.listWidget.addItem(item)
                    except TypeError as error:
                        if item != self.nickName:
                            self.AddFRNDForm.listWidget.addItem(item)





    def Reg_in(self):
        login_reg = self.LP_RForm.lineEdit_log.text().strip()
        if self.LP_RForm.lineEdit_pass.text().strip() == self.LP_RForm.lineEdit_pass2.text().strip():
            password_reg = self.LP_RForm.lineEdit_pass.text().strip()
            data_of_reg = ["TRY_TO_REG", login_reg, password_reg]
            data_of_reg = pickle.dumps(data_of_reg)
            self.cl.send_data(data_of_reg)

        else:
            self.RegForm.label_4.setText("Пароли не совпадают!")

    def Sign_in(self):  # ChildWindow
        login = self.LP_RForm.lineEdit.text()
        password = self.LP_RForm.lineEdit_2.text()

        data_of_sign = ["TRY_TO_ENTRY", login, password]
        data_of_sign = pickle.dumps(data_of_sign)
        print(data_of_sign)

        self.cl.send_data(data_of_sign)

    def shotdown(self):  # К хренам обрумаем ему все его костыли и прога умирает от нажатия на Крестик
        print("ОКНО ЗАКРЫТО ПО ЖЕЛАНИЮ ПОЛЬЗОВАТЕЛЯ")
        msgError = ["USER_OUT", self.nickName]

        self.cl.send_data(pickle.dumps(msgError))
        raise Exception

    def quit(self):
        data_of_sign = ["USER_OUT", self.nickName]
        data_of_sign = pickle.dumps(data_of_sign)
        self.cl.send_data(data_of_sign)
        self.textEdit_room.clear()
        self.listWidget_msgRoom.clear()
        self.listWidget_title.clear()
        self.roomsForLoad.clear()
        self.listWidget_people.clear()
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_room.hide()
        ChildWindow.show()

    def load(self):
        try:
            for item in self.roomsForLoad[0].values():
                self.listWidget_people.addItem(item)
        except IndexError:
            pass

    def adding_load(self, value_ofScrollBar):
        try:
            if value_ofScrollBar == 0:
                for IDRoom, nameRoom in self.roomsForLoad[0].items():
                    self.listWidget_title.clear()
                    self.listWidget_title.setText(nameRoom)
                    if self.listWidget_people.currentItem().text() == nameRoom:
                        ind_start = self.listWidget_msgRoom.count()
                        msg_room = ["LOADMSG_ADD", IDRoom, ind_start, ]
                        msg_room = pickle.dumps(msg_room)
                        self.cl.send_data(msg_room)
                        break
        except IndexError as error:
            print(f"{error}, value_ofScrollBar --> {value_ofScrollBar}")

    def loadMSG(self):
        self.pushButton_room.show()
        try:
            for IDRoom, nameRoom in self.roomsForLoad[0].items():
                self.listWidget_title.clear()
                self.listWidget_title.setText(nameRoom)
                if self.listWidget_people.currentItem().text() == nameRoom:
                    msgRoom = ["LOADMSG", IDRoom, ]
                    msgRoom = pickle.dumps(msgRoom)
                    self.cl.send_data(msgRoom)
                    break
        except IndexError:
            print("IndexError IN loadMSG")

    def searchPeople(self):
        self.AddFRNDWindow.show()
        if self.AddFRNDForm.lineEdit.text().strip() != "":
            men = ["SEARCH", self.AddFRNDForm.lineEdit.text()]
            men = pickle.dumps(men)
            self.cl.send_data(men)

    def roomMessage(self):

        if self.can_write:
            for IDRoom, nameRoom in self.roomsForLoad[0].items():
                if self.listWidget_people.currentItem().text() == nameRoom and self.textEdit_room.toPlainText().strip() != "" and self.can_write:
                    list = ["MSGROOM", IDRoom, self.nickName, self.listWidget_people.currentItem().text(),
                            self.textEdit_room.toPlainText().strip()]
                    list = pickle.dumps(list)
                    self.cl.send_data(list)
                    self.textEdit_room.clear()
                    self.textEdit_room.setFocus()

    def addNewFriend(self):
        newRoom = ["CRT_ROOM", self.AddFRNDForm.listWidget.currentItem().text(), self.nickName, ]
        newRoom = pickle.dumps(newRoom)
        self.AddFRNDWindow.close()
        self.cl.send_data(newRoom)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ChildWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow, ChildWindow)
    ui.setupUi(MainWindow, ChildWindow)
    MainWindow.show()
    ChildWindow.show()
    app.lastWindowClosed.connect(ui.shotdown)
    sys.exit(app.exec_())
