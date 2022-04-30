import pickle
import socket
import threading
import logging
from init_data import Data

class Server(socket.socket):
    def __init__(self):
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

    def listen_socket(self, ip_user, socket_user,):  # Accept text from client

        try:
            while True:
                self.signal = socket_user.recv(2048)  # Accepting a message
                self.signal = pickle.loads(self.signal)
                print(f"ДАННЫЕ ОТ КЛИЕНТА --->{self.signal}")
                if self.signal[0] == "TRY_TO_ENTRY":
                    self.log_in(self.signal, socket_user)
                    print(f"self.name_withIp {self.data.name_withIp}")
                    print(f"self.users_ip[0] {self.data.users_ip}")
                    self.data.name_withIp[self.signal[1]] = self.data.users_ip[0]
                    self.recreating_room_from_JSON()
                elif self.signal[0] == "TRY_TO_REG":
                    self.registration(self.signal, socket_user)
                elif self.signal[0] == "MSGROOM":
                    self.private_MSG()
                elif self.signal[0] == "SEARCH":
                    print(socket_user)
                    self.search_people(socket_user)
                elif self.signal[0] == "CRT_ROOM":
                    self.create_room_JSON()
                elif self.signal[0] == "LOADMSG_ADD":
                    self.add_load_MSG_for_client(socket_user, self.signal[2])
                elif self.signal[0] == "LOADMSG":
                    self.load_MSG_for_client(socket_user)
                elif self.signal[0] == "USER_OUT":
                    """
                     Удаление пользователя из комнаты ЛС, так как при подключении пользователя меняеться его 'fd',
                     а в комнате все еще старый объект со старым 'fd'
                    
                    """
                    for roomID, roomName in self.data.DB.find_one({'_id': 'USERS'}, {'_id': 0})[self.signal[1]]["ROOMS"].items():
                        try:
                            self.data.rooms[roomID][0].pop(self.signal[1])
                            self.data.userAndObject.pop(self.signal[1])
                            self.data.users.remove(socket_user)
                        except:
                            pass
        except EOFError as error:
            print(error)
            pass

    def registration(self, data, user):
        self.data.idUser += 1
        if data[1] not in self.data.DB.find_one({'_id': 'USERS'}, {'_id': 0}):
            self.data.DB.update_one({"_id": "USERS"}, {"$set": {data[1]: {"password": data[2],
                                                                     "ID": self.data.idUser,  # Пока нигде не используется
                                                                     "ROOMS": {}
                                                                       }}})
            self.data.DB.find_one({'_id': 'COUNT'}, {'_id': 0})["USERS"] = self.data.idUser
            print(f"ПОЛЬЗОВАТЕЛЬ ЗАРЕГИСТРИРОВАН ")
            user.send(pickle.dumps(["USER_IS_REG"]))

        else:
            user.send(pickle.dumps(["HAVE_THIS_USER"]))
            print("HAVE_THIS_USER")

    def log_in(self, data,
               socket_user):
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
                                           {"_id": 0}).keys()  # Создание комнаты, без необходимости перезагрузки сервера
        for name in name_of_rooms:
            for usersInRoom in self.data.DB.find_one({"_id": "ROOMS"}, {"_id": 0})[name][0]["USERS"]:
                try:
                    if usersInRoom not in self.data.rooms[name][0]:  # Условие, что бы не дублировать в комнаты
                        self.data.rooms[name][0].update({usersInRoom: self.data.userAndObject[usersInRoom]})
                except Exception:
                    pass

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
                except KeyError:
                    pass

    def private_MSG(self):
        print("------------КОМНАТА-------------")
        for roomID, roomName in self.data.DB.find_one({"_id": "USERS"}, {"_id": 0})[self.signal[2]]["ROOMS"].items():

            if roomName == self.signal[3]:
                print(f"roomID, roomName --- >{roomID, roomName}")
                print(f"self.rooms[roomID][0] --- >{self.data.rooms[roomID][0]}")

                for userInRoom in self.data.rooms[roomID][0].values():
                    print(f"userInRoom --- >{userInRoom}")
                    userInRoom.send(pickle.dumps(["MSGROOM", self.signal[2], self.signal[-1], self.signal[3]]))
                    print(f"FOR ROOM IN CL --- >{['MSGROOM', self.signal[2], self.signal[-1], self.signal[3]]}")

        self.data.DB.update_one({"_id": "MESSAGE"}, {"$push": {self.signal[1]: f"{self.signal[2]}: {self.signal[-1]}"}})

        print("------------КОНЕЦ КОМНАТЫ-------------")

    def load_MSG_for_client(self, user, ):
        cut_bank_of_messg = []
        bank_of_mess = self.data.DB.find_one({"_id": "MESSAGE"}, {"_id": 0})[self.signal[1]]
        bank_of_mess.reverse()
        try:
            if not bank_of_mess:
                for_load_MSG = pickle.dumps(["LOADMSG", "NOMSG"])
                self.logger_package_MSG.info(f"{['LOADMSG', 'NOMSG']}")
                user.send(for_load_MSG)
            else:
                print(bank_of_mess)
                for i in bank_of_mess:
                    cut_bank_of_messg.append(i)
                    if len(cut_bank_of_messg) == 50:
                        break
                print(f"1l{cut_bank_of_messg}")
                for_load_MSG = pickle.dumps(
                    ["LOADMSG", cut_bank_of_messg])
                user.send(for_load_MSG)



        except KeyError as error:
            self.data.DB.find_one({"_id": "MESSAGE"}, {"_id": 0})[self.signal[1]] = []

    def add_load_MSG_for_client(self, user, index_of_start):
        print("dddddddddddddddddddd")
        print(f"index_of_start -- {index_of_start}")
        bank_of_mess = self.data.DB.find_one({"_id": "MESSAGE"}, {"_id": 0})[self.signal[1]]
        cut_bank_of_messg = []
        index_of_end = len(bank_of_mess) - index_of_start
        print(f"index_of_end -- {index_of_end}")
        for i in reversed(range(index_of_end)):
            cut_bank_of_messg.append(bank_of_mess[i])
            if len(cut_bank_of_messg) == 50:
                break
        print(f"cut_bank_of_messg -- {cut_bank_of_messg}")
        for_load_MSG = pickle.dumps(["LOADMSG_ADD", cut_bank_of_messg])
        user.send(for_load_MSG)



    def search_people(self, user_socket):
        users_in_JSON = self.data.DB.find_one({'_id': 'USERS'}, {'_id': 0})
        user_of_search = []

        for user in users_in_JSON:
            if self.signal[1] in user:
                user_of_search.append(user)

        user_of_search = pickle.dumps(["SEARCH", pickle.dumps(user_of_search)])
        print(user_of_search)
        print()
        user_socket.send(user_of_search)

    def start_server(self):

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
    server.start_server()
