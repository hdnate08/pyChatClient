# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nateh\PycharmProjects\pyChatClient\pyChat_applicationScreen_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_applicationScreen_MainWindow(object):
    def setupUi(self, applicationScreen_MainWindow):
        applicationScreen_MainWindow.setObjectName("applicationScreen_MainWindow")
        applicationScreen_MainWindow.resize(733, 641)
        applicationScreen_MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #555555;\n"
"    color: #ffffff;\n"
"    border: 1px solid #888888;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(applicationScreen_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.applicationTitle_label = QtWidgets.QLabel(self.centralwidget)
        self.applicationTitle_label.setGeometry(QtCore.QRect(0, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.applicationTitle_label.setFont(font)
        self.applicationTitle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.applicationTitle_label.setObjectName("applicationTitle_label")
        self.chatLog_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.chatLog_textBrowser.setGeometry(QtCore.QRect(150, 30, 541, 421))
        self.chatLog_textBrowser.setObjectName("chatLog_textBrowser")
        self.inputChat_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.inputChat_textEdit.setGeometry(QtCore.QRect(150, 460, 541, 61))
        self.inputChat_textEdit.setObjectName("inputChat_textEdit")
        self.chatBox_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.chatBox_groupBox.setGeometry(QtCore.QRect(140, 10, 561, 561))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.chatBox_groupBox.setFont(font)
        self.chatBox_groupBox.setObjectName("chatBox_groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.chatBox_groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 520, 541, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sendMessage_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.sendMessage_pushButton.setObjectName("sendMessage_pushButton")
        self.horizontalLayout.addWidget(self.sendMessage_pushButton)
        self.clearMessage_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.clearMessage_pushButton.setObjectName("clearMessage_pushButton")
        self.horizontalLayout.addWidget(self.clearMessage_pushButton)
        self.clearMessage_pushButton.raise_()
        self.sendMessage_pushButton.raise_()
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 121, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.login_pushButton.setObjectName("login_pushButton")
        self.verticalLayout.addWidget(self.login_pushButton)
        self.register_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.register_pushButton.setObjectName("register_pushButton")
        self.verticalLayout.addWidget(self.register_pushButton)
        self.exit_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.exit_pushButton.setObjectName("exit_pushButton")
        self.verticalLayout.addWidget(self.exit_pushButton)
        self.chatBox_groupBox.raise_()
        self.layoutWidget.raise_()
        self.applicationTitle_label.raise_()
        self.inputChat_textEdit.raise_()
        self.chatLog_textBrowser.raise_()
        applicationScreen_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(applicationScreen_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 21))
        self.menubar.setObjectName("menubar")
        applicationScreen_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(applicationScreen_MainWindow)
        self.statusbar.setObjectName("statusbar")
        applicationScreen_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(applicationScreen_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(applicationScreen_MainWindow)

    def retranslateUi(self, applicationScreen_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        applicationScreen_MainWindow.setWindowTitle(_translate("applicationScreen_MainWindow", "MainWindow"))
        self.applicationTitle_label.setText(_translate("applicationScreen_MainWindow", "pyChat"))
        self.chatBox_groupBox.setTitle(_translate("applicationScreen_MainWindow", "Chat"))
        self.sendMessage_pushButton.setText(_translate("applicationScreen_MainWindow", "Send Message"))
        self.clearMessage_pushButton.setText(_translate("applicationScreen_MainWindow", "Clear Message"))
        self.login_pushButton.setText(_translate("applicationScreen_MainWindow", "Login"))
        self.register_pushButton.setText(_translate("applicationScreen_MainWindow", "Register"))
        self.exit_pushButton.setText(_translate("applicationScreen_MainWindow", "Exit"))