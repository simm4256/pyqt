import sys
from PyQt5 import QtWidgets, uic
from pys import first, second

class Vars:
	def __init__(self):
		self.n=0

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = first.First()
    sys.exit(app.exec_())