# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(517, 563)
        MainWindow.setMinimumSize(QtCore.QSize(517, 552))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 1251))
        MainWindow.setBaseSize(QtCore.QSize(521, 552))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(40, 10, 433, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 432, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.res16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res16.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res16.setFont(font)
        self.res16.setObjectName("res16")
        self.gridLayout.addWidget(self.res16, 15, 2, 1, 1)
        self.scroll8 = QtWidgets.QScrollBar(self.gridLayoutWidget)
        self.scroll8.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scroll8.setFont(font)
        self.scroll8.setMinimum(160)
        self.scroll8.setMaximum(250)
        self.scroll8.setSingleStep(1)
        self.scroll8.setPageStep(1)
        self.scroll8.setOrientation(QtCore.Qt.Horizontal)
        self.scroll8.setObjectName("scroll8")
        self.gridLayout.addWidget(self.scroll8, 7, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.scroll12 = QtWidgets.QScrollBar(self.gridLayoutWidget)
        self.scroll12.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scroll12.setFont(font)
        self.scroll12.setMinimum(10)
        self.scroll12.setMaximum(100)
        self.scroll12.setOrientation(QtCore.Qt.Horizontal)
        self.scroll12.setObjectName("scroll12")
        self.gridLayout.addWidget(self.scroll12, 11, 1, 1, 1)
        self.res1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res1.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res1.setFont(font)
        self.res1.setObjectName("res1")
        self.gridLayout.addWidget(self.res1, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        self.res11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res11.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res11.setFont(font)
        self.res11.setObjectName("res11")
        self.gridLayout.addWidget(self.res11, 10, 2, 1, 1)
        self.res7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res7.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res7.setFont(font)
        self.res7.setObjectName("res7")
        self.gridLayout.addWidget(self.res7, 6, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.res3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res3.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res3.setFont(font)
        self.res3.setObjectName("res3")
        self.gridLayout.addWidget(self.res3, 2, 2, 1, 1)
        self.res9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res9.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res9.setFont(font)
        self.res9.setObjectName("res9")
        self.gridLayout.addWidget(self.res9, 8, 2, 1, 1)
        self.res13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res13.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res13.setFont(font)
        self.res13.setObjectName("res13")
        self.gridLayout.addWidget(self.res13, 12, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.res10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res10.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res10.setFont(font)
        self.res10.setObjectName("res10")
        self.gridLayout.addWidget(self.res10, 9, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 14, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.res12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res12.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res12.setFont(font)
        self.res12.setObjectName("res12")
        self.gridLayout.addWidget(self.res12, 11, 2, 1, 1)
        self.res6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res6.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res6.setFont(font)
        self.res6.setObjectName("res6")
        self.gridLayout.addWidget(self.res6, 5, 2, 1, 1)
        self.res8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res8.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res8.setFont(font)
        self.res8.setObjectName("res8")
        self.gridLayout.addWidget(self.res8, 7, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 13, 0, 1, 1)
        self.scroll10 = QtWidgets.QScrollBar(self.gridLayoutWidget)
        self.scroll10.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scroll10.setFont(font)
        self.scroll10.setMinimum(15)
        self.scroll10.setMaximum(50)
        self.scroll10.setPageStep(1)
        self.scroll10.setOrientation(QtCore.Qt.Horizontal)
        self.scroll10.setObjectName("scroll10")
        self.gridLayout.addWidget(self.scroll10, 9, 1, 1, 1)
        self.res5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res5.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res5.setFont(font)
        self.res5.setObjectName("res5")
        self.gridLayout.addWidget(self.res5, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.res14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res14.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res14.setFont(font)
        self.res14.setObjectName("res14")
        self.gridLayout.addWidget(self.res14, 13, 2, 1, 1)
        self.res4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res4.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res4.setFont(font)
        self.res4.setObjectName("res4")
        self.gridLayout.addWidget(self.res4, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.res2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res2.setFont(font)
        self.res2.setObjectName("res2")
        self.gridLayout.addWidget(self.res2, 1, 2, 1, 1)
        self.res15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res15.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res15.setFont(font)
        self.res15.setObjectName("res15")
        self.gridLayout.addWidget(self.res15, 14, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 15, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)
        self.input_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_1.setObjectName("input_1")
        self.gridLayout.addWidget(self.input_1, 0, 1, 1, 1)
        self.input_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_2.setObjectName("input_2")
        self.gridLayout.addWidget(self.input_2, 1, 1, 1, 1)
        self.input_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_3.setObjectName("input_3")
        self.gridLayout.addWidget(self.input_3, 2, 1, 1, 1)
        self.input_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_4.setObjectName("input_4")
        self.gridLayout.addWidget(self.input_4, 3, 1, 1, 1)
        self.input_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_5.setObjectName("input_5")
        self.gridLayout.addWidget(self.input_5, 4, 1, 1, 1)
        self.input_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_6.setObjectName("input_6")
        self.gridLayout.addWidget(self.input_6, 5, 1, 1, 1)
        self.input_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_7.setObjectName("input_7")
        self.gridLayout.addWidget(self.input_7, 6, 1, 1, 1)
        self.input_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_9.setObjectName("input_9")
        self.gridLayout.addWidget(self.input_9, 8, 1, 1, 1)
        self.input_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_11.setObjectName("input_11")
        self.gridLayout.addWidget(self.input_11, 10, 1, 1, 1)
        self.input_13 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_13.setObjectName("input_13")
        self.gridLayout.addWidget(self.input_13, 12, 1, 1, 1)
        self.input_14 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_14.setObjectName("input_14")
        self.gridLayout.addWidget(self.input_14, 13, 1, 1, 1)
        self.input_15 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_15.setObjectName("input_15")
        self.gridLayout.addWidget(self.input_15, 14, 1, 1, 1)
        self.input_16 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_16.setObjectName("input_16")
        self.gridLayout.addWidget(self.input_16, 15, 1, 1, 1)
        self.warning = QtWidgets.QLabel(MainWindow)
        self.warning.setGeometry(QtCore.QRect(40, 520, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.warning.setFont(font)
        self.warning.setText("")
        self.warning.setObjectName("warning")
        self.res1.setText('0.90')
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(480, 530, 21, 23))
        self.pushButton.setObjectName("pushButton")



        self.retranslateUi(MainWindow)
        # self.input_1.textChanged.connect(self.res1.setText)
        # отлавливаем изменения и вызываем функции
        self.scroll8.valueChanged['int'].connect(self.res8.setNum)
        self.scroll10.valueChanged['int'].connect(self.res10.setNum)
        self.scroll12.valueChanged['int'].connect(self.res12.setNum)

        # ячейка 2
        self.input_3.textChanged.connect(self.formula_2)
        self.scroll12.valueChanged['int'].connect(self.formula_2)
        self.scroll10.valueChanged['int'].connect(self.formula_2)
        self.scroll8.valueChanged['int'].connect(self.formula_2)
        # self.scroll8.valueChanged['int'].connect(self.formula_2)
        # ячейка 3
        self.scroll8.valueChanged['int'].connect(self.formula_3)
        self.scroll10.valueChanged['int'].connect(self.formula_3)
        # ячейка 4
        self.scroll8.valueChanged['int'].connect(self.formula_4)
        # ячейка 5
        self.input_3.textChanged.connect(self.formula_5)
        self.input_4.textChanged.connect(self.formula_5)

        # ячейка 6
        self.scroll12.valueChanged['int'].connect(self.formula_6)
        self.input_4.textChanged.connect(self.formula_6)
        self.input_1.textChanged.connect(self.formula_6)

        # ячейка 7
        self.input_1.textChanged.connect(self.formula_7)
        self.input_2.textChanged.connect(self.formula_7)
        self.input_5.textChanged.connect(self.formula_7)

        # ячейка 9
        self.scroll10.valueChanged['int'].connect(self.formula_9)
        self.input_11.textChanged.connect(self.formula_9)

        # ячейка 11
        self.scroll8.valueChanged['int'].connect(self.formula_11)
        self.scroll12.valueChanged['int'].connect(self.formula_11)
        # ячейка 13
        self.scroll12.valueChanged['int'].connect(self.formula_13)
        # ячейка 14
        self.scroll8.valueChanged['int'].connect(self.formula_14)
        self.scroll10.valueChanged['int'].connect(self.formula_14)
        self.input_11.textChanged.connect(self.formula_14)
        # ячейка 15
        self.input_6.textChanged.connect(self.formula_15)
        self.input_14.textChanged.connect(self.formula_15)
        # ячейка 16
        self.input_14.textChanged.connect(self.formula_16)
        # отслеживаем ячейку 14 массы для изм цвета
        self.input_14.textChanged.connect(self.change_color)

        # ручной ввод
        self.input_1.textChanged.connect(self.change_res1)
        self.input_2.textChanged.connect(self.res2.setText)
        self.input_3.textChanged.connect(self.res3.setText)
        self.input_4.textChanged.connect(self.res4.setText)
        self.input_5.textChanged.connect(self.res5.setText)
        self.input_6.textChanged.connect(self.res6.setText)
        self.input_7.textChanged.connect(self.res7.setText)
        self.input_9.textChanged.connect(self.res9.setText)
        self.input_11.textChanged.connect(self.res11.setText)
        self.input_13.textChanged.connect(self.res13.setText)
        self.input_14.textChanged.connect(self.change_14)
        self.input_15.textChanged.connect(self.res15.setText)
        self.input_16.textChanged.connect(self.res16.setText)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # вызов кнопки справка
        self.pushButton.clicked.connect(self.show_popup)

    def change_14(self):
        try:
            if self.input_14.text():
                # print(self.input_14.text())
                self.res14.setText(self.input_14.text())
            else:
                self.res14.setText(str('1'))
        except:
            self.res14.setText(str('1'))

    def change_res1(self):
        try:
            if float(self.input_1.text()) > 0:
                txt = str(self.input_1.text())
                self.res1.setText(str(txt))
            else:
                self.res1.setText(str('0.90'))
        except:
            self.res1.setText(str('0.90'))


    #  номинальный крутящий момент
    def formula_2(self):
        try:
            a = int(self.res3.text())
            b = int(self.scroll12.value())

        except:
            a = 608
            b = 10

        res = round(4700 * a / 2500 * b / 10)

        self.res2.setText(str(res))
        self.input_2.setText(str(res))

    #  рабочий объем
    def formula_3(self):
        try:
            a = int(self.scroll8.value())
            b = int(self.scroll10.value())

        except:
            a = 160
            b = 15
        res = round(2500 * (a / 250) ** 2 * b / 32)

        self.res3.setText(str(res))
        self.input_3.setText(str(res))

    # ном расход гидр жидкости
    def formula_4(self):
        try:
            a = int(self.scroll8.value())

        except:
            a = 160
        res = round(150 * a / 250)

        self.res4.setText(str(res))
        self.input_4.setText(str(res))

    # ном частота вращения
    def formula_5(self):
        try:
            a = float(self.res3.text())
            b = float(self.res4.text())
        except:
            a = 608
            b = 108
        res = round(b / a * 1000)
        self.res5.setText(str(res))
        self.input_5.setText(str(res))

    # ном гидр мощность
    def formula_6(self):
        try:
            a = float(self.res1.text())
            b = int(self.res4.text())
            c = int(self.scroll12.value())
        except:
            a = 0.90
            b = 108
            c = 10
        res = round(2.75 * b / 30 * c / 10 * a / 0.5)
        self.res6.setText(str(res))
        self.input_6.setText(str(res))

    # ном механическая мощность
    def formula_7(self):
        try:
            a = float(self.res1.text())
            b = int(self.res2.text())
            c = int(self.res5.text())
        except:
            a = 0.90
            b = 1140
            c = 177
        res = round(a * b * c * 2 * 3.14 / 60 / 1000)
        self.res7.setText(str(res))
        self.input_7.setText(str(res))

    # высота двигателя
    def formula_9(self):
        try:
            a = int(self.res11.text())
            b = int(self.res10.text())
        except:
            a = 8
            b = 15
        res = round(b + 2 * a)
        self.res9.setText(str(res))
        self.input_9.setText(str(res))

    # высота крышки
    def formula_11(self):
        try:
            a = int(self.res8.text())
            b = int(self.res12.text())
        except:
            a = 160
            b = 10
        res = round(33 * (a / 250) ** 4 * b / 10)
        self.res11.setText(str(res))
        self.input_11.setText(str(res))

    # макс давление
    def formula_13(self):
        try:
            txt = float(self.scroll12.value())

        except:
            txt = 10
        res = round(1.6 * txt)

        self.res13.setText(str(res))
        self.input_13.setText(str(res))

    # масса
    def formula_14(self):
        try:
            a = int(self.res8.text())
            b = int(self.res10.text())
            c = int(self.res11.text())
        except:
            a = 160
            b = 15
            c = 8
        res = round(a ** 2 * 0.785 * (b + 2 * c) * 7.8 / 1000000 * 31.1 / 37.5)
        self.res14.setText(str(res))
        self.input_14.setText(str(res))

    # удельная мощность
    def formula_15(self):
        try:
            a = int(self.res6.text())
            b = int(self.res14.text())
            # print(a, b)
            if b <= 0:
                b = 0.01
        except:
            a = 17
            b = 5
        res = round(a / b)
        self.res15.setText(str(res))
        self.input_15.setText(str(res))

    # удельная мощность
    def formula_16(self):
        try:
            a = int(self.res14.text())
        except:
            a = 5
        res = round(50000 / 31.1 * a)
        self.res16.setText(str(res))
        self.input_16.setText(str(res))

    def change_color(self):

        try:
            a = float(self.res14.text())
            if a < 7:
                self.warning.setText('Неверные параметры, измените показатели. ')
                self.warning.setStyleSheet("#warning {color: red;}")
                self.res14.setStyleSheet("#res14 {color: red;}")
            else:
                self.warning.setText(' ')
                self.warning.setStyleSheet("#res8 {color: black;}")
                self.res14.setStyleSheet("#res14 {color: black;}")

        except:
            print('pass')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Варианты гидравлических героторных двигателей"))
        MainWindow.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.label.setText(_translate("MainWindow", "Варианты гидравлических героторных двигателей"))
        self.label_11.setText(_translate("MainWindow", "Высота крышки, мм"))
        self.res16.setText(_translate("MainWindow", "1"))
        self.label_8.setText(_translate("MainWindow", "Диаметр двигателя, мм"))
        self.label_3.setText(_translate("MainWindow", "Рабочий объем, см3"))
        self.res1.setText(_translate("MainWindow", "0.90"))
        self.label_12.setText(_translate("MainWindow", "Ном. давление, МПа"))
        self.res11.setText(_translate("MainWindow", "1"))
        self.res7.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "Номинальный крутящий момент, Н/м"))
        self.label_4.setText(_translate("MainWindow", "Ном. расх. гидр. жидк., л/мин"))
        self.res3.setText(_translate("MainWindow", "1"))
        self.res9.setText(_translate("MainWindow", "1"))
        self.res13.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "Высота ротора, мм"))
        self.res10.setText(_translate("MainWindow", "1"))
        self.label_15.setText(_translate("MainWindow", "Удельная мощность, кВт/кг"))
        self.label_7.setText(_translate("MainWindow", "Ном. механическая мощность,кВт"))
        self.res12.setText(_translate("MainWindow", "20"))
        self.res6.setText(_translate("MainWindow", "1"))
        self.res8.setText(_translate("MainWindow", "160"))
        self.label_9.setText(_translate("MainWindow", "Высота двигателя, мм"))
        self.label_14.setText(_translate("MainWindow", "Масса, кг"))
        self.res5.setText(_translate("MainWindow", "1"))
        self.label_5.setText(_translate("MainWindow", "Ном. частота вращения, мин-1"))
        self.res14.setText(_translate("MainWindow", "1"))
        self.res4.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Ном. гидравлическая мощность,кВт"))
        self.label_1.setText(_translate("MainWindow", "КПД"))
        self.res2.setText(_translate("MainWindow", "1"))
        self.res15.setText(_translate("MainWindow", "1"))
        self.label_16.setText(_translate("MainWindow", "Ориентировочная стоимость, руб"))
        self.label_13.setText(_translate("MainWindow", "Макс. давление, МПа"))
        self.input_1.setText(_translate("MainWindow", "0.90"))
        self.pushButton.setText(_translate("MainWindow", "?"))


    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("О программе")
        msg.setText('Данная программа предназначена для оценки и подбора оптимальных характеристик, '
                    'при конструировании двигателей Hydrush.\nПоказатели, выделенные "красным" указывают, '
                    'что двигатель проблематично сконструировать - измените показатели.\n\n'
                    'Авторы:\n'
                    'Жадько Иван Сергеевич\n'
                    'Валеев Вильдан Майданович')
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()

if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
