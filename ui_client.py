from PyQt5 import QtCore, QtWidgets, QtGui

from ui_add_friend import Ui_AddFriend
from ui_users_login import Ui_LandP_Reg


class UI_ForMain(object):
    def setupUi(self, MainWindow, ChildWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.main_left = QtWidgets.QFrame(self.page)
        self.main_left.setMinimumSize(QtCore.QSize(200, 0))
        self.main_left.setMaximumSize(QtCore.QSize(335, 16777215))
        self.main_left.setStyleSheet("border:0px;\n"
                                     "background-color: rgb(50, 50, 50);")
        self.main_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_left.setObjectName("main_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_left)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upper_footer = QtWidgets.QFrame(self.main_left)
        self.upper_footer.setMinimumSize(QtCore.QSize(0, 47))
        self.upper_footer.setMaximumSize(QtCore.QSize(16777215, 48))
        self.upper_footer.setStyleSheet("border:0px;")
        self.upper_footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upper_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upper_footer.setMidLineWidth(0)
        self.upper_footer.setObjectName("upper_footer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.upper_footer)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_33 = QtWidgets.QFrame(self.upper_footer)
        self.frame_33.setMaximumSize(QtCore.QSize(41, 41))
        self.frame_33.setStyleSheet("border:0px;")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_settings = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_settings.setMaximumSize(QtCore.QSize(40, 29))
        self.pushButton_settings.setStyleSheet("\n"
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
        self.pushButton_settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/free-icon-menu-1828859.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_settings.setIcon(icon)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.verticalLayout_2.addWidget(self.pushButton_settings)
        self.horizontalLayout_2.addWidget(self.frame_33)
        self.frame_2 = QtWidgets.QFrame(self.upper_footer)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 47))
        self.frame_2.setStyleSheet("border:0px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_addFriend = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_addFriend.setMaximumSize(QtCore.QSize(274, 29))
        self.pushButton_addFriend.setStyleSheet("\n"
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
        self.pushButton_addFriend.setObjectName("pushButton_addFriend")
        self.verticalLayout_3.addWidget(self.pushButton_addFriend)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.upper_footer)
        self.people = QtWidgets.QFrame(self.main_left)
        self.people.setMaximumSize(QtCore.QSize(330, 9000))
        self.people.setStyleSheet("border:0px;")
        self.people.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.people.setFrameShadow(QtWidgets.QFrame.Raised)
        self.people.setObjectName("people")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.people)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listWidget_people = QtWidgets.QListWidget(self.people)
        self.listWidget_people.setAutoFillBackground(False)
        self.listWidget_people.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                             "font: 25 18pt \"Corbel Light\";\n"
                                             "color: rgb(158, 158, 158);\n"
                                             "border:0px;\n"
                                             "")
        self.listWidget_people.setObjectName("listWidget_people")
        self.horizontalLayout_3.addWidget(self.listWidget_people)
        self.verticalLayout.addWidget(self.people)
        self.horizontalLayout_4.addWidget(self.main_left)
        self.main_right = QtWidgets.QFrame(self.page)
        self.main_right.setMinimumSize(QtCore.QSize(400, 300))
        self.main_right.setMaximumSize(QtCore.QSize(90000, 16777215))
        self.main_right.setStyleSheet("border:0px;\n"
                                      "background-color: rgb(30, 30, 30);")
        self.main_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_right.setObjectName("main_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.main_right)
        self.frame_6.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_6.setMaximumSize(QtCore.QSize(9000, 50))
        self.frame_6.setStyleSheet("border:0px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_label = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_label.setFont(font)
        self.pushButton_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_label.setStyleSheet("border-bottom-color: rgb(50, 50, 50);\n"
                                            "border-style: outset;\n"
                                            "border-bottom-width: 2px;\n"
                                            "background-color: rgb(30, 30, 30);\n"
                                            "color: rgb(158, 158, 158);")
        self.pushButton_label.setObjectName("pushButton_label")
        self.verticalLayout_8.addWidget(self.pushButton_label)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.main_right)
        self.frame_4.setStyleSheet("border:0px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.listWidget_msgRoom = QtWidgets.QListWidget(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget_msgRoom.setFont(font)
        self.listWidget_msgRoom.setStyleSheet("background-color: rgb(30, 30, 30);\n"
                                              "color: rgb(158, 158, 158);\n"
                                              "border:0px;")
        self.listWidget_msgRoom.setProperty("isWrapping", False)
        self.listWidget_msgRoom.setObjectName("listWidget_msgRoom")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_msgRoom.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_msgRoom.addItem(item)
        self.verticalLayout_7.addWidget(self.listWidget_msgRoom)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.right_footer = QtWidgets.QFrame(self.main_right)
        self.right_footer.setMinimumSize(QtCore.QSize(0, 0))
        self.right_footer.setMaximumSize(QtCore.QSize(16777215, 100))
        self.right_footer.setStyleSheet("border:0px;")
        self.right_footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_footer.setObjectName("right_footer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.right_footer)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.right_footer)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_7.setStyleSheet("border:0px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEdit_room = QtWidgets.QTextEdit(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit_room.setFont(font)
        self.textEdit_room.setMouseTracking(False)
        self.textEdit_room.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_room.setStyleSheet("background-color: rgb(50, 50, 50);\n"
                                         "font: 14pt \"Cantarell\";\n"
                                         "color: rgb(158, 158, 158);\n"
                                         "border:0px;\n"
                                         "border-radius: 12px;\n"
                                         "")
        self.textEdit_room.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit_room.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_room.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit_room.setTabChangesFocus(True)
        self.textEdit_room.setOverwriteMode(False)
        self.textEdit_room.setPlaceholderText("Text")
        self.textEdit_room.setObjectName("textEdit_room")
        self.verticalLayout_5.addWidget(self.textEdit_room)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.right_footer)
        self.frame_5.setMaximumSize(QtCore.QSize(9000, 9000))
        self.frame_5.setStyleSheet("border:0px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_room = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_room.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_room.setFont(font)
        self.pushButton_room.setAutoFillBackground(False)
        self.pushButton_room.setStyleSheet("QPushButton{\n"
                                           "font: 11pt ;\n"
                                           "background-color: rgb(50, 50, 50);\n"
                                           "\n"
                                           "color: rgb(158, 158, 158);\n"
                                           "border:0px;\n"
                                           "border-radius: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgb(70, 70, 70);\n"
                                           "color: rgb(158, 158, 158);\n"
                                           "border-radius: 6px;\n"
                                           "}\n"
                                           "")
        self.pushButton_room.setObjectName("pushButton_room")
        self.verticalLayout_6.addWidget(self.pushButton_room)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.right_footer)
        self.horizontalLayout_4.addWidget(self.main_right)
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setMaximumSize(QtCore.QSize(0, 9000))
        self.frame.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.frame.setStyleSheet("border:0px;\n"
                                 "background-color: rgb(50, 50, 50);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setMaximumSize(QtCore.QSize(800, 50))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_card_fio = QtWidgets.QLabel(self.frame_9)
        self.label_card_fio.setMaximumSize(QtCore.QSize(16777215, 8000))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_card_fio.setFont(font)
        self.label_card_fio.setStyleSheet("color: rgb(158, 158, 158);\n"
                                          "font: 25 18pt \"Corbel Light\";")
        self.label_card_fio.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_card_fio.setObjectName("label_card_fio")
        self.verticalLayout_11.addWidget(self.label_card_fio)
        self.verticalLayout_9.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMaximumSize(QtCore.QSize(500, 135))
        self.frame_8.setStyleSheet("border:4px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_card_post = QtWidgets.QLabel(self.frame_8)
        self.label_card_post.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_card_post.setStyleSheet("color: rgb(158, 158, 158);\n"
                                           "font: 25 18pt \"Corbel Light\";")
        self.label_card_post.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_card_post.setObjectName("label_card_post")
        self.verticalLayout_10.addWidget(self.label_card_post)
        self.label_card_mail = QtWidgets.QLabel(self.frame_8)
        self.label_card_mail.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_card_mail.setStyleSheet("color: rgb(158, 158, 158);\n"
                                           "font: 25 18pt \"Corbel Light\";")
        self.label_card_mail.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_card_mail.setObjectName("label_card_mail")
        self.verticalLayout_10.addWidget(self.label_card_mail)
        self.label_card_phone = QtWidgets.QLabel(self.frame_8)
        self.label_card_phone.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_card_phone.setStyleSheet("color: rgb(158, 158, 158);\n"
                                            "font: 25 18pt \"Corbel Light\";")
        self.label_card_phone.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_card_phone.setObjectName("label_card_phone")
        self.verticalLayout_10.addWidget(self.label_card_phone)
        self.verticalLayout_9.addWidget(self.frame_8)
        self.card = QtWidgets.QFrame(self.frame)
        self.card.setMinimumSize(QtCore.QSize(900, 500))
        self.card.setMaximumSize(QtCore.QSize(0, 90000))
        self.card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card.setObjectName("card")
        self.verticalLayout_9.addWidget(self.card)
        self.horizontalLayout_4.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.page_2.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_11 = QtWidgets.QFrame(self.page_2)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_11.setStyleSheet("border:0px;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_18 = QtWidgets.QFrame(self.frame_11)
        self.frame_18.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_back_tomain = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_back_tomain.setMaximumSize(QtCore.QSize(29, 40))
        self.pushButton_back_tomain.setStyleSheet("\n"
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
        self.pushButton_back_tomain.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/free-icon-back-130882.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back_tomain.setIcon(icon1)
        self.pushButton_back_tomain.setObjectName("pushButton_back_tomain")
        self.horizontalLayout_8.addWidget(self.pushButton_back_tomain)
        self.horizontalLayout_6.addWidget(self.frame_18)
        self.frame_17 = QtWidgets.QFrame(self.frame_11)
        self.frame_17.setMaximumSize(QtCore.QSize(9000, 100))
        self.frame_17.setStyleSheet("border:0px;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_6.addWidget(self.frame_17)
        self.verticalLayout_12.addWidget(self.frame_11)
        self.frame_10 = QtWidgets.QFrame(self.page_2)
        self.frame_10.setStyleSheet("border:0px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setMinimumSize(QtCore.QSize(500, 100))
        self.frame_12.setMaximumSize(QtCore.QSize(9000, 149))
        self.frame_12.setStyleSheet("border:0px;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_13.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(self.frame_10)
        self.frame_14.setStyleSheet("border:0px;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_15.setMaximumSize(QtCore.QSize(99999, 500))
        self.frame_15.setStyleSheet("border:0px;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_quit = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_quit.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_quit.setStyleSheet("\n"
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
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout_7.addWidget(self.pushButton_quit)
        self.verticalLayout_14.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setStyleSheet("border:0px;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_of_creator = QtWidgets.QLabel(self.frame_16)
        self.label_of_creator.setMaximumSize(QtCore.QSize(999999, 100))
        self.label_of_creator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_of_creator.setObjectName("label_of_creator")
        self.verticalLayout_16.addWidget(self.label_of_creator)
        self.verticalLayout_14.addWidget(self.frame_16)
        self.verticalLayout_13.addWidget(self.frame_14)
        self.frame_13 = QtWidgets.QFrame(self.frame_10)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_13.setMaximumSize(QtCore.QSize(9000, 9000))
        self.frame_13.setStyleSheet("border:0px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_13.addWidget(self.frame_13)
        self.verticalLayout_12.addWidget(self.frame_10)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_room.hide()
        self.listWidget_msgRoom.raise_()
        self.listWidget_people.raise_()
        self.pushButton_addFriend.raise_()
        self.textEdit_room.raise_()
        self.pushButton_room.raise_()
        self.pushButton_label.raise_()
        self.frame.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.LP_RForm = Ui_LandP_Reg()
        self.LP_RForm.setupUi(ChildWindow)

        self.AddFRNDWindow = QtWidgets.QMainWindow()
        self.AddFRNDForm = Ui_AddFriend()
        self.AddFRNDForm.setupUi(self.AddFRNDWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # НИЖЕ КНОПКИ ОКНА ВХОДА
        self.LP_RForm.pushButton.clicked.connect(self.Sign_in)
        # self.RegForm.pushButton_settings.clicked.connect(self.Reg_in)

        # НИЖЕ КНОПКИ ДОБАВЛЕНИЯ В ДРУЗЬЯ

        self.AddFRNDForm.pushButton_2.clicked.connect(self.searchPeople)
        self.AddFRNDForm.pushButton.clicked.connect(self.addNewFriend)

        # НИЖЕ КНОПКА ОТПРАВКИ СООБЩЕНИЯ

        self.listWidget_msgRoom.verticalScrollBar().valueChanged.connect(self.adding_load)

        self.pushButton_settings.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_quit.clicked.connect(self.quit)
        self.pushButton_back_tomain.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_room.clicked.connect(self.roomMessage)
        self.pushButton_addFriend.clicked.connect(lambda: self.AddFRNDWindow.show())
        self.pushButton_label.clicked.connect(self.show_card_of_user)
        self.pushButton_label.clicked.connect(self.load_info_card)

        self.listWidget_people.clicked.connect(self.loadMSG)
        self.pushButton_addFriend.hide()
        self.pushButton_settings.hide()

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The_CorpMess_v1.5.0"))
        __sortingEnabled = self.listWidget_people.isSortingEnabled()
        self.listWidget_people.setSortingEnabled(False)
        self.listWidget_people.setSortingEnabled(__sortingEnabled)
        self.pushButton_label.setText(_translate("MainWindow", ""))
        self.pushButton_addFriend.setText(_translate("MainWindow", "Найти друзей"))
        self.textEdit_room.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Candara\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_room.setText(_translate("MainWindow", "Отправить"))
        self.label_card_fio.setText(_translate("MainWindow", "ФИО:"))
        self.label_card_post.setText(_translate("MainWindow", "Должность:"))
        self.label_card_phone.setText(_translate("MainWindow", "Кабинет:"))
        self.label_card_mail.setText(_translate("MainWindow", "Кабинет:"))
        self.pushButton_quit.setText(_translate("MainWindow", "Выйти"))
        self.label_of_creator.setText(
            _translate("MainWindow", "Unitum             |               Nikita Tarasov"))
