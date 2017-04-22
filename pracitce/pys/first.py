from PyQt5 import QtWidgets
from PyQt5 import uic
from . import second
import main

class First(QtWidgets.QDialog):
    global n
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("uis/main.ui",self)
        self.ui.show()
    def slot1(self):
        self.ui.label.setText("1")
        main.Vars.n=1
        #self.close()
        self.dialogTextBrowser = second.Second(self)
    def slot2(self):
        self.ui.label.setText("2")
        main.Vars.n=2
        #self.close()
        self.dialogTextBrowser = second.Second(self)
    def slot3(self):
        self.ui.label.setText("3")
        main.Vars.n=3
        #self.close()
        self.dialogTextBrowser = second.Second(self)