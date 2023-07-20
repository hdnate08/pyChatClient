"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChat_loginScreen_GUI import Ui_loginScreen_MainWindow
from pyChatClient import PyChatClient
import time


class pyChatClientBackend:
    def __init__(self):
        # Defaults setup
        self.current_datetime = time.ctime()
        self.pychat_client = PyChatClient('127.0.0.7', 60002)

        # Window setup
        self.app = QApplication([])
        self.window = QMainWindow()
        self.ui = Ui_loginScreen_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.currentDateTime_label.setText(self.current_datetime)

        # Default settings
        self.window.closeEvent = self.close_event

        # Connecting buttons to their respective functions
        self.ui.login_pushButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)
        self.ui.forgotPasswordButton.clicked.connect(self.passwordReset)
        self.ui.exitButton.clicked.connect(self.exit)

        # Connection setup
        self.pychat_client.connect()

    def login(self):
        print("Inside of login")

    def register(self):
        print("Inside of register")

    def passwordReset(self):
        print("Inside of passwordReset")

    def exit(self):
        print("Inside of exit")

    def close_event(self, event):
        self.pychat_client.close()
        event.accept()

    def run(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    client = pyChatClientBackend()
    client.run()
