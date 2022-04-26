import json
import pickle
import socket
import threading
import logging
from pymongo import MongoClient

from configparser import ConfigParser


class Server(socket.socket):
    def __init__(self):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        logging.basicConfig(level="INFO")
        self.logger_login = logging.getLogger("log_in")
        self.logger_package_MSG = logging.getLogger("load_MSG_for_client")
        self.logger_accept = logging.getLogger("start_server")
        self.logger_listen_socket = logging.getLogger("listen_socket")
        self.logger_accept.setLevel("DEBUG")
        self.logger_accept.setLevel("ERROR")
        configfile = "config.ini"
        config = ConfigParser()
        config.read(configfile)

        client = MongoClient("localhost", 27017)
        collect = client["Messanger"]
        self.DB = collect["msgr"]
        self.idUser = self.DB.find_one({"_id": "COUNT"})["USERS"]
        self.idRoom = self.DB.find_one({"_id": "COUNT"})["ROOMS"]
        print(self.idRoom)

        # with open("DB.json", 'r') as json_file:
        #     self.DB = json.load(json_file)  # ----
        #     self.idRoom = self.DB["COUNT"]["ROOMS"]

        self.bind((config["server"]["ip"], int(config["server"]["port"])))
        self.listen()

        print("Server Listen")
        # ----
        self.users = []  # List of all users
        self.users_ip = []  # List of all users-ip
        self.name_withIp = {}
        self.userAndObject = {}
        self.rooms = {}
        self.create_room()

    def send_data(self, data):  # Send text to all users (in the list)
        try:
            for user in reversed(self.users):
                user.send(pickle.dumps(data))
                print(f"ДАННЫЕ ОТ СЕРВЕРА ----> {data}")

        except Exception as a:
            print(f"_SEND_DATA ---> {a}")

    def listen_socket(self, ip_user, socket_user, ):  # Accept text from client

        # try:
        while True:
            self.data_s = socket_user.recv(2048)  # Accepting a message
            self.data_s = pickle.loads(self.data_s)
            print(f"ДАННЫЕ ОТ КЛИЕНТА --->{self.data_s}")
            if self.data_s[
                0] == "TRY_TO_ENTRY":  # If there is an ENTRY signal from the client, we start the process of checking the data from the user
                self.log_in(self.data_s, socket_user)
                self.name_withIp[self.data_s[1]] = self.users_ip[0]
                self.recreating_room_from_JSON()
            elif self.data_s[0] == "TRY_TO_REG":
                self.registration(self.data_s, socket_user)
            elif self.data_s[0] == "MSGROOM":
                self.private_MSG()
            elif self.data_s[0] == "SEARCH":
                self.search_people()
            elif self.data_s[0] == "CRT_ROOM":
                self.create_room_JSON()
            elif self.data_s[0] == "LOADMSG":
                self.load_MSG_for_client(socket_user)
            elif self.data_s[0] == "USER_OUT":
                """
                 Удаление пользователя из комнаты ЛС, так как при подключении пользователя меняеться его 'fd',
                 а в комнате все еще старый объект со старым 'fd'
                
                """
                for roomID, roomName in self.DB.find_one({'_id': 'USERS'}, {'_id': 0})[self.data_s[1]]["ROOMS"].items():
                    print(f"USER '{self.data_s[1]}' IS OUT")
                    self.rooms[roomID][0].pop(self.data_s[1])
                    self.userAndObject.pop(self.data_s[1])
                    self.users.remove(socket_user)
                    self.users_ip.remove(ip_user)

        # except Exception as a:

    #
    #    try:
    #        self.logger_listen_socket.error(a)
    #        print(f"{self.data_s}")
    #    except Exception:
    #        pass
    #    """
    #       If the client is disconnected, then we remove it from the user array and
    #       the IP array
    #       users at the moment so. (While it works and thank God)
    #    """

    def registration(self, data, user):
        self.idUser += 1
        if data[1] not in self.DB.find_one({'_id': 'USERS'}, {'_id': 0}):
            self.DB.update_one({"_id": "USERS"}, {"$set": {data[1]: {"password": data[2],
                                                                     "ID": self.idUser,  # Пока нигде не используется
                                                                     "ROOMS": {}
                                                                     }}})
            self.DB.find_one({'_id': 'COUNT'}, {'_id': 0})["USERS"] = self.idUser
            print(f"ПОЛЬЗОВАТЕЛЬ ЗАРЕГИСТРИРОВАН ")
            user.send(pickle.dumps(["USER_IS_REG"]))

        else:
            user.send(pickle.dumps(["HAVE_THIS_USER"]))
            print("HAVE_THIS_USER")

    def log_in(self, data,
               socket_user):
        try:
            if self.DB.find_one({"_id": "USERS"})[data[1]]["password"] == data[2] and self.data_s[
                1] not in self.userAndObject.keys():

                keys = self.DB.find_one({"_id": "USERS"})[data[1]]["ROOMS"].keys()
                list_rooms = []
                if not keys:
                    sign_in = ["USER IS SIGN"]
                    self.userAndObject[self.data_s[1]] = socket_user
                else:

                    list_rooms.append(self.DB.find_one({"_id": "USERS"})[data[1]]["ROOMS"])

                    sign_in = ["USER IS SIGN", list_rooms]
                    self.userAndObject[self.data_s[1]] = socket_user

                self.logger_login.info("USER_IS_SIGN")
                self.userAndObject[self.data_s[1]] = socket_user
                socket_user.send(pickle.dumps(sign_in))

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
        self.idRoom = self.idRoom + 1
        listUsers = []
        while i < len(self.data_s):
            listUsers.append(self.data_s[i])
            self.DB.update_one({'_id': 'ROOMS'}, {'$set': {str(self.idRoom) + "R": [
                {"USERS": listUsers, "NAME": self.data_s[2]}]}})
            i += 1
        self.DB.update_one({'_id': 'COUNT'}, {'$set': {'ROOMS': self.idRoom}})

        self.DB.update_one({'_id': 'USERS'},
                           [{'$set': {f'{self.data_s[1]}.ROOMS': {str(self.idRoom) + "R": self.data_s[2]}}}])

        self.DB.update_one({'_id': 'USERS'},
                           [{'$set': {f'{self.data_s[2]}.ROOMS': {str(self.idRoom) + "R": self.data_s[1]}}}])
        self.DB.update_one({'_id': 'MESSAGE'}, {'$set': {str(self.idRoom) + 'R': []}})

        print("ROOM IS CREATE")

        self.create_room()
        self.create_room_now()

    def create_room_now(self):
        name_of_rooms = self.DB.find_one({"_id": "ROOMS"},
                                         {"_id": 0}).keys()  # Создание комнаты, без необходимости перезагрузки сервера
        for name in name_of_rooms:
            for usersInRoom in self.DB.find_one({"_id": "ROOMS"}, {"_id": 0})[name][0]["USERS"]:
                try:
                    if usersInRoom not in self.rooms[name][0]:  # Условие, что бы не дублировать в комнаты
                        self.rooms[name][0].update({usersInRoom: self.userAndObject[usersInRoom]})
                except Exception:
                    pass

        try:

            self.userAndObject[self.data_s[1]].send(
                pickle.dumps(["CRT_ROOM", {str(self.idRoom) + "R": self.data_s[2]}]))
            self.userAndObject[self.data_s[2]].send(
                pickle.dumps(["CRT_ROOM", {str(self.idRoom) + "R": self.data_s[1]}]))
            print(["CRT_ROOM", {str(self.idRoom) + "R": self.data_s[1]}])
        except KeyError:
            self.userAndObject[self.data_s[2]].send(
                pickle.dumps(["CRT_ROOM", {str(self.idRoom) + "R": self.data_s[1]}]))

    def create_room(self):
        name_of_rooms = self.DB.find_one({"_id": "ROOMS"}, {"_id": 0}).keys()

        for name in name_of_rooms:
            self.rooms[name] = [{}]
        print(self.rooms)

    def recreating_room_from_JSON(self):
        name_of_rooms = self.DB.find_one({"_id": "ROOMS"}, {"_id": 0}).keys()  # Воссоздание комнат из JSON
        for name in name_of_rooms:
            for usersInRoom in self.DB.find_one({"_id": "ROOMS"}, {"_id": 0})[name][0]["USERS"]:
                try:
                    if usersInRoom not in self.rooms[name][0]:  # Условие, что бы не дублировать в комнаты
                        self.rooms[name][0].update({usersInRoom: self.userAndObject[usersInRoom]})
                except KeyError:
                    pass

    def private_MSG(self):
        print("------------КОМНАТА-------------")
        for roomID, roomName in self.DB.find_one({"_id": "USERS"}, {"_id": 0})[self.data_s[2]]["ROOMS"].items():

            if roomName == self.data_s[3]:
                print(f"roomID, roomName --- >{roomID, roomName}")
                print(f"self.rooms[roomID][0] --- >{self.rooms[roomID][0]}")

                for userInRoom in self.rooms[roomID][0].values():
                    print(f"userInRoom --- >{userInRoom}")
                    userInRoom.send(pickle.dumps(["MSGROOM", self.data_s[2], self.data_s[-1], self.data_s[3]]))
                    print(f"FOR ROOM IN CL --- >{['MSGROOM', self.data_s[2], self.data_s[-1], self.data_s[3]]}")

        self.DB.update_one({"_id": "MESSAGE"}, {"$push": {self.data_s[1]: f"{self.data_s[2]}: {self.data_s[-1]}"}})

        print("------------КОНЕЦ КОМНАТЫ-------------")

    def load_MSG_for_client(self, user):
        try:
            if not self.DB.find_one({"_id": "MESSAGE"}, {"_id": 0})[self.data_s[1]]:
                for_load_MSG = pickle.dumps(["LOADMSG", "NOMSG"])
                self.logger_package_MSG.info(f"{['LOADMSG', 'NOMSG']}")
                user.send(for_load_MSG)

            else:
                self.logger_package_MSG.info(
                    f"{['LOADMSG', self.DB.find_one({'_id': 'MESSAGE'}, {'_id': 0})[self.data_s[1]]]}")
                for_load_MSG = pickle.dumps(
                    ["LOADMSG", self.DB.find_one({'_id': 'MESSAGE'}, {'_id': 0})[self.data_s[1]]])
                user.send(for_load_MSG)

        except KeyError as error:

            self.DB.find_one({"_id": "MESSAGE"}, {"_id": 0})[self.data_s[1]] = []

    def search_people(self):
        users_in_JSON = self.DB.find_one({'_id': 'USERS'}, {'_id': 0})
        user_of_search = []

        for user in users_in_JSON:
            if self.data_s[1] in user:
                user_of_search.append(user)

        user_of_search = ["SEARCH", pickle.dumps(user_of_search)]
        self.send_data(user_of_search)

    def start_server(self):

        while True:
            users_socket, address = self.accept()
            self.logger_accept.debug("USER ACCEPT")

            # if address[0] not in self.users_ip:
            """
            Checking that the user could not run many clients on one pc
            """
            self.users_ip.append(address[0])
            '''
            accept() - Ожидает нового пользователя, и пока новый пользователь не придет
            код дальше не пойдет
            '''
            print("Users accept!" + address[0])  # Вывод айпи нового ползователя
            self.users.append(users_socket)  # Добавление нового пользователя в список
            threading.Thread(target=self.listen_socket, args=(address[0], users_socket)).start()
            '''
            Старт потока для принятия сообщений, иначе из-за accept() код дальше не идет
            и функция для принятия сообщения стартует после входа нового пользователя
            '''


if __name__ == '__main__':  # Start
    server = Server()
    server.start_server()
