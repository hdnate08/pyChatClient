# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nateh\PycharmProjects\pyChatClient\pyChat_loginScreen_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginScreen_MainWindow(object):
    def setupUi(self, loginScreen_MainWindow):
        loginScreen_MainWindow.setObjectName("loginScreen_MainWindow")
        loginScreen_MainWindow.resize(813, 666)
        loginScreen_MainWindow.setStyleSheet("#centralWidget {\n"
" background: rgba(32, 80, 96, 100);\n"
" }\n"
"\n"
"#topPanel { \n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0, y2:0, stop:0 rgba(91, 204, 233, 100), stop:1 rgba(32, 80, 96, 100));\n"
" }\n"
"\n"
"#loginForm\n"
"{\n"
" background: rgba(0, 0, 0, 80);\n"
" border-radius: 8px;\n"
"}\n"
"\n"
"QLabel { color: white; }\n"
"\n"
"QLineEdit { border-radius: 3px; }\n"
"\n"
"QPushButton\n"
"{\n"
"  color: white;\n"
"  background-color: #27a9e3;\n"
"  border-width: 0px;\n"
"  border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover { background-color: #66c011; }\n"
"\n"
"#centralWidget\n"
"{\n"
"  background: rgba(32, 80, 96, 100);\n"
"  border-image: url(:/images/resources/images/6204882.jpg);\n"
"}")
        self.centralWidget = QtWidgets.QWidget(loginScreen_MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topPanel = QtWidgets.QWidget(self.centralWidget)
        self.topPanel.setObjectName("topPanel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topPanel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currentDateTime_label = QtWidgets.QLabel(self.topPanel)
        self.currentDateTime_label.setObjectName("currentDateTime_label")
        self.horizontalLayout.addWidget(self.currentDateTime_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.topPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(55, 55))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/icons/rotate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.topPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(55, 55))
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/icons/power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.topPanel)
        self.spacer_3 = QtWidgets.QHBoxLayout()
        self.spacer_3.setContentsMargins(-1, 0, -1, -1)
        self.spacer_3.setObjectName("spacer_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacer_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.spacer_3)
        self.middlePanel = QtWidgets.QHBoxLayout()
        self.middlePanel.setContentsMargins(-1, 0, -1, 0)
        self.middlePanel.setObjectName("middlePanel")
        self.logo_label = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label.sizePolicy().hasHeightForWidth())
        self.logo_label.setSizePolicy(sizePolicy)
        self.logo_label.setMinimumSize(QtCore.QSize(150, 150))
        self.logo_label.setStyleSheet("border: 1px solid;\n"
"\n"
"  border-image: url(:/images/resources/images/pumpkin-pie.png);")
        self.logo_label.setText("")
        self.logo_label.setScaledContents(False)
        self.logo_label.setObjectName("logo_label")
        self.middlePanel.addWidget(self.logo_label)
        self.verticalLayout.addLayout(self.middlePanel)
        self.spacer_2 = QtWidgets.QHBoxLayout()
        self.spacer_2.setContentsMargins(-1, 0, -1, -1)
        self.spacer_2.setObjectName("spacer_2")
        spacerItem2 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.spacer_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.spacer_2)
        self.bottomPanel = QtWidgets.QHBoxLayout()
        self.bottomPanel.setContentsMargins(0, 0, -1, -1)
        self.bottomPanel.setObjectName("bottomPanel")
        self.loginForm = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginForm.sizePolicy().hasHeightForWidth())
        self.loginForm.setSizePolicy(sizePolicy)
        self.loginForm.setMinimumSize(QtCore.QSize(350, 200))
        self.loginForm.setStyleSheet("#loginForm_verticalWidget { border: 1px solid; }")
        self.loginForm.setObjectName("loginForm")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.loginForm)
        self.verticalLayout_2.setContentsMargins(35, 35, 35, 35)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.loginForm)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.username_lineEdit = QtWidgets.QLineEdit(self.loginForm)
        self.username_lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.horizontalLayout_6.addWidget(self.username_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.loginForm)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.loginForm)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_5.addWidget(self.password_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.login_pushButton = QtWidgets.QPushButton(self.loginForm)
        self.login_pushButton.setMinimumSize(QtCore.QSize(0, 25))
        self.login_pushButton.setObjectName("login_pushButton")
        self.verticalLayout_2.addWidget(self.login_pushButton)
        self.bottomPanel.addWidget(self.loginForm)
        self.verticalLayout.addLayout(self.bottomPanel)
        self.spacer = QtWidgets.QHBoxLayout()
        self.spacer.setContentsMargins(-1, 0, -1, -1)
        self.spacer.setObjectName("spacer")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.spacer.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.spacer)
        loginScreen_MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(loginScreen_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 21))
        self.menubar.setObjectName("menubar")
        loginScreen_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginScreen_MainWindow)
        self.statusbar.setObjectName("statusbar")
        loginScreen_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(loginScreen_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(loginScreen_MainWindow)

    def retranslateUi(self, loginScreen_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        loginScreen_MainWindow.setWindowTitle(_translate("loginScreen_MainWindow", "MainWindow"))
        self.currentDateTime_label.setText(_translate("loginScreen_MainWindow", "Tuesday, 7/18/2023 5:07 PM"))
        self.label.setText(_translate("loginScreen_MainWindow", "Username:"))
        self.label_2.setText(_translate("loginScreen_MainWindow", "Password:"))
        self.login_pushButton.setText(_translate("loginScreen_MainWindow", "Login"))
import resources_rc
