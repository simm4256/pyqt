import socket, sys, threading
from PyQt5 import QtWidgets, uic
from pys import connect, first

name=""
text=""

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    app = QtWidgets.QApplication(sys.argv)
    w1 = connect.MainWindow(sock)
    sys.exit(app.exec_())
