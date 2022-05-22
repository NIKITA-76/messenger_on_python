from PyQt5 import QtCore, QtWidgets


class Ui_Server(object):
    def setupUi(self, MainWindow, ):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 662)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 10, 1041, 641))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton_show_all_usr = QtWidgets.QPushButton(self.page)
        self.pushButton_show_all_usr.setGeometry(QtCore.QRect(407, 160, 221, 36))
        self.pushButton_show_all_usr.setObjectName("pushButton_show_all_usr")
        self.pushButton_crt_user = QtWidgets.QPushButton(self.page)
        self.pushButton_crt_user.setGeometry(QtCore.QRect(405, 200, 223, 36))
        self.pushButton_crt_user.setObjectName("pushButton_crt_user")
        self.stackedWidget.addWidget(self.page)
        self.page_usr = QtWidgets.QWidget()
        self.page_usr.setObjectName("page_usr")
        self.listWidget_people = QtWidgets.QListWidget(self.page_usr)
        self.listWidget_people.setGeometry(QtCore.QRect(10, 0, 1021, 351))
        self.listWidget_people.setStyleSheet("color: rgb(50, 50, 50);\n"
                                             "")
        self.listWidget_people.setObjectName("listWidget_people")
        self.pushButton_back_main_page_usr = QtWidgets.QPushButton(self.page_usr)
        self.pushButton_back_main_page_usr.setGeometry(QtCore.QRect(470, 360, 103, 36))
        self.pushButton_back_main_page_usr.setObjectName("pushButton_back_main_page_usr")
        self.stackedWidget.addWidget(self.page_usr)
        self.page_crt_usr = QtWidgets.QWidget()
        self.page_crt_usr.setObjectName("page_crt_usr")
        self.stackedWidget.addWidget(self.page_crt_usr)
        self.page_change_usr = QtWidgets.QWidget()
        self.page_change_usr.setObjectName("page_change_usr")
        self.stackedWidget_change = QtWidgets.QStackedWidget(self.page_change_usr)
        self.stackedWidget_change.setGeometry(QtCore.QRect(-10, 64, 1051, 590))
        self.stackedWidget_change.setObjectName("stackedWidget_change")
        self.page_crt_user = QtWidgets.QWidget()
        self.page_crt_user.setObjectName("page_crt_user")
        self.lineEdit_fio = QtWidgets.QLineEdit(self.page_crt_user)
        self.lineEdit_fio.setGeometry(QtCore.QRect(110, 70, 321, 36))
        self.lineEdit_fio.setStyleSheet("color: rgb(158, 158, 158);")
        self.lineEdit_fio.setObjectName("lineEdit_fio")
        self.lineEdit_login = QtWidgets.QLineEdit(self.page_crt_user)
        self.lineEdit_login.setGeometry(QtCore.QRect(700, 70, 321, 36))
        self.lineEdit_login.setStyleSheet("color: rgb(158, 158, 158);")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.label_passw = QtWidgets.QLabel(self.page_crt_user)
        self.label_passw.setGeometry(QtCore.QRect(610, 130, 66, 19))
        self.label_passw.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_passw.setAlignment(QtCore.Qt.AlignCenter)
        self.label_passw.setObjectName("label_passw")
        self.lineEdit_phone = QtWidgets.QLineEdit(self.page_crt_user)
        self.lineEdit_phone.setGeometry(QtCore.QRect(110, 170, 321, 36))
        self.lineEdit_phone.setStyleSheet("color: rgb(158, 158, 158);")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.label_phone = QtWidgets.QLabel(self.page_crt_user)
        self.label_phone.setGeometry(QtCore.QRect(18, 176, 66, 19))
        self.label_phone.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_phone.setAlignment(QtCore.Qt.AlignCenter)
        self.label_phone.setObjectName("label_phone")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.page_crt_user)
        self.lineEdit_pass.setGeometry(QtCore.QRect(700, 120, 321, 36))
        self.lineEdit_pass.setStyleSheet("color: rgb(158, 158, 158);")
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.label_crt_info = QtWidgets.QLabel(self.page_crt_user)
        self.label_crt_info.setGeometry(QtCore.QRect(370, 20, 321, 20))
        self.label_crt_info.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_crt_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_crt_info.setObjectName("label_crt_info")
        self.lineEdit_mail = QtWidgets.QLineEdit(self.page_crt_user)
        self.lineEdit_mail.setGeometry(QtCore.QRect(110, 220, 321, 36))
        self.lineEdit_mail.setStyleSheet("color: rgb(158, 158, 158);")
        self.lineEdit_mail.setObjectName("lineEdit_mail")
        self.lineEdit_post = QtWidgets.QLineEdit(self.page_crt_user)
        self.lineEdit_post.setGeometry(QtCore.QRect(110, 120, 321, 36))
        self.lineEdit_post.setStyleSheet("color: rgb(158, 158, 158);")
        self.lineEdit_post.setObjectName("lineEdit_post")
        self.label_passw_2 = QtWidgets.QLabel(self.page_crt_user)
        self.label_passw_2.setGeometry(QtCore.QRect(513, 180, 171, 19))
        self.label_passw_2.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_passw_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_passw_2.setObjectName("label_passw_2")
        self.label_post = QtWidgets.QLabel(self.page_crt_user)
        self.label_post.setGeometry(QtCore.QRect(10, 126, 91, 20))
        self.label_post.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_post.setAlignment(QtCore.Qt.AlignCenter)
        self.label_post.setObjectName("label_post")
        self.label_fio = QtWidgets.QLabel(self.page_crt_user)
        self.label_fio.setGeometry(QtCore.QRect(20, 80, 66, 19))
        self.label_fio.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_fio.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fio.setObjectName("label_fio")
        self.label_login = QtWidgets.QLabel(self.page_crt_user)
        self.label_login.setGeometry(QtCore.QRect(610, 80, 66, 19))
        self.label_login.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login.setObjectName("label_login")
        self.label_mail = QtWidgets.QLabel(self.page_crt_user)
        self.label_mail.setGeometry(QtCore.QRect(18, 226, 71, 19))
        self.label_mail.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_mail.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mail.setObjectName("label_mail")
        self.lineEdit_passw_2 = QtWidgets.QLineEdit(self.page_crt_user)
        self.lineEdit_passw_2.setGeometry(QtCore.QRect(700, 175, 321, 36))
        self.lineEdit_passw_2.setStyleSheet("color: rgb(158, 158, 158);")
        self.lineEdit_passw_2.setObjectName("lineEdit_passw_2")
        self.pushButton_crt_cancel = QtWidgets.QPushButton(self.page_crt_user)
        self.pushButton_crt_cancel.setGeometry(QtCore.QRect(630, 360, 191, 36))
        self.pushButton_crt_cancel.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_crt_cancel.setObjectName("pushButton_crt_cancel")
        self.pushButton_save = QtWidgets.QPushButton(self.page_crt_user)
        self.pushButton_save.setGeometry(QtCore.QRect(230, 360, 191, 36))
        self.pushButton_save.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.stackedWidget_change.addWidget(self.page_crt_user)
        self.page_change_user = QtWidgets.QWidget()
        self.page_change_user.setObjectName("page_change_user")
        self.comboBox = QtWidgets.QComboBox(self.page_change_user)
        self.comboBox.setGeometry(QtCore.QRect(408, 170, 194, 37))
        self.comboBox.setStyleSheet("color: rgb(158, 158, 158);")
        self.comboBox.setObjectName("comboBox")
        self.label_ch_info = QtWidgets.QLabel(self.page_change_user)
        self.label_ch_info.setGeometry(QtCore.QRect(340, 30, 341, 20))
        self.label_ch_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch_info.setObjectName("label_ch_info")
        self.label_ch_whtCh = QtWidgets.QLabel(self.page_change_user)
        self.label_ch_whtCh.setGeometry(QtCore.QRect(380, 140, 261, 19))
        self.label_ch_whtCh.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_ch_whtCh.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch_whtCh.setObjectName("label_ch_whtCh")
        self.label_ch_srch_user = QtWidgets.QLabel(self.page_change_user)
        self.label_ch_srch_user.setGeometry(QtCore.QRect(10, 70, 261, 19))
        self.label_ch_srch_user.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_ch_srch_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch_srch_user.setObjectName("label_ch_srch_user")
        self.listWidget_users = QtWidgets.QListWidget(self.page_change_user)
        self.listWidget_users.setGeometry(QtCore.QRect(10, 199, 256, 231))
        self.listWidget_users.setStyleSheet("color: rgb(158, 158, 158);")
        self.listWidget_users.setObjectName("listWidget_users")
        self.lineEdit_ch = QtWidgets.QLineEdit(self.page_change_user)
        self.lineEdit_ch.setGeometry(QtCore.QRect(10, 100, 256, 36))
        self.lineEdit_ch.setStyleSheet("color: rgb(158, 158, 158);")
        self.lineEdit_ch.setObjectName("lineEdit_ch")
        self.pushButton_ch_search = QtWidgets.QPushButton(self.page_change_user)
        self.pushButton_ch_search.setGeometry(QtCore.QRect(84, 140, 103, 36))
        self.pushButton_ch_search.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_ch_search.setObjectName("pushButton_ch_search")
        self.plainTextEdit_ch_data = QtWidgets.QPlainTextEdit(self.page_change_user)
        self.plainTextEdit_ch_data.setGeometry(QtCore.QRect(770, 150, 191, 111))
        self.plainTextEdit_ch_data.setStyleSheet("color: rgb(158, 158, 158);")
        self.plainTextEdit_ch_data.setObjectName("plainTextEdit_ch_data")
        self.pushButton_ch_save = QtWidgets.QPushButton(self.page_change_user)
        self.pushButton_ch_save.setGeometry(QtCore.QRect(200, 480, 190, 36))
        self.pushButton_ch_save.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_ch_save.setObjectName("pushButton_ch_save")
        self.pushButton_ch_cancel = QtWidgets.QPushButton(self.page_change_user)
        self.pushButton_ch_cancel.setGeometry(QtCore.QRect(610, 480, 190, 36))
        self.pushButton_ch_cancel.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_ch_cancel.setObjectName("pushButton_ch_cancel")
        self.label_ch_inf = QtWidgets.QLabel(self.page_change_user)
        self.label_ch_inf.setGeometry(QtCore.QRect(725, 110, 281, 20))
        self.label_ch_inf.setText("")
        self.label_ch_inf.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch_inf.setObjectName("label_ch_inf")
        self.stackedWidget_change.addWidget(self.page_change_user)
        self.page_delete_user = QtWidgets.QWidget()
        self.page_delete_user.setObjectName("page_delete_user")
        self.listWidget_del_users = QtWidgets.QListWidget(self.page_delete_user)
        self.listWidget_del_users.setGeometry(QtCore.QRect(380, 219, 256, 231))
        self.listWidget_del_users.setStyleSheet("color: rgb(158, 158, 158);")
        self.listWidget_del_users.setObjectName("listWidget_del_users")
        self.lineEdit_del_search = QtWidgets.QLineEdit(self.page_delete_user)
        self.lineEdit_del_search.setGeometry(QtCore.QRect(380, 120, 256, 36))
        self.lineEdit_del_search.setStyleSheet("color: rgb(158, 158, 158);")
        self.lineEdit_del_search.setObjectName("lineEdit_del_search")
        self.label_del_search = QtWidgets.QLabel(self.page_delete_user)
        self.label_del_search.setGeometry(QtCore.QRect(380, 90, 261, 19))
        self.label_del_search.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_del_search.setAlignment(QtCore.Qt.AlignCenter)
        self.label_del_search.setObjectName("label_del_search")
        self.pushButton_del_search = QtWidgets.QPushButton(self.page_delete_user)
        self.pushButton_del_search.setGeometry(QtCore.QRect(454, 160, 103, 36))
        self.pushButton_del_search.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_del_search.setObjectName("pushButton_del_search")
        self.label_del_info = QtWidgets.QLabel(self.page_delete_user)
        self.label_del_info.setGeometry(QtCore.QRect(350, 40, 321, 20))
        self.label_del_info.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_del_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_del_info.setObjectName("label_del_info")
        self.pushButton_del_cancel = QtWidgets.QPushButton(self.page_delete_user)
        self.pushButton_del_cancel.setGeometry(QtCore.QRect(610, 500, 191, 36))
        self.pushButton_del_cancel.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_del_cancel.setObjectName("pushButton_del_cancel")
        self.pushButton_del_save = QtWidgets.QPushButton(self.page_delete_user)
        self.pushButton_del_save.setGeometry(QtCore.QRect(210, 500, 191, 36))
        self.pushButton_del_save.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_del_save.setObjectName("pushButton_del_save")
        self.stackedWidget_change.addWidget(self.page_delete_user)
        self.pushButton_crt_user_2 = QtWidgets.QPushButton(self.page_change_usr)
        self.pushButton_crt_user_2.setGeometry(QtCore.QRect(20, 20, 231, 36))
        self.pushButton_crt_user_2.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_crt_user_2.setObjectName("pushButton_crt_user_2")
        self.pushButton_delete_user = QtWidgets.QPushButton(self.page_change_usr)
        self.pushButton_delete_user.setGeometry(QtCore.QRect(740, 20, 201, 36))
        self.pushButton_delete_user.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_delete_user.setObjectName("pushButton_delete_user")
        self.pushButton_change_user = QtWidgets.QPushButton(self.page_change_usr)
        self.pushButton_change_user.setGeometry(QtCore.QRect(400, 20, 211, 36))
        self.pushButton_change_user.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_change_user.setObjectName("pushButton_change_user")
        self.stackedWidget.addWidget(self.page_change_usr)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_change.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_crt_user.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.pushButton_crt_user_2.clicked.connect(lambda: self.stackedWidget_change.setCurrentIndex(0))
        self.pushButton_change_user.clicked.connect(lambda: self.stackedWidget_change.setCurrentIndex(1))
        self.pushButton_delete_user.clicked.connect(lambda: self.stackedWidget_change.setCurrentIndex(2))

        self.pushButton_save.clicked.connect(self.crt_new_user)
        self.pushButton_crt_cancel.clicked.connect(lambda: self.stackedWidget_change.setCurrentIndex(0))

        self.pushButton_ch_save.clicked.connect(self.change_user)
        self.pushButton_ch_search.clicked.connect(self.search_for_chenge)
        self.pushButton_ch_cancel.clicked.connect(lambda: self.stackedWidget_change.setCurrentIndex(0))


        #self.pushButton_del_save.clicked.connect(self.del_user)
        self.pushButton_del_cancel.clicked.connect(lambda: self.stackedWidget_change.setCurrentIndex(0))

        self.pushButton_show_all_usr.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_back_main_page_usr.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_show_all_usr.setText(_translate("MainWindow", "Просмотр всех пользователей"))
        self.pushButton_crt_user.setText(_translate("MainWindow", "Настройка  пользователей"))
        self.pushButton_back_main_page_usr.setText(_translate("MainWindow", "Назад"))
        self.label_passw.setText(_translate("MainWindow", "Пароль:"))
        self.label_phone.setText(_translate("MainWindow", "Телефон:"))
        self.label_crt_info.setText(_translate("MainWindow", "Создание пользователя"))
        self.label_passw_2.setText(_translate("MainWindow", "Подтвердите пароль:"))
        self.label_post.setText(_translate("MainWindow", "Должность:"))
        self.label_fio.setText(_translate("MainWindow", "ФИО:"))
        self.label_login.setText(_translate("MainWindow", "Логин:"))
        self.label_mail.setText(_translate("MainWindow", "Эл.почта:"))
        self.pushButton_crt_cancel.setText(_translate("MainWindow", "Отмена"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.label_ch_info.setStyleSheet(_translate("MainWindow", "color: rgb(158, 158, 158);"))
        self.label_ch_info.setText(_translate("MainWindow", "Изменение данных пользователя"))
        self.label_ch_whtCh.setText(_translate("MainWindow", "Выберите что нужно изменить"))
        self.label_ch_srch_user.setText(_translate("MainWindow", "Поиск пользователя"))
        self.pushButton_ch_search.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_ch_save.setText(_translate("MainWindow", "Сохранить "))
        self.pushButton_ch_cancel.setText(_translate("MainWindow", "Отмена"))
        self.label_del_search.setText(_translate("MainWindow", "Поиск пользователя"))
        self.pushButton_del_search.setText(_translate("MainWindow", "Поиск"))
        self.label_del_info.setText(_translate("MainWindow", "Удаление пользователя"))
        self.pushButton_del_cancel.setText(_translate("MainWindow", "Отмена"))
        self.pushButton_del_save.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_crt_user_2.setText(_translate("MainWindow", "Добавить нового пользователя"))
        self.pushButton_delete_user.setText(_translate("MainWindow", "Удалить сущ.пользователя"))
        self.pushButton_change_user.setText(_translate("MainWindow", "Изменить сущ.пользователя"))
