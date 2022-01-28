import json
import pickle
import socket
import threading


class Server(socket.socket):
    def __init__(self):  # Инициализация сервера
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        with open("DB.json", 'r') as json_file:
            self.DB = json.load(json_file)
            self.idUser = self.DB["COUNT"]["USERS"]
            self.idRoom = self.DB["COUNT"]["ROOMS"]
        self.bind(("192.168.0.3", 9090))
        self.listen()

        print("Server Listen")
        self.users = []  # List of all users
        self.users_ip = []  # List of all users-ip
        self.name_withIp = {"Gena": "89.179.112.93"}
        self.userAndObject = {}
        self.rooms = {}
        self.createRoom()

        # "Data base"

    def send_data(self, data):  # Send text to all users (in the list)
        try:

            for user in reversed(self.users):
                count_users = len(self.users)
                print(f"Кол-во польз.---> {count_users}")
                count_users = str(count_users).encode('utf-8')
                all_data = [count_users, data]
                user.send(pickle.dumps(all_data))
                print(f"ДАННЫЕ ОТ СЕРВЕРА ----> {all_data}")

        except Exception as a:
            print(f"_SEND_DATA ---> {a}")

    def listen_socket(self, ip_user, socket_user=None, ):  # Accept text from client

        print("Listen User")

        try:
            while True:
                self.data_s = socket_user.recv(2048)  # Accepting a message
                self.data_s = pickle.loads(self.data_s)
                print(f"ДАННЫЕ ОТ КЛИЕНТА --->{self.data_s}")
                if self.data_s[0] == "TRY_TO_ENTRY":  # If there is an ENTRY signal from the client, we start the process of checking the data from the user
                    self.userSignIn(self.data_s, socket_user)
                    self.name_withIp[self.data_s[1]] = self.users_ip[0]
                    self.RecreatingRoomFromJSON()
                elif self.data_s[0] == "TRY_TO_REG":
                    self.registration(self.data_s, socket_user)
                    self.userAndObject[self.data_s[1]] = socket_user
                elif self.data_s[0] == "MSGROOM":
                    self.PrivateMSG()
                elif self.data_s[0] == "SEARCH":
                    self.SearchPeople()
                elif self.data_s[0] == "CRT_ROOM":
                    self.createRoomJSON(socket_user)
                elif self.data_s[0] == "LOADMSG":
                    self.LoadMSGForClient(socket_user)






        except Exception as a:

            print("---------------------------------------------------------------")
            try:
                print(f"{self.data_s}", f"{a}")
                print(f"Ошибка --- >{a}")
                if self.data_s[0] == "USER_OUT":
                    """
                     Удаление пользователя из комнаты ЛС, так как при подключении пользователя меняеться его 'fd',
                     а в комнате все еще старый объект со старым 'fd'
                    
                    """
                    for roomID, roomName in self.DB["USERS"][self.data_s[1]]["ROOMS"][0].items():
                        print(f"USER '{self.data_s[1]}' IS OUT")
                        self.rooms[roomID][0].pop(self.data_s[1])
                        self.userAndObject.pop(self.data_s[1])
            except Exception:
                pass

            """

            If the client is disconnected, then we remove it from the user array and 
            the IP array
            users at the moment so. (While it works and thank God)
            """
            self.users.remove(socket_user)
            self.users_ip.remove(ip_user)

    def registration(self, data, user):
        self.idUser += 1
        if data[1] not in self.DB["USERS"]:
            self.DB["USERS"].update({data[1]: {"password": data[2],
                                               "ID": self.idUser,  # Пока нигде не используется
                                               "ROOMS": [{}]
                                               }})
            self.DB["COUNT"]["USERS"] = self.idUser
            with open("DB.json", 'w') as json_file:
                a = self.DB
                json.dump(a, json_file, indent=4)
            print(f"ПОЛЬЗОВАТЕЛЬ ЗАРЕГИСТРИРОВАН ")
            user.send(pickle.dumps(["USER_IS_REG"]))

        else:
            user.send(pickle.dumps(["HAVE_THIS_USER"]))
            print("HAVE_THIS_USER")

    def userSignIn(self, data,
                   socket_user):
        try:
            if self.DB["USERS"][data[1]]["password"] == data[2] and self.data_s[1] not in self.userAndObject.keys():

                keys = self.DB["USERS"][data[1]]["ROOMS"][0].keys()
                listRooms = []
                if not keys:
                    signIN = ["USER IS SIGN"]
                    self.userAndObject[self.data_s[1]] = socket_user
                else:

                    listRooms.append(self.DB["USERS"][data[1]]["ROOMS"][0])

                    signIN = ["USER IS SIGN", listRooms]
                    self.userAndObject[self.data_s[1]] = socket_user


                print("USER IS SIGN")
                self.userAndObject[self.data_s[1]] = socket_user
                socket_user.send(pickle.dumps(signIN))

            else:
                no_sign_in = ["USER_IS_NOT_SIGN"]
                print("USER_IS_NOT_SIGN (BAD_PASSWORD)")
                socket_user.send(pickle.dumps(no_sign_in))
        except KeyError:
            no_sign_in = ["USER_IS_NOT_SIGN"]
            print("USER_IS_NOT_SIGN (BAD_LOGIN)")
            socket_user.send(pickle.dumps(no_sign_in))

    def createRoomJSON(self, user):
        i = 1
        self.idRoom = self.idRoom + 1
        listUsers = []
        while i < len(self.data_s):
            listUsers.append(self.data_s[i])
            self.DB["ROOMS"][str(self.idRoom) + "R"] = [{"USERS": listUsers, "NAME": self.data_s[2]}]
            i += 1
        self.DB["COUNT"]["ROOMS"] = self.idRoom
        self.DB["USERS"][self.data_s[1]]["ROOMS"][0].update({str(self.idRoom) + "R": self.data_s[2]})
        self.DB["USERS"][self.data_s[2]]["ROOMS"][0].update({str(self.idRoom) + "R": self.data_s[1]})
        self.DB["MESSAGE"][str(self.idRoom) + "R"] = []

        print("ROOM IS CREATE")
        with open("DB.json", 'w') as json_file:
            a = self.DB
            json.dump(a, json_file, indent=4)

        self.createRoom()

        nameOfRooms = self.DB["ROOMS"].keys()  # Создание комнаты, без неоюходимости перезагрузки сервера
        for name in nameOfRooms:
            print(f"name {name}")
            for usersInRoom in self.DB["ROOMS"][name][0]["USERS"]:
                print(f"usersInRoom {usersInRoom}")
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

    def createRoom(self):
        nameOfRooms = self.DB["ROOMS"].keys()

        for name in nameOfRooms:
            self.rooms[name] = [{}]
        print(self.rooms)

    def RecreatingRoomFromJSON(self):
        nameOfRooms = self.DB["ROOMS"].keys()  # Воссоздание комнат из JSON
        for name in nameOfRooms:
            for usersInRoom in self.DB["ROOMS"][name][0]["USERS"]:
                try:
                    if usersInRoom not in self.rooms[name][0]:  # Условие, что бы не дублировать в комнаты
                        self.rooms[name][0].update({usersInRoom: self.userAndObject[usersInRoom]})
                except KeyError:
                    pass

    def PrivateMSG(self):
        print("------------КОМНАТА-------------")
        for roomID, roomName in self.DB["USERS"][self.data_s[2]]["ROOMS"][0].items():

            if roomName == self.data_s[3]:
                print(f"roomID, roomName --- >{roomID, roomName}")
                print(f"self.rooms[roomID][0] --- >{self.rooms[roomID][0]}")

                for userInRoom in self.rooms[roomID][0].values():
                    print(f"userInRoom --- >{userInRoom}")
                    userInRoom.send(pickle.dumps(["MSGROOM", self.data_s[2], self.data_s[-1]]))
                    print(f"FOR ROOM IN CL --- >{['MSGROOM', self.data_s[2], self.data_s[-1]]}")

        self.DB["MESSAGE"][self.data_s[1]].append(f"{self.data_s[2]}: {self.data_s[-1]}")
        with open("DB.json", 'w') as json_file:
            a = self.DB
            json.dump(a, json_file, indent=4)
        print("------------КОНЕЦ КОМНАТЫ-------------")

    def LoadMSGForClient(self, user):
        print(self.userAndObject)
        try:
            print(self.data_s)
            if not self.DB["MESSAGE"][self.data_s[1]]:
                forLoadMSG = pickle.dumps(["LOADMSG", "NOMSG"])
                print(f"forLoadMSG клиенту --- >{['LOADMSG', 'NOMSG']}")
                user.send(forLoadMSG)

            else:
                print(f"forLoadMSG клиенту --- >{['LOADMSG', self.DB['MESSAGE'][self.data_s[1]]]}")
                forLoadMSG = pickle.dumps(["LOADMSG", self.DB["MESSAGE"][self.data_s[1]]])
                user.send(forLoadMSG)

        except KeyError as error:

            self.DB["MESSAGE"][self.data_s[1]] = []

    def SearchPeople(self):
        usersInJSON = self.DB["USERS"]
        userOfSearch = []

        for user in usersInJSON:
            if self.data_s[1] in user:
                print("ЕСТЬ СОВПАДЕНИЕ")
                userOfSearch.append(user)

        userOfSearch = ["SEARCH", pickle.dumps(userOfSearch)]
        self.send_data(userOfSearch)
        userOfSearch = []
        print(f"userOfSearch --- >{userOfSearch}")

    def start_server(self):

        while True:
            users_socket, address = self.accept()
            print(f"users_socket --- >{users_socket}")

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
