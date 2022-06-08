from PyQt5 import QtCore, QtWidgets


class Ui_Server(object):
    def setupUi(self, MainWindow, ):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 712)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border:0px;background-color: rgb(50, 50, 50);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(9000, 9000))
        self.frame.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.page_3.setStyleSheet("")
        self.page_3.setObjectName("page_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.page_3)
        self.frame_2.setMaximumSize(QtCore.QSize(9000, 10000))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_show_all_usr = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_show_all_usr.sizePolicy().hasHeightForWidth())
        self.pushButton_show_all_usr.setSizePolicy(sizePolicy)
        self.pushButton_show_all_usr.setMinimumSize(QtCore.QSize(300, 35))
        self.pushButton_show_all_usr.setMaximumSize(QtCore.QSize(500, 35))
        self.pushButton_show_all_usr.setStyleSheet("\n"
                                                   "\n"
                                                   "QPushButton{\n"
                                                   "background-color: rgb(100, 100, 100);\n"
                                                   "\n"
                                                   "color: rgb(50, 50, 50);\n"
                                                   "border:0px;\n"
                                                   "border-radius: 6px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover{\n"
                                                   "background-color: rgb(130, 130, 130);\n"
                                                   "color: rgb(50, 50, 50);\n"
                                                   "border-radius: 6px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "")
        self.pushButton_show_all_usr.setObjectName("pushButton_show_all_usr")
        self.horizontalLayout_3.addWidget(self.pushButton_show_all_usr)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.page_3)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_crt_user = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_crt_user.setMinimumSize(QtCore.QSize(300, 35))
        self.pushButton_crt_user.setMaximumSize(QtCore.QSize(500, 35))
        self.pushButton_crt_user.setStyleSheet("\n"
                                               "\n"
                                               "QPushButton{\n"
                                               "background-color: rgb(100, 100, 100);\n"
                                               "\n"
                                               "color: rgb(50, 50, 50);\n"
                                               "border:0px;\n"
                                               "border-radius: 6px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "background-color: rgb(130, 130, 130);\n"
                                               "color: rgb(50, 50, 50);\n"
                                               "border-radius: 6px;\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "")
        self.pushButton_crt_user.setObjectName("pushButton_crt_user")
        self.horizontalLayout_2.addWidget(self.pushButton_crt_user)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_usr_3 = QtWidgets.QWidget()
        self.page_usr_3.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.page_usr_3.setObjectName("page_usr_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_usr_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.page_usr_3)
        self.frame_4.setMaximumSize(QtCore.QSize(90000, 1000))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 418))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.listWidget_people = QtWidgets.QListWidget(self.frame_5)
        self.listWidget_people.setMaximumSize(QtCore.QSize(90000, 400))
        self.listWidget_people.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                             "font: 14pt \"Cantarell\";\n"
                                             "color: rgb(158, 158, 158);\n"
                                             "border:0px;\n"
                                             "border-radius: 12px;\n"
                                             "")
        self.listWidget_people.setObjectName("listWidget_people")
        self.verticalLayout_5.addWidget(self.listWidget_people)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(100, 52))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_back_main_page_usr = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_back_main_page_usr.setMaximumSize(QtCore.QSize(500, 300))
        self.pushButton_back_main_page_usr.setStyleSheet("\n"
                                                         "\n"
                                                         "QPushButton{\n"
                                                         "background-color: rgb(100, 100, 100);\n"
                                                         "\n"
                                                         "color: rgb(50, 50, 50);\n"
                                                         "border:0px;\n"
                                                         "border-radius: 6px;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QPushButton:hover{\n"
                                                         "background-color: rgb(130, 130, 130);\n"
                                                         "color: rgb(50, 50, 50);\n"
                                                         "border-radius: 6px;\n"
                                                         "}\n"
                                                         "\n"
                                                         "\n"
                                                         "\n"
                                                         "")
        self.pushButton_back_main_page_usr.setObjectName("pushButton_back_main_page_usr")
        self.horizontalLayout_4.addWidget(self.pushButton_back_main_page_usr)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.page_usr_3)
        self.page_change_usr_3 = QtWidgets.QWidget()
        self.page_change_usr_3.setObjectName("page_change_usr_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_change_usr_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.page_change_usr_3)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 9000))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setMinimumSize(QtCore.QSize(800, 40))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_crt_user_2 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_crt_user_2.setMaximumSize(QtCore.QSize(16777215, 33))
        self.pushButton_crt_user_2.setStyleSheet("\n"
                                                 "\n"
                                                 "QPushButton{\n"
                                                 "background-color: rgb(100, 100, 100);\n"
                                                 "\n"
                                                 "color: rgb(50, 50, 50);\n"
                                                 "border:0px;\n"
                                                 "border-radius: 6px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover{\n"
                                                 "background-color: rgb(130, 130, 130);\n"
                                                 "color: rgb(50, 50, 50);\n"
                                                 "border-radius: 6px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.pushButton_crt_user_2.setObjectName("pushButton_crt_user_2")
        self.horizontalLayout_6.addWidget(self.pushButton_crt_user_2)
        self.pushButton_change_user = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_change_user.setMaximumSize(QtCore.QSize(16777215, 33))
        self.pushButton_change_user.setStyleSheet("\n"
                                                  "\n"
                                                  "QPushButton{\n"
                                                  "background-color: rgb(100, 100, 100);\n"
                                                  "\n"
                                                  "color: rgb(50, 50, 50);\n"
                                                  "border:0px;\n"
                                                  "border-radius: 6px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "background-color: rgb(130, 130, 130);\n"
                                                  "color: rgb(50, 50, 50);\n"
                                                  "border-radius: 6px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "")
        self.pushButton_change_user.setObjectName("pushButton_change_user")
        self.horizontalLayout_6.addWidget(self.pushButton_change_user)
        self.pushButton_delete_user = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_delete_user.setMaximumSize(QtCore.QSize(16777215, 33))
        self.pushButton_delete_user.setStyleSheet("\n"
                                                  "\n"
                                                  "QPushButton{\n"
                                                  "background-color: rgb(100, 100, 100);\n"
                                                  "\n"
                                                  "color: rgb(50, 50, 50);\n"
                                                  "border:0px;\n"
                                                  "border-radius: 6px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "background-color: rgb(130, 130, 130);\n"
                                                  "color: rgb(50, 50, 50);\n"
                                                  "border-radius: 6px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "\n"
                                                  "\n"
                                                  "")
        self.pushButton_delete_user.setObjectName("pushButton_delete_user")
        self.horizontalLayout_6.addWidget(self.pushButton_delete_user)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 9000))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget_change = QtWidgets.QStackedWidget(self.frame_9)
        self.stackedWidget_change.setObjectName("stackedWidget_change")
        self.page_crt_user_3 = QtWidgets.QWidget()
        self.page_crt_user_3.setObjectName("page_crt_user_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_crt_user_3)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_23 = QtWidgets.QFrame(self.page_crt_user_3)
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 58))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_crt_info = QtWidgets.QLabel(self.frame_23)
        self.label_crt_info.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_crt_info.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_crt_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_crt_info.setObjectName("label_crt_info")
        self.horizontalLayout_16.addWidget(self.label_crt_info)
        self.verticalLayout_12.addWidget(self.frame_23)
        self.frame_24 = QtWidgets.QFrame(self.page_crt_user_3)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.frame_13 = QtWidgets.QFrame(self.frame_24)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_32 = QtWidgets.QFrame(self.frame_14)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_fio = QtWidgets.QLabel(self.frame_32)
        self.label_fio.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_fio.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fio.setObjectName("label_fio")
        self.verticalLayout_23.addWidget(self.label_fio)
        self.horizontalLayout_8.addWidget(self.frame_32)
        self.frame_25 = QtWidgets.QFrame(self.frame_14)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_16.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lineEdit_fio = QtWidgets.QLineEdit(self.frame_25)
        self.lineEdit_fio.setMaximumSize(QtCore.QSize(90000, 16777215))
        self.lineEdit_fio.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                        "font: 14pt \"Cantarell\";\n"
                                        "color: rgb(158, 158, 158);\n"
                                        "border:0px;\n"
                                        "border-radius: 12px;\n"
                                        "")
        self.lineEdit_fio.setObjectName("lineEdit_fio")
        self.verticalLayout_16.addWidget(self.lineEdit_fio)
        self.horizontalLayout_8.addWidget(self.frame_25)
        self.verticalLayout_10.addWidget(self.frame_14)
        self.frame_16 = QtWidgets.QFrame(self.frame_13)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_33 = QtWidgets.QFrame(self.frame_16)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_post = QtWidgets.QLabel(self.frame_33)
        self.label_post.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_post.setAlignment(QtCore.Qt.AlignCenter)
        self.label_post.setObjectName("label_post")
        self.verticalLayout_22.addWidget(self.label_post)
        self.horizontalLayout_9.addWidget(self.frame_33)
        self.frame_26 = QtWidgets.QFrame(self.frame_16)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.lineEdit_post = QtWidgets.QLineEdit(self.frame_26)
        self.lineEdit_post.setMaximumSize(QtCore.QSize(90000, 16777215))
        self.lineEdit_post.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                         "font: 14pt \"Cantarell\";\n"
                                         "color: rgb(158, 158, 158);\n"
                                         "border:0px;\n"
                                         "border-radius: 12px;\n"
                                         "")
        self.lineEdit_post.setObjectName("lineEdit_post")
        self.verticalLayout_17.addWidget(self.lineEdit_post)
        self.horizontalLayout_9.addWidget(self.frame_26)
        self.verticalLayout_10.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_13)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_34 = QtWidgets.QFrame(self.frame_17)
        self.frame_34.setMaximumSize(QtCore.QSize(9000, 16777215))
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_phone = QtWidgets.QLabel(self.frame_34)
        self.label_phone.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_phone.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_phone.setAlignment(QtCore.Qt.AlignCenter)
        self.label_phone.setObjectName("label_phone")
        self.verticalLayout_20.addWidget(self.label_phone)
        self.horizontalLayout_10.addWidget(self.frame_34)
        self.frame_28 = QtWidgets.QFrame(self.frame_17)
        self.frame_28.setMaximumSize(QtCore.QSize(9000, 16777215))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_18.setContentsMargins(23, -1, -1, -1)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.lineEdit_phone = QtWidgets.QLineEdit(self.frame_28)
        self.lineEdit_phone.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                          "font: 14pt \"Cantarell\";\n"
                                          "color: rgb(158, 158, 158);\n"
                                          "border:0px;\n"
                                          "border-radius: 12px;\n"
                                          "")
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.verticalLayout_18.addWidget(self.lineEdit_phone)
        self.horizontalLayout_10.addWidget(self.frame_28)
        self.verticalLayout_10.addWidget(self.frame_17)
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_35 = QtWidgets.QFrame(self.frame_15)
        self.frame_35.setMinimumSize(QtCore.QSize(83, 0))
        self.frame_35.setMaximumSize(QtCore.QSize(75, 16777215))
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_mail = QtWidgets.QLabel(self.frame_35)
        self.label_mail.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_mail.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mail.setObjectName("label_mail")
        self.verticalLayout_21.addWidget(self.label_mail)
        self.horizontalLayout_11.addWidget(self.frame_35)
        self.frame_27 = QtWidgets.QFrame(self.frame_15)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_19.setContentsMargins(25, -1, -1, -1)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.lineEdit_mail = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_mail.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                         "font: 14pt \"Cantarell\";\n"
                                         "color: rgb(158, 158, 158);\n"
                                         "border:0px;\n"
                                         "border-radius: 12px;\n"
                                         "")
        self.lineEdit_mail.setObjectName("lineEdit_mail")
        self.verticalLayout_19.addWidget(self.lineEdit_mail)
        self.horizontalLayout_11.addWidget(self.frame_27)
        self.verticalLayout_10.addWidget(self.frame_15)
        self.horizontalLayout_17.addWidget(self.frame_13)
        self.frame_18 = QtWidgets.QFrame(self.frame_24)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_36 = QtWidgets.QFrame(self.frame_20)
        self.frame_36.setMaximumSize(QtCore.QSize(75, 16777215))
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_login = QtWidgets.QLabel(self.frame_36)
        self.label_login.setMaximumSize(QtCore.QSize(103, 16777215))
        self.label_login.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login.setObjectName("label_login")
        self.verticalLayout_24.addWidget(self.label_login)
        self.horizontalLayout_12.addWidget(self.frame_36)
        self.frame_29 = QtWidgets.QFrame(self.frame_20)
        self.frame_29.setMaximumSize(QtCore.QSize(9000, 16777215))
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lineEdit_login = QtWidgets.QLineEdit(self.frame_29)
        self.lineEdit_login.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                          "font: 14pt \"Cantarell\";\n"
                                          "color: rgb(158, 158, 158);\n"
                                          "border:0px;\n"
                                          "border-radius: 12px;\n"
                                          "")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.verticalLayout_15.addWidget(self.lineEdit_login)
        self.horizontalLayout_12.addWidget(self.frame_29)
        self.verticalLayout_11.addWidget(self.frame_20)
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_37 = QtWidgets.QFrame(self.frame_19)
        self.frame_37.setMaximumSize(QtCore.QSize(78, 16777215))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_passw = QtWidgets.QLabel(self.frame_37)
        self.label_passw.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_passw.setAlignment(QtCore.Qt.AlignCenter)
        self.label_passw.setObjectName("label_passw")
        self.verticalLayout_25.addWidget(self.label_passw)
        self.horizontalLayout_13.addWidget(self.frame_37)
        self.frame_30 = QtWidgets.QFrame(self.frame_19)
        self.frame_30.setMaximumSize(QtCore.QSize(9000, 16777215))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.frame_30)
        self.lineEdit_pass.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                         "font: 14pt \"Cantarell\";\n"
                                         "color: rgb(158, 158, 158);\n"
                                         "border:0px;\n"
                                         "border-radius: 12px;\n"
                                         "")
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.verticalLayout_13.addWidget(self.lineEdit_pass)
        self.horizontalLayout_13.addWidget(self.frame_30)
        self.verticalLayout_11.addWidget(self.frame_19)
        self.frame_21 = QtWidgets.QFrame(self.frame_18)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_38 = QtWidgets.QFrame(self.frame_21)
        self.frame_38.setMaximumSize(QtCore.QSize(160, 16777215))
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_passw_2 = QtWidgets.QLabel(self.frame_38)
        self.label_passw_2.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_passw_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_passw_2.setObjectName("label_passw_2")
        self.verticalLayout_26.addWidget(self.label_passw_2)
        self.horizontalLayout_14.addWidget(self.frame_38)
        self.frame_31 = QtWidgets.QFrame(self.frame_21)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.lineEdit_pass_2 = QtWidgets.QLineEdit(self.frame_31)
        self.lineEdit_pass_2.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                           "font: 14pt \"Cantarell\";\n"
                                           "color: rgb(158, 158, 158);\n"
                                           "border:0px;\n"
                                           "border-radius: 12px;\n"
                                           "")
        self.lineEdit_pass_2.setObjectName("lineEdit_pass_2")
        self.verticalLayout_14.addWidget(self.lineEdit_pass_2)
        self.horizontalLayout_14.addWidget(self.frame_31)
        self.verticalLayout_11.addWidget(self.frame_21)
        self.frame_39 = QtWidgets.QFrame(self.frame_18)
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.verticalLayout_11.addWidget(self.frame_39)
        self.horizontalLayout_17.addWidget(self.frame_18)
        self.verticalLayout_12.addWidget(self.frame_24)
        self.frame_22 = QtWidgets.QFrame(self.page_crt_user_3)
        self.frame_22.setMaximumSize(QtCore.QSize(16777215, 125))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_save = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_save.setMaximumSize(QtCore.QSize(300, 30))
        self.pushButton_save.setStyleSheet("\n"
                                           "\n"
                                           "QPushButton{\n"
                                           "background-color: rgb(100, 100, 100);\n"
                                           "\n"
                                           "color: rgb(50, 50, 50);\n"
                                           "border:0px;\n"
                                           "border-radius: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgb(130, 130, 130);\n"
                                           "color: rgb(50, 50, 50);\n"
                                           "border-radius: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "\n"
                                           "")
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_15.addWidget(self.pushButton_save)
        self.pushButton_crt_cancel = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_crt_cancel.setMaximumSize(QtCore.QSize(300, 35))
        self.pushButton_crt_cancel.setStyleSheet("\n"
                                                 "\n"
                                                 "QPushButton{\n"
                                                 "background-color: rgb(100, 100, 100);\n"
                                                 "\n"
                                                 "color: rgb(50, 50, 50);\n"
                                                 "border:0px;\n"
                                                 "border-radius: 6px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover{\n"
                                                 "background-color: rgb(130, 130, 130);\n"
                                                 "color: rgb(50, 50, 50);\n"
                                                 "border-radius: 6px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.pushButton_crt_cancel.setObjectName("pushButton_crt_cancel")
        self.horizontalLayout_15.addWidget(self.pushButton_crt_cancel)
        self.verticalLayout_12.addWidget(self.frame_22)
        self.stackedWidget_change.addWidget(self.page_crt_user_3)
        self.page_change_user_3 = QtWidgets.QWidget()
        self.page_change_user_3.setObjectName("page_change_user_3")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.page_change_user_3)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_ch_info = QtWidgets.QLabel(self.page_change_user_3)
        self.label_ch_info.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_ch_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch_info.setObjectName("label_ch_info")
        self.verticalLayout_30.addWidget(self.label_ch_info)
        self.frame_43 = QtWidgets.QFrame(self.page_change_user_3)
        self.frame_43.setMaximumSize(QtCore.QSize(9000, 9000))
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_12 = QtWidgets.QFrame(self.frame_43)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_40 = QtWidgets.QFrame(self.frame_12)
        self.frame_40.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_ch_srch_user = QtWidgets.QLabel(self.frame_40)
        self.label_ch_srch_user.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_ch_srch_user.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_ch_srch_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch_srch_user.setObjectName("label_ch_srch_user")
        self.verticalLayout.addWidget(self.label_ch_srch_user)
        self.lineEdit_ch = QtWidgets.QLineEdit(self.frame_40)
        self.lineEdit_ch.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_ch.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                       "font: 14pt \"Cantarell\";\n"
                                       "color: rgb(158, 158, 158);\n"
                                       "border:0px;\n"
                                       "border-radius: 12px;\n"
                                       "")
        self.lineEdit_ch.setObjectName("lineEdit_ch")
        self.verticalLayout.addWidget(self.lineEdit_ch)
        self.pushButton_ch_search = QtWidgets.QPushButton(self.frame_40)
        self.pushButton_ch_search.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_ch_search.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_ch_search.setStyleSheet("\n"
                                                "\n"
                                                "QPushButton{\n"
                                                "background-color: rgb(100, 100, 100);\n"
                                                "\n"
                                                "color: rgb(50, 50, 50);\n"
                                                "border:0px;\n"
                                                "border-radius: 6px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "background-color: rgb(130, 130, 130);\n"
                                                "color: rgb(50, 50, 50);\n"
                                                "border-radius: 6px;\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "")
        self.pushButton_ch_search.setObjectName("pushButton_ch_search")
        self.verticalLayout.addWidget(self.pushButton_ch_search)
        self.listWidget_users = QtWidgets.QListWidget(self.frame_40)
        self.listWidget_users.setMaximumSize(QtCore.QSize(300, 16777215))
        self.listWidget_users.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                            "font: 14pt \"Cantarell\";\n"
                                            "color: rgb(158, 158, 158);\n"
                                            "border:0px;\n"
                                            "border-radius: 12px;\n"
                                            "")
        self.listWidget_users.setObjectName("listWidget_users")
        self.verticalLayout.addWidget(self.listWidget_users)
        self.horizontalLayout_21.addWidget(self.frame_40)
        self.frame_41 = QtWidgets.QFrame(self.frame_12)
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_41)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_44 = QtWidgets.QFrame(self.frame_41)
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_44)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_50 = QtWidgets.QFrame(self.frame_44)
        self.frame_50.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_50.setMaximumSize(QtCore.QSize(60, 16777215))
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_50)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label = QtWidgets.QLabel(self.frame_50)
        self.label.setStyleSheet("color: rgb(158, 158, 158);")
        self.label.setObjectName("label")
        self.horizontalLayout_27.addWidget(self.label)
        self.horizontalLayout_22.addWidget(self.frame_50)
        self.textEdit_ch_fio = QtWidgets.QTextEdit(self.frame_44)
        self.textEdit_ch_fio.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                           "font: 14pt \"Cantarell\";\n"
                                           "color: rgb(158, 158, 158);\n"
                                           "border:0px;\n"
                                           "border-radius: 12px;\n"
                                           "")
        self.textEdit_ch_fio.setObjectName("textEdit_ch_fio")
        self.horizontalLayout_22.addWidget(self.textEdit_ch_fio)
        self.verticalLayout_27.addWidget(self.frame_44)
        self.frame_47 = QtWidgets.QFrame(self.frame_41)
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_47)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame_51 = QtWidgets.QFrame(self.frame_47)
        self.frame_51.setMaximumSize(QtCore.QSize(105, 16777215))
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_51)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_2 = QtWidgets.QLabel(self.frame_51)
        self.label_2.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_28.addWidget(self.label_2)
        self.horizontalLayout_23.addWidget(self.frame_51)
        self.frame_55 = QtWidgets.QFrame(self.frame_47)
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_55)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.textEdit_ch_post = QtWidgets.QTextEdit(self.frame_55)
        self.textEdit_ch_post.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                            "font: 14pt \"Cantarell\";\n"
                                            "color: rgb(158, 158, 158);\n"
                                            "border:0px;\n"
                                            "border-radius: 12px;\n"
                                            "")
        self.textEdit_ch_post.setObjectName("textEdit_ch_post")
        self.verticalLayout_29.addWidget(self.textEdit_ch_post)
        self.horizontalLayout_23.addWidget(self.frame_55)
        self.verticalLayout_27.addWidget(self.frame_47)
        self.frame_45 = QtWidgets.QFrame(self.frame_41)
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_45)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_52 = QtWidgets.QFrame(self.frame_45)
        self.frame_52.setMinimumSize(QtCore.QSize(95, 0))
        self.frame_52.setMaximumSize(QtCore.QSize(90, 16777215))
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_52)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_3 = QtWidgets.QLabel(self.frame_52)
        self.label_3.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_29.addWidget(self.label_3)
        self.horizontalLayout_24.addWidget(self.frame_52)
        self.frame_56 = QtWidgets.QFrame(self.frame_45)
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_56)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.textEdit_ch_phone = QtWidgets.QTextEdit(self.frame_56)
        self.textEdit_ch_phone.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                             "font: 14pt \"Cantarell\";\n"
                                             "color: rgb(158, 158, 158);\n"
                                             "border:0px;\n"
                                             "border-radius: 12px;\n"
                                             "")
        self.textEdit_ch_phone.setObjectName("textEdit_ch_phone")
        self.verticalLayout_31.addWidget(self.textEdit_ch_phone)
        self.horizontalLayout_24.addWidget(self.frame_56)
        self.verticalLayout_27.addWidget(self.frame_45)
        self.frame_46 = QtWidgets.QFrame(self.frame_41)
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_46)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.frame_53 = QtWidgets.QFrame(self.frame_46)
        self.frame_53.setMinimumSize(QtCore.QSize(94, 0))
        self.frame_53.setMaximumSize(QtCore.QSize(90, 16777215))
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_53)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_4 = QtWidgets.QLabel(self.frame_53)
        self.label_4.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_30.addWidget(self.label_4)
        self.horizontalLayout_25.addWidget(self.frame_53)
        self.frame_57 = QtWidgets.QFrame(self.frame_46)
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_57)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.textEdit_ch_mail = QtWidgets.QTextEdit(self.frame_57)
        self.textEdit_ch_mail.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                            "font: 14pt \"Cantarell\";\n"
                                            "color: rgb(158, 158, 158);\n"
                                            "border:0px;\n"
                                            "border-radius: 12px;\n"
                                            "")
        self.textEdit_ch_mail.setObjectName("textEdit_ch_mail")
        self.verticalLayout_32.addWidget(self.textEdit_ch_mail)
        self.horizontalLayout_25.addWidget(self.frame_57)
        self.verticalLayout_27.addWidget(self.frame_46)
        self.frame_48 = QtWidgets.QFrame(self.frame_41)
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_48)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.frame_54 = QtWidgets.QFrame(self.frame_48)
        self.frame_54.setMinimumSize(QtCore.QSize(94, 0))
        self.frame_54.setMaximumSize(QtCore.QSize(76, 16777215))
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_54)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_5 = QtWidgets.QLabel(self.frame_54)
        self.label_5.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_31.addWidget(self.label_5)
        self.horizontalLayout_26.addWidget(self.frame_54)
        self.frame_58 = QtWidgets.QFrame(self.frame_48)
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_58)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.textEdit_ch_pass = QtWidgets.QTextEdit(self.frame_58)
        self.textEdit_ch_pass.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                            "font: 14pt \"Cantarell\";\n"
                                            "color: rgb(158, 158, 158);\n"
                                            "border:0px;\n"
                                            "border-radius: 12px;\n"
                                            "")
        self.textEdit_ch_pass.setObjectName("textEdit_ch_pass")
        self.verticalLayout_33.addWidget(self.textEdit_ch_pass)
        self.horizontalLayout_26.addWidget(self.frame_58)
        self.verticalLayout_27.addWidget(self.frame_48)
        self.horizontalLayout_21.addWidget(self.frame_41)
        self.horizontalLayout_19.addWidget(self.frame_12)
        self.verticalLayout_30.addWidget(self.frame_43)
        self.frame_42 = QtWidgets.QFrame(self.page_change_user_3)
        self.frame_42.setMinimumSize(QtCore.QSize(0, 55))
        self.frame_42.setMaximumSize(QtCore.QSize(16777215, 55))
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_42)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pushButton_ch_save = QtWidgets.QPushButton(self.frame_42)
        self.pushButton_ch_save.setMaximumSize(QtCore.QSize(300, 40))
        self.pushButton_ch_save.setStyleSheet("\n"
                                              "\n"
                                              "QPushButton{\n"
                                              "background-color: rgb(100, 100, 100);\n"
                                              "\n"
                                              "color: rgb(50, 50, 50);\n"
                                              "border:0px;\n"
                                              "border-radius: 6px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgb(130, 130, 130);\n"
                                              "color: rgb(50, 50, 50);\n"
                                              "border-radius: 6px;\n"
                                              "}\n"
                                              "\n"
                                              "\n"
                                              "\n"
                                              "")
        self.pushButton_ch_save.setObjectName("pushButton_ch_save")
        self.horizontalLayout_18.addWidget(self.pushButton_ch_save)
        self.pushButton_ch_cancel = QtWidgets.QPushButton(self.frame_42)
        self.pushButton_ch_cancel.setMaximumSize(QtCore.QSize(300, 40))
        self.pushButton_ch_cancel.setStyleSheet("\n"
                                                "\n"
                                                "QPushButton{\n"
                                                "background-color: rgb(100, 100, 100);\n"
                                                "\n"
                                                "color: rgb(50, 50, 50);\n"
                                                "border:0px;\n"
                                                "border-radius: 6px;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "background-color: rgb(130, 130, 130);\n"
                                                "color: rgb(50, 50, 50);\n"
                                                "border-radius: 6px;\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "")
        self.pushButton_ch_cancel.setObjectName("pushButton_ch_cancel")
        self.horizontalLayout_18.addWidget(self.pushButton_ch_cancel)
        self.verticalLayout_30.addWidget(self.frame_42)
        self.stackedWidget_change.addWidget(self.page_change_user_3)
        self.page_delete_user_3 = QtWidgets.QWidget()
        self.page_delete_user_3.setObjectName("page_delete_user_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_delete_user_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_10 = QtWidgets.QFrame(self.page_delete_user_3)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 9000))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_del_info = QtWidgets.QLabel(self.frame_10)
        self.label_del_info.setMinimumSize(QtCore.QSize(0, 0))
        self.label_del_info.setMaximumSize(QtCore.QSize(16777215, 45))
        self.label_del_info.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_del_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_del_info.setObjectName("label_del_info")
        self.verticalLayout_8.addWidget(self.label_del_info)
        self.label_del_search = QtWidgets.QLabel(self.frame_10)
        self.label_del_search.setMinimumSize(QtCore.QSize(0, 40))
        self.label_del_search.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_del_search.setStyleSheet("color: rgb(158, 158, 158);")
        self.label_del_search.setAlignment(QtCore.Qt.AlignCenter)
        self.label_del_search.setObjectName("label_del_search")
        self.verticalLayout_8.addWidget(self.label_del_search)
        self.lineEdit_del_search = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_del_search.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                               "font: 14pt \"Cantarell\";\n"
                                               "color: rgb(158, 158, 158);\n"
                                               "border:0px;\n"
                                               "border-radius: 12px;\n"
                                               "")
        self.lineEdit_del_search.setObjectName("lineEdit_del_search")
        self.verticalLayout_8.addWidget(self.lineEdit_del_search)
        self.pushButton_del_search = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_del_search.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_del_search.setStyleSheet("color: rgb(158, 158, 158);")
        self.pushButton_del_search.setObjectName("pushButton_del_search")
        self.verticalLayout_8.addWidget(self.pushButton_del_search)
        self.listWidget_del_users = QtWidgets.QListWidget(self.frame_10)
        self.listWidget_del_users.setMaximumSize(QtCore.QSize(16777215, 9000))
        self.listWidget_del_users.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                                "font: 14pt \"Cantarell\";\n"
                                                "color: rgb(158, 158, 158);\n"
                                                "border:0px;\n"
                                                "border-radius: 12px;\n"
                                                "")
        self.listWidget_del_users.setObjectName("listWidget_del_users")
        self.verticalLayout_8.addWidget(self.listWidget_del_users)
        self.verticalLayout_9.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.page_delete_user_3)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_del_save = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_del_save.setMaximumSize(QtCore.QSize(300, 35))
        self.pushButton_del_save.setStyleSheet("\n"
                                               "\n"
                                               "QPushButton{\n"
                                               "background-color: rgb(100, 100, 100);\n"
                                               "\n"
                                               "color: rgb(50, 50, 50);\n"
                                               "border:0px;\n"
                                               "border-radius: 6px;\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover{\n"
                                               "background-color: rgb(130, 130, 130);\n"
                                               "color: rgb(50, 50, 50);\n"
                                               "border-radius: 6px;\n"
                                               "}\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "")
        self.pushButton_del_save.setObjectName("pushButton_del_save")
        self.horizontalLayout_7.addWidget(self.pushButton_del_save)
        self.pushButton_del_cancel = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_del_cancel.setMaximumSize(QtCore.QSize(300, 48))
        self.pushButton_del_cancel.setStyleSheet("\n"
                                                 "\n"
                                                 "QPushButton{\n"
                                                 "background-color: rgb(100, 100, 100);\n"
                                                 "\n"
                                                 "color: rgb(50, 50, 50);\n"
                                                 "border:0px;\n"
                                                 "border-radius: 6px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover{\n"
                                                 "background-color: rgb(130, 130, 130);\n"
                                                 "color: rgb(50, 50, 50);\n"
                                                 "border-radius: 6px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "\n"
                                                 "\n"
                                                 "")
        self.pushButton_del_cancel.setObjectName("pushButton_del_cancel")
        self.horizontalLayout_7.addWidget(self.pushButton_del_cancel)
        self.verticalLayout_9.addWidget(self.frame_11)
        self.stackedWidget_change.addWidget(self.page_delete_user_3)
        self.verticalLayout_7.addWidget(self.stackedWidget_change)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.stackedWidget.addWidget(self.page_change_usr_3)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_20.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_change.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_crt_user.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        self.pushButton_crt_user_2.clicked.connect(lambda: self.stackedWidget_change.setCurrentIndex(0))
        self.pushButton_change_user.clicked.connect(lambda: self.stackedWidget_change.setCurrentIndex(1))
        self.pushButton_delete_user.clicked.connect(lambda: self.stackedWidget_change.setCurrentIndex(2))

        self.pushButton_save.clicked.connect(self.crt_new_user)
        self.pushButton_crt_cancel.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.pushButton_ch_save.clicked.connect(self.change_user)
        self.pushButton_ch_search.clicked.connect(self.search_for_change)
        self.pushButton_ch_cancel.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.pushButton_del_cancel.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_del_save.clicked.connect(self.delete_user)
        self.pushButton_del_search.clicked.connect(self.search_for_delete)

        self.pushButton_show_all_usr.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The_CorpMess(Server)"))
        self.pushButton_show_all_usr.setText(_translate("MainWindow", "Просмотр всех пользователей"))
        self.pushButton_crt_user.setText(_translate("MainWindow", "Настройка  пользователей"))
        self.pushButton_crt_cancel.setText(_translate("MainWindow", "Назад"))
        self.label_passw.setText(_translate("MainWindow", "Пароль:"))
        self.label_phone.setText(_translate("MainWindow", "Телефон:"))
        self.label_crt_info.setText(_translate("MainWindow", "Создание пользователя"))
        self.label_passw_2.setText(_translate("MainWindow", "Подтвердите пароль:"))
        self.label_post.setText(_translate("MainWindow", "Должность:"))
        self.label_fio.setText(_translate("MainWindow", "ФИО:"))
        self.label_login.setText(_translate("MainWindow", "Логин:"))
        self.label_mail.setText(_translate("MainWindow", "Эл.почта:"))
        self.pushButton_save.setText(_translate("MainWindow", "Сохранить"))
        self.label_ch_info.setStyleSheet(_translate("MainWindow", "color: rgb(158, 158, 158);"))
        self.label_ch_info.setText(_translate("MainWindow", "Изменение данных пользователя"))
        self.label_ch_srch_user.setText(_translate("MainWindow", "Поиск пользователя"))
        self.label.setText(_translate("MainWindow", "ФИО:"))
        self.label_2.setText(_translate("MainWindow", "Должность:"))
        self.label_3.setText(_translate("MainWindow", "Телефон:"))
        self.label_4.setText(_translate("MainWindow", "Эл.почта:"))
        self.label_5.setText(_translate("MainWindow", "Пароль:"))
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
