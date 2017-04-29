import socket, sys, threading
from PyQt5 import QtWidgets, uic
import client

th=[]

class First(QtWidgets.QDialog):
    def __init__(self, sock, HOST, PORT, parent=None):
        self.text=""
        self.name=""
        self.sock=sock;
        print(self)
        global th

        try:
            sock.connect((HOST,PORT))
            print('='*50)
        except socket.error as msg:
            print("Failed to create socket.\nError code: %s\nError msg: %s"%(str(msg[0]),msg[1]))
            sys.exit(0)
        print("Socket created")

        self.l = threading.Thread(target=self.listen, args=(sock,))
        th.append(self.l)
        self.l.start()

        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("uis/main.ui",self)
        self.ui.show()
    def nameChange(self):
        print(self.ui)
        self.text = "User " + self.name + " change name to : " + self.ui.lineEdit.text()
        self.ui.textBrowser.append(self.text)
        self.name = self.ui.lineEdit.text()
    def textChange(self):
        print(self)
        print(self.ui)
        self.text = self.name + " : " + self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.setText("")
        self.sock.sendall(self.text.encode('utf8'))
    def fs_nameChanged(self,name):
        print(self)
        print(self.ui)
        self.name=name
        self.ui.lineEdit.setText(name)
    def fs_textUpdated(self,text):
        print(self)
        print(self.ui)
        self.ui.textBrowser.append(text)
    def listen(self, s):
        while 1:
            read = s.recv(1024).decode('utf8')
            print(read)
            if read[0:19]=="!server create user":
                self.fs_nameChanged(read)
            else:
                self.fs_textUpdated(read)
