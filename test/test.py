"""Perform action on <Enter> or click."""
import sys
from PyQt5.QtWidgets import (QApplication, QLCDNumber, QLineEdit, QPushButton,
                             QGridLayout, QWidget)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('<Enter> or click')
lcd = QLCDNumber(4)
button = QPushButton('Enter')
textfield = QLineEdit('123')
textfield.setFocus()

grid = QGridLayout()
grid.addWidget(lcd, 1, 1, 1, 2)  # first row, span two columns
grid.addWidget(textfield, 2, 1)  # 2nd row, 1st column
grid.addWidget(button, 2, 2)     # 2nd row, 2nd column
window.setLayout(grid)


def sync_lcd():
    lcd.display(textfield.text())


textfield.textChanged.connect(sync_lcd)
sync_lcd()

window.show()
sys.exit(app.exec())