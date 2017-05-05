import socket, sys, threading
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from pys import first

class MainWindow(QtWidgets.QDialog):
    def __init__(self, sock, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("uis/connect.ui",self)
        self.ui.show()
        self.sock = sock
    def ok(self):
        w = first.MainWindow(self.sock,self.ui.lineEdit.text(),int(self.ui.lineEdit_5.text()))
        self.ui.close()
