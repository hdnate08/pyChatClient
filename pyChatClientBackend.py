"""
pyChat application using PyQt5
Nathan Harris
July 17, 2023
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from pyChatClientGUI import Ui_MainWindow
from pyChatClient import pyChatClient


# TODO: I think I want the pyChat client to automatically connect to the server and then
#   display a login/register/exit page. Upon successful login the client would be taken
#   to the actual application page

class pyChatClientBackend:
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

    def run(self):
        self.window.show()
        self.app.exec_()


if __name__ == '__main__':
    client = pyChatClientBackend()
    client.run()
