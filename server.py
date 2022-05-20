import logging
import pickle
import socket
import sys
import threading

from PyQt5 import QtWidgets

from init_data import Data
from ui_server import Ui_Server


class Server(socket.socket, Ui_Server):
    def __init__(self, ):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.data = Data()
        self.bind((self.data.config["server"]["ip"], int(self.data.config["server"]["port"])))
        self.listen()
        logging.basicConfig(level="INFO")
        self.logger_login = logging.getLogger("log_in")
        self.logger_package_MSG = logging.getLogger("load_MSG_for_client")
        self.logger_accept = logging.getLogger("start_server")
        self.logger_listen_socket = logging.getLogger("listen_socket")
        self.logger_accept.setLevel("DEBUG")
        self.logger_accept.setLevel("ERROR")
        self.create_room()
        self.x = threading.Thread(target=self.start_server).start()
        app = QtWidgets.QApplication(sys.argv)
        Ui_Server = QtWidgets.QMainWindow()
        super().setupUi(Ui_Server, )
        Ui_Server.show()
        app.lastWindowClosed.connect(self.shotdown)
        sys.exit(app.exec_())

    def shotdown(self):  # К хренам обрумаем ему все его костыли и прога умирает от нажатия на Крестик
        print("ОКНО ЗАКРЫТО ПО ЖЕЛАНИЮ ПОЛЬЗОВАТЕЛЯ")
        raise Exception

    def listen_socket(self, ip_user, socket_user, ):  # Accept text from client
        try:
            while True:  # Accepting a message
                self.signal = socket_user.recv(4096)
                print(f"ДАННЫЕ ОТ КЛИЕНТА --->{self.signal}")
                self.signal = pickle.loads(self.signal)
                if self.signal[0] == "TRY_TO_ENTRY":
                    self.log_in(self.signal, socket_user, ip_user)
                    self.data.name_withIp[self.signal[1]] = self.data.users_ip[0]
                    self.recreating_room_from_JSON()
                elif self.signal[0] == "MSGROOM":
                    self.private_MSG()
                elif self.signal[0] == "SEARCH":
                    self.search_people(socket_user)
                elif self.signal[0] == "CRT_ROOM":
                    self.create_room_JSON()
                elif self.signal[0] == "LOADMSG_ADD":
                    self.add_load_MSG_for_client(socket_user, self.signal[2])
                elif self.signal[0] == "LOADMSG":
                    self.load_MSG_for_client(socket_user)
                elif self.signal[0] == "FILE":
                    self.get_file()
                elif self.signal[0] == "USER_OUT":
                    """
                     Удаление пользователя из комнаты ЛС, так как при подключении пользователя меняеться его 'fd',
                     а в комнате все еще старый объект со старым 'fd'
                    """
                    for roomID, roomName in self.data.DB.find_one({'_id': 'USERS'}, {'_id': 0})[self.signal[1]][
                        "ROOMS"].items():
                        try:
                            self.data.rooms[roomID][0].pop(self.signal[1])
                            self.data.userAndObject.pop(self.signal[1])
                            self.data.users.remove(socket_user)
                        except:
                            pass

        except EOFError as error:
            print(f"ERROR IN listen_socket(76) {error}")

    def get_file(self):
        file = open("_SERVER" + self.signal[5], 'ab')
        file.write(self.signal[4])
        file.close()

    # def get_file(self):
    #    for roomID, roomName in self.data.DB.find_one({"_id": "USERS"}, {"_id": 0})[self.signal[2]]["ROOMS"].items():
    #        if roomName == self.signal[3]:
    #            for userInRoom, socket_of_user in self.data.rooms[roomID][0].items():
    #                if userInRoom is not self.signal[2]:
    #                    socket_of_user.send(pickle.dumps(["FILE", self.signal[2], self.signal[4], self.signal[5]]))

    def log_in(self, data,
               socket_user, ip_user):
        try:
            if self.data.DB.find_one({"_id": "USERS"})[data[1]]["password"] == data[2] and self.signal[1]:

                keys = self.data.DB.find_one({"_id": "USERS"})[data[1]]["ROOMS"].keys()
                list_rooms = []
                if not keys:
                    sign_in = ["USER IS SIGN"]
                    self.data.userAndObject[self.signal[1]] = socket_user
                else:
                    list_rooms.append(self.data.DB.find_one({"_id": "USERS"})[data[1]]["ROOMS"])
                    sign_in = ["USER IS SIGN", list_rooms]
                    self.data.userAndObject[self.signal[1]] = socket_user

                self.logger_login.info("USER_IS_SIGN")
                self.data.userAndObject[self.signal[1]] = socket_user
                socket_user.send(pickle.dumps(sign_in))
                self.listWidget_people.addItem(self.signal[1])

            else:
                no_sign_in = ["USER_IS_NOT_SIGN"]
                self.logger_login.info("USER_IS_NOT_SIGN (BAD_PASSWORD)")
                socket_user.send(pickle.dumps(no_sign_in))
        except KeyError:
            no_sign_in = ["USER_IS_NOT_SIGN"]
            self.logger_login.info("USER_IS_NOT_SIGN (BAD_LOGIN)")
            socket_user.send(pickle.dumps(no_sign_in))

    def create_room_JSON(self):
        i = 1
        self.idRoom = self.data.idRoom + 1
        list_users = []
        while i < len(self.signal):
            list_users.append(self.signal[i])
            self.data.DB.update_one({'_id': 'ROOMS'}, {'$set': {str(self.idRoom) + "R": [
                {"USERS": list_users, "NAME": self.signal[2]}]}})
            i += 1
        print("111111111111111111")
        self.data.DB.update_one({'_id': 'COUNT'}, {'$set': {'ROOMS': self.idRoom}})

        self.data.DB.update_one({'_id': 'USERS'},
                                [{'$set': {f'{self.signal[1]}.ROOMS': {str(self.idRoom) + "R": self.signal[2]}}}])

        self.data.DB.update_one({'_id': 'USERS'},
                                [{'$set': {f'{self.signal[2]}.ROOMS': {str(self.idRoom) + "R": self.signal[1]}}}])

        self.data.DB.update_one({'_id': 'MESSAGE'}, {'$set': {str(self.idRoom) + 'R': []}})

        print("ROOM IS CREATE")

        self.create_room()
        self.create_room_now()

    def create_room_now(self):
        name_of_rooms = self.data.DB.find_one({"_id": "ROOMS"},
                                              {
                                                  "_id": 0}).keys()  # Создание комнаты, без необходимости перезагрузки сервера
        for name in name_of_rooms:
            for usersInRoom in self.data.DB.find_one({"_id": "ROOMS"}, {"_id": 0})[name][0]["USERS"]:
                try:
                    if usersInRoom not in self.data.rooms[name][0]:  # Условие, что бы не дублировать в комнаты
                        self.data.rooms[name][0].update({usersInRoom: self.data.userAndObject[usersInRoom]})
                except Exception as error:
                    print(f"ERROR IN create_room_now(150) {error}")

        try:

            self.data.userAndObject[self.signal[1]].send(
                pickle.dumps(["CRT_ROOM", {str(self.idRoom) + "R": self.signal[2]}]))
            self.data.userAndObject[self.signal[2]].send(
                pickle.dumps(["CRT_ROOM", {str(self.idRoom) + "R": self.signal[1]}]))
            print(["CRT_ROOM", {str(self.idRoom) + "R": self.signal[1]}])
        except KeyError:
            self.data.userAndObject[self.signal[2]].send(
                pickle.dumps(["CRT_ROOM", {str(self.idRoom) + "R": self.signal[1]}]))

    def create_room(self):
        name_of_rooms = self.data.DB.find_one({"_id": "ROOMS"}, {"_id": 0}).keys()

        for name in name_of_rooms:
            self.data.rooms[name] = [{}]
        print(self.data.rooms)

    def recreating_room_from_JSON(self):
        name_of_rooms = self.data.DB.find_one({"_id": "ROOMS"}, {"_id": 0}).keys()  # Воссоздание комнат из JSON
        for name in name_of_rooms:
            for usersInRoom in self.data.DB.find_one({"_id": "ROOMS"}, {"_id": 0})[name][0]["USERS"]:
                try:
                    if usersInRoom not in self.data.rooms[name][0]:  # Условие, что бы не дублировать в комнаты
                        self.data.rooms[name][0].update({usersInRoom: self.data.userAndObject[usersInRoom]})
                except KeyError as error:
                    print(f"ERROR IN recreating_room_from_JSON(178) {error}")

    def private_MSG(self):
        print("------------КОМНАТА-------------")
        for roomID, roomName in self.data.DB.find_one({"_id": "USERS"}, {"_id": 0})[self.signal[2]]["ROOMS"].items():
            if roomName == self.signal[3]:
                for userInRoom, socket_of_user in self.data.rooms[roomID][0].items():
                    socket_of_user.send(pickle.dumps(["MSGROOM", self.signal[2], self.signal[-1], self.signal[3]]))
                    print(roomID)
                    print(roomName)
                    print(self.data.rooms[roomID][0])
        self.data.DB.update_one({"_id": "MESSAGE"}, {"$push": {self.signal[1]: f"{self.signal[2]}: {self.signal[-1]}"}})

        print("------------КОНЕЦ КОМНАТЫ-------------")

    def load_MSG_for_client(self, user, ):
        cut_bank_of_messg = []
        bank_of_mess = self.data.DB.find_one({"_id": "MESSAGE"}, {"_id": 0})[self.signal[1]]
        fio_of_user = self.data.DB.find_one({"_id": "USERS"}, {"_id": 0})[self.signal[2]]["FIO"]
        cabinet_of_mess = self.data.DB.find_one({"_id": "USERS"}, {"_id": 0})[self.signal[2]]["post"]
        mail_of_mess = self.data.DB.find_one({"_id": "USERS"}, {"_id": 0})[self.signal[2]]["mail"]
        post_of_mess = self.data.DB.find_one({"_id": "USERS"}, {"_id": 0})[self.signal[2]]["phone"]
        bank_of_mess.reverse()
        try:
            if not bank_of_mess:
                for_load_MSG = pickle.dumps(["LOADMSG", fio_of_user, cabinet_of_mess, mail_of_mess, post_of_mess, "NOMSG", ])
                self.logger_package_MSG.info(f"{['LOADMSG', 'NOMSG']}")
                user.send(for_load_MSG)
            else:
                for i in bank_of_mess:
                    cut_bank_of_messg.append(i)
                    if len(cut_bank_of_messg) == 50:
                        break
                for_load_MSG = pickle.dumps(
                    ["LOADMSG", fio_of_user, cabinet_of_mess, mail_of_mess, post_of_mess, cut_bank_of_messg])
                user.send(for_load_MSG)

        except KeyError as error:
            self.data.DB.find_one({"_id": "MESSAGE"}, {"_id": 0})[self.signal[1]] = []

    def add_load_MSG_for_client(self, user, index_of_start):
        bank_of_mess = self.data.DB.find_one({"_id": "MESSAGE"}, {"_id": 0})[self.signal[1]]
        cut_bank_of_messg = []
        index_of_end = len(bank_of_mess) - index_of_start
        for i in reversed(range(index_of_end)):
            cut_bank_of_messg.append(bank_of_mess[i])
            if len(cut_bank_of_messg) == 50:
                break
        if cut_bank_of_messg:
            for_load_MSG = pickle.dumps(["LOADMSG_ADD", cut_bank_of_messg])
            user.send(for_load_MSG)

    def search_people(self, user_socket):
        users_in_JSON = self.data.DB.find_one({'_id': 'USERS'}, {'_id': 0})
        user_of_search = []
        for user in users_in_JSON:
            if self.signal[1] in user:
                user_of_search.append(user)

        user_of_search = pickle.dumps(["SEARCH", pickle.dumps(user_of_search)])
        user_socket.send(user_of_search)

    def crt_new_user(self, ):
        self.data.idUser += 1
        if self.lineEdit_login.text() not in self.data.DB.find_one({'_id': 'USERS'}, {'_id': 0}):
            if self.lineEdit_pass.text() == self.lineEdit_passw_2.text():
                self.data.DB.update_one({"_id": "USERS"},
                                        {"$set": {self.lineEdit_login.text(): {"password": self.lineEdit_pass.text(),
                                                                               "FIO": self.lineEdit_fio.text(),
                                                                               "post": self.lineEdit_post.text(),
                                                                               "phone": self.lineEdit_phone.text(),
                                                                               "mail": self.lineEdit_mail.text(),
                                                                               # Пока нигде не используется
                                                                               "ROOMS": {}
                                                                               }}})
                self.data.DB.update_one({'_id': 'COUNT'}, {'$set': {"USERS": self.data.idUser}})
                print(f"ПОЛЬЗОВАТЕЛЬ ЗАРЕГИСТРИРОВАН ")
                self.label_info.setText("Пользователь успешно зарегистрирован!")
                self.lineEdit_fio.clear()
                self.lineEdit_phone.clear()
                self.lineEdit_post.clear()
                self.lineEdit_login.clear()
                self.lineEdit_pass.clear()
                self.lineEdit_passw_2.clear()
                self.lineEdit_mail.clear()
            else:
                self.label_info.setText("Пароли не совпадают!")
                print("Passwords don't match")

        else:
            self.label_info.setText("Такой пользователеь уже существует")
            self.label_login.setStyleSheet("color: red")
            print("HAVE_THIS_USER")

    def start_server(self):
        print("Listen")

        while True:
            users_socket, address = self.accept()
            self.logger_accept.debug("USER ACCEPT")

            """
            Checking that the user could not run many clients on one pc
            """
            self.data.users_ip.append(address[0])
            '''
            accept() - Ожидает нового пользователя, и пока новый пользователь не придет
            код дальше не пойдет
            '''
            print("Users accept!" + address[0])  # Вывод айпи нового ползователя
            self.data.users.append(users_socket)  # Добавление нового пользователя в список
            threading.Thread(target=self.listen_socket, args=(address[0], users_socket)).start()
            '''
            Старт потока для принятия сообщений, иначе из-за accept() код дальше не идет
            и функция для принятия сообщения стартует после входа нового пользователя
            '''


if __name__ == '__main__':
    server = Server()
