import pickle
import socket
import sys
import threading
import time
from configparser import ConfigParser

from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QWidget
from notifypy import Notify

import ui_client


class Client(socket.socket):
    def __init__(self):  # Connect to server
        configfile = "config.ini"
        config = ConfigParser()
        config.read(configfile)
        super().__init__()
        self.connect((config["client"]["ip"], int(config["client"]["port"])))

    def send_data(self, data_text):  # Send data on server
        self.sendall(data_text)


class Ui_MainWindow(ui_client.UI_ForMain, QWidget):
    def __init__(self, MainWindow, ChildWindow):
        super().__init__()
        super().setupUi(MainWindow, ChildWindow, )
        self.cl = Client()

        threading.Thread(target=self.get_text).start()
        self.canLoad = True
        self.roomsForLoad = []
        self.animation_play = False
        self.notify = Notify()
        print("Connect")

    def get_text(self, ):
        # We receive text from the server USING the client (Client)
        while True:
            data = self.cl.recv(2048)
            data = pickle.loads(data)
            print(f"Данные от сервера --- >{data}")
            if data[0] == "USER IS SIGN":  # Login check (Server confirmed login with a message)
                print("YOU GOT IN")
                try:
                    for item in data[1]:
                        self.roomsForLoad.append(item)
                except IndexError:
                    pass
                self.nick_name = self.LP_RForm.lineEdit.text()
                ChildWindow.close()
                self.pushButton_addFriend.show()
                self.pushButton_settings.show()
                self.load()
                MainWindow.setWindowTitle(self.nick_name)
            elif data[0] == "USER_IS_NOT_SIGN":
                self.LP_RForm.label.setText("Неправлиьный логин или пароль")
                self.LP_RForm.lineEdit.setStyleSheet("border: 1px solid rgb(94, 0, 1);")
                self.LP_RForm.lineEdit_2.setStyleSheet("border: 1px solid rgb(94, 0, 1);")
                print("USER_IS_NOT_SIGN")
            elif data[0] == "MSGROOM":
                if self.listWidget_people.currentItem().text() == data[3] or self.listWidget_people.currentItem().text() == data[1]:
                    self.listWidget_msgRoom.addItem(f"{data[1]}: {''.join(data[2])}")
                    time.sleep(0.01)
                    self.listWidget_msgRoom.verticalScrollBar().setValue(
                        self.listWidget_msgRoom.verticalScrollBar().maximum())
                    self.notify.title = f"New message from '{data[1]}': "
                    self.notify.message = f"{''.join(data[2])}"
                    self.notify.icon = "ui/logo_Unitum.png"
                    if data[1] != self.nick_name:
                        self.notify.send()
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
                if data[-1] == "NOMSG":
                    self.listWidget_msgRoom.clear()
                else:

                    self.pushButton_room.show()
                    self.listWidget_msgRoom.clear()
                    bank_of_message = data[-1]
                    bank_of_message.reverse()
                    print(f"Банк сообщений с сервера --->{bank_of_message}")
                    self.listWidget_msgRoom.addItems(bank_of_message)
                    time.sleep(0.01)
                    self.listWidget_msgRoom.verticalScrollBar().setValue(
                        self.listWidget_msgRoom.verticalScrollBar().maximum())
            elif data[0] == "SEARCH":
                match_of_people = pickle.loads(data[1])
                self.AddFRNDForm.listWidget.clear()
                for item in match_of_people:
                    try:
                        if item != self.nick_name and (item not in self.listWidget_people.items()):
                            self.AddFRNDForm.listWidget.addItem(item)
                    except TypeError as error:
                        print(error)
                        try:
                            if item != self.nick_name and item not in self.roomsForLoad[0].values():
                                self.AddFRNDForm.listWidget.addItem(item)
                        except IndexError:
                            self.AddFRNDForm.listWidget.addItem(item)
            elif data[0] == "INFO_CARD":
                self.label_card_fio.setText(data[1])
                self.label_card_post.setText("Должность: " + data[2])
                self.label_card_mail.setText("Эл.Почта: " + data[3])
                self.label_card_phone.setText("Телефон: " + data[4])

    def Sign_in(self):
        login = self.LP_RForm.lineEdit.text()
        password = self.LP_RForm.lineEdit_2.text()

        data_of_sign = ["TRY_TO_ENTRY", login, password]
        data_of_sign = pickle.dumps(data_of_sign)

        self.cl.send_data(data_of_sign)

    def shotdown(self):  # К хренам обрумаем ему все его костыли и прога умирает от нажатия на Крестик
        print("ОКНО ЗАКРЫТО ПО ЖЕЛАНИЮ ПОЛЬЗОВАТЕЛЯ")
        msg_error = ["USER_OUT", self.nick_name]

        self.cl.send_data(pickle.dumps(msg_error))
        raise Exception

    def quit(self):
        data_of_sign = ["USER_OUT", self.nick_name]
        data_of_sign = pickle.dumps(data_of_sign)
        self.cl.send_data(data_of_sign)
        self.textEdit_room.clear()
        self.listWidget_msgRoom.clear()
        self.pushButton_label.setText("")
        self.roomsForLoad.clear()
        self.label_card_mail.clear()
        self.label_card_post.clear()
        self.label_card_fio.clear()
        self.label_card_phone.clear()
        self.listWidget_people.clear()
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_room.hide()
        self.pushButton_addFriend.hide()
        self.pushButton_settings.hide()
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
                    self.pushButton_label.setText("")
                    self.pushButton_label.setText(nameRoom)
                    if self.listWidget_people.currentItem().text() == nameRoom:
                        ind_start = self.listWidget_msgRoom.count()
                        msg_room = ["LOADMSG_ADD", IDRoom, ind_start, ]
                        msg_room = pickle.dumps(msg_room)
                        self.cl.send_data(msg_room)
                        break
        except IndexError as error:
            print(f"{error}, value_ofScrollBar --> {value_ofScrollBar}")


    def loadMSG(self):

        if self.frame.maximumWidth() == 600:
            self.anim.setDuration(50)
            self.anim.setStartValue(600)
            self.anim.setEndValue(0)
            self.anim.start()
            self.animation_play = False
        self.pushButton_room.show()
        try:
            for IDRoom, nameRoom in self.roomsForLoad[0].items():
                self.pushButton_label.setText("")
                self.pushButton_label.setText(nameRoom)

                if self.listWidget_people.currentItem().text() == nameRoom:
                    msg_room = ["LOADMSG", IDRoom, nameRoom, ]
                    msg_room = pickle.dumps(msg_room)
                    self.cl.send_data(msg_room)
                    break
        except IndexError:
            print("IndexError IN loadMSG")

    def show_card_of_user(self):
        self.anim = QPropertyAnimation(self.frame, b'maximumWidth')
        if self.animation_play:
            self.animation_play = False
            self.anim.setDuration(50)
            self.anim.setStartValue(600)
            self.anim.setEndValue(0)
            self.anim.start()
        else:
            self.animation_play = True
            self.anim.setDuration(50)
            self.anim.setStartValue(0)
            self.anim.setEndValue(600)
            self.anim.start()

    def searchPeople(self):
        self.AddFRNDWindow.show()
        if self.AddFRNDForm.lineEdit.text().strip() != "":
            men = ["SEARCH", self.AddFRNDForm.lineEdit.text()]
            men = pickle.dumps(men)
            self.cl.send_data(men)

    def roomMessage(self):
        for IDRoom, nameRoom in self.roomsForLoad[0].items():
            if self.listWidget_people.currentItem().text() == nameRoom and self.textEdit_room.toPlainText().strip() != "":
                list_for_server = ["MSGROOM", IDRoom, self.nick_name, self.listWidget_people.currentItem().text(),
                                   self.textEdit_room.toPlainText().strip()]
                list_for_server = pickle.dumps(list_for_server)
                self.cl.send_data(list_for_server)
                self.textEdit_room.clear()
                self.textEdit_room.setFocus()
                break

    def addNewFriend(self):
        new_room = ["CRT_ROOM", self.AddFRNDForm.listWidget.currentItem().text(), self.nick_name, ]
        new_room = pickle.dumps(new_room)
        self.AddFRNDWindow.close()
        self.cl.send_data(new_room)

    def load_info_card(self):
        if self.pushButton_label.text() != "":
            info_card = ["INFO_CARD", self.listWidget_people.currentItem().text(), self.nick_name, ]
            info_card = pickle.dumps(info_card)
            self.cl.send_data(info_card)

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
