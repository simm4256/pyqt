from PyQt5 import QtWidgets
from PyQt5 import uic
import main

class First(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("uis/main.ui",self)
        self.ui.setTitle("채팅")
        self.ui.show()
        main.Vars.text = ""
        main.Vars.name = ""
    def nameChange(self):
        main.Vars.text = "User " + main.Vars.name + " change name to : " + self.ui.lineEdit.text()
        self.ui.textBrowser.append(main.Vars.text)
        main.Vars.name = self.ui.lineEdit.text()
    def textChange(self):
        main.Vars.text = main.Vars.name + " : " + self.ui.lineEdit_2.text()
        self.ui.textBrowser.append(main.Vars.text)
        self.ui.lineEdit_2.setText("")