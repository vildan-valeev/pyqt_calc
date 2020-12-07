import sys
from PyQt5 import QtWidgets
from test.design import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.lineEdit_2.textChanged.connect(self.changelabel)

    def changelabel(self):
        text = self.ui.lineEdit_2.text()
        res = int(text) * 2

        self.ui.label_2.setText(str(res))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
