"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChatClientGUI import Ui_MainWindow
import socket


class pyChatClient:
    def __init__(self):
        # Window setup
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        # Connect button signals to their respective functions
        self.ui.login_pushButton.clicked.connect(self.login)
        self.ui.register_pushButton.clicked.connect(self.register)
        self.ui.exit_pushButton.clicked.connect(self.exit)
        self.ui.sendMessage_pushButton.clicked.connect(self.sendMessage)
        self.ui.clearMessage_pushButton.clicked.connect(self.clearMessage)

    def login(self):
        self.ui.chatLog_textBrowser.append('Inside of the login function')

    def register(self):
        self.ui.chatLog_textBrowser.append('Inside of the register function')

    def exit(self):
        self.ui.chatLog_textBrowser.append('Inside of the exit function')

    def sendMessage(self):
        self.ui.chatLog_textBrowser.append('Inside of the sendMessage function')

    def clearMessage(self):
        self.ui.chatLog_textBrowser.append('Inside of the clearMessage function')

    def run(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    client = pyChatClient()
    client.run()
