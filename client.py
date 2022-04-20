import pickle
import socket
import sys
import threading

from PyQt5 import QtCore, QtWidgets, QtGui

import ui_client
from AddFriend import Ui_AddFriend
from users_login import Ui_LandP_Reg

class Client(socket.socket):
    def __init__(self):  # Connect to server
        super().__init__()
        self.connect(("178.71.224.84", 8080))

    def send_data(self, data_text):  # Send data on server
        self.send(data_text)



class Ui_MainWindow(ui_client.UI_ForMain):
    def __init__(self, MainWindow, ChildWindow):
        super().setupUi(MainWindow, ChildWindow)
        self.cl = Client()
        self.thr = threading.Thread(target=self.get_text).start()
        self.canLoad = True
        self.user_is_sign = False
        self.can_write = False
        self.roomsForLoad = []









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

                    self.nickName = self.LP_RForm.lineEdit.text()
                    ChildWindow.close()
                    self.load()
                    self.pushButton_room.show()

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

                elif data[0] == "CRT_ROOM":
                    try:
                        self.roomsForLoad[0].update(data[1])
                    except IndexError:
                        self.roomsForLoad.append(data[1])
                    for _, value in data[1].items():
                        self.listWidget_people.addItem(value)

                elif data[0] == "LOADMSG":
                    if data[1] == "NOMSG":
                        self.listWidget_msgRoom.clear()
                    else:
                        self.listWidget_msgRoom.clear()
                        x = data[1]
                        print(f"Банк сообщений с сервера --->{x}")
                        self.listWidget_msgRoom.addItems(x)

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
        login_reg = self.LP_RForm.lineEdit_log.text().strip()
        if self.LP_RForm.lineEdit_pass.text().strip() == self.LP_RForm.lineEdit_pass2.text().strip():
            password_reg = self.LP_RForm.lineEdit_pass.text().strip()
            data_of_reg = ["TRY_TO_REG", login_reg, password_reg]
            data_of_reg = pickle.dumps(data_of_reg)
            self.cl.send_data(data_of_reg)


        else:
            self.RegForm.label_4.setText("Пароли не совпадают!")

    def Sign_in(self):  # ChildWindow
        print("assdasdasdasdasdasd")
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

    def load(self):
        try:

            if self.canLoad:
                for item in self.roomsForLoad[0].values():
                    self.listWidget_people.addItem(item)
            self.canLoad = False
        except IndexError:
            pass

    def correctItemInList(self):
        list_item = ["ITEM", self.listWidget_people.currentItem().text()]
        list_item = pickle.dumps(list_item)

        self.cl.send_data(list_item)

    def searchPeople(self):
        self.AddFRNDWindow.show()
        if self.AddFRNDForm.lineEdit.text().strip() != "":
            men = ["SEARCH", self.AddFRNDForm.lineEdit.text()]
            men = pickle.dumps(men)
            self.cl.send_data(men)

    def crtRoom(self):
        usersInNewRoom = self.listWidget.selectedItems()
        newRoom = ["CRT_ROOM", self.lineEdit_2.text(), self.nickName]
        for item in usersInNewRoom:
            item = item.text()
            newRoom.append(item)
        newRoom = pickle.dumps(newRoom)
        self.cl.send_data(newRoom)
        self.listWidget_rooms.addItem(self.lineEdit_2.text())

    def loadMSG(self):
        try:
            for IDRoom, nameRoom in self.roomsForLoad[0].items():
                self.listWidget_title.clear()
                self.listWidget_title.setText(nameRoom)

                if self.listWidget_people.currentItem().text() == nameRoom:
                    msgRoom = ["LOADMSG", IDRoom]

                    msgRoom = pickle.dumps(msgRoom)
                    self.cl.send_data(msgRoom)
                    break
        except IndexError:
            print("IndexError IN loadMSG")

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
