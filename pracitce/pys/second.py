import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
import main

class Second(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("uis/second.ui",self)
        self.ui.show()
        self.ui.label.setText(str(main.Vars.n))