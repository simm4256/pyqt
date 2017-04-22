import sys
from PyQt5 import QtWidgets, uic
from pys import first

class Vars:
	def __init__(self):
		self.name=""
		self.text=""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = first.First()
    sys.exit(app.exec_())