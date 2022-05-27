from configparser import ConfigParser
from pymongo import MongoClient


class Data:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.client = MongoClient(self.config["database"]["ip"], int(self.config["database"]["port"]))
        self.collect = self.client["Messanger"]
        self.DB = self.collect["msgr"]
        self.userAndObject = {}
        self.rooms = {}
        self.users = []  # List of all users
        self.users_ip = []  # List of all users-ip
        self.name_withIp = {}
        self.idUser = self.DB.find_one({"_id": "COUNT"})["USERS"]
        self.idRoom = self.DB.find_one({"_id": "COUNT"})["ROOMS"]
