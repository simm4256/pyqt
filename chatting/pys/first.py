import socket, sys, threading
from PyQt5 import QtWidgets, uic, QtGui

class MainWindow(QtWidgets.QDialog):
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
            print("잘못된 주소를 입력하셨습니다.")
            sys.exit(0)
        print("Socket created")

        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("uis/main.ui",self)
        self.ui.show()

        self.l = threading.Thread(target=self.listen, args=(sock,self.ui))
        self.l.start()

    def nameChange(self):
        self.text = "User " + self.name + " change name to : " + self.ui.lineEdit.text()
        self.ui.textBrowser.append(self.text)
        self.name = self.ui.lineEdit.text()
    def textChange(self):
        self.text = self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.setText("")
        self.sock.sendall(self.text.encode('utf8'))
    def fs_nameChanged(self,name, ui):
        ui.name=name
        ui.lineEdit.setText("user"+name)
    def fs_textUpdated(self,text, ui):
        ui.textBrowser.append(text)
        ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
    def listen(self, s, ui):
        while 1:
            read = s.recv(1024).decode('utf8')
            print(read[1:20])
            if read[1:20]=="!server create user":
                x=int(read[0])
                self.fs_textUpdated(read[20+x:], ui)
                self.fs_nameChanged(read[20:20+x], ui)
            else:
                self.fs_textUpdated(read, ui)
