import socket, sys, threading
from PyQt5 import QtWidgets, uic
from pys import first

HOST, PORT = '127.0.0.1', 3030
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name=""
text=""



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    w1 = first.First(sock, HOST, PORT)
    sys.exit(app.exec_())




'''
while True:
    data = input("text: ")

    if data == ':/quit' or not data:
        sock.close()
        break
    sock.sendall((data).encode('utf8'))
    '''
