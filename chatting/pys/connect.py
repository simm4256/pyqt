import socket, sys, threading
from PyQt5 import QtWidgets, uic, QtGui
from pys import first

class MainWindow(QtWidgets.QDialog):
    def __init__(self, sock, parent=None):

        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("uis/connect.ui",self)
        self.ui.show()

        pos = QtGui.QCursor.pos()
        QtGui.QCursor.setPos(1,0)
        QtGui.QCursor.setPos(pos)

    def ok(self):
        print('')
