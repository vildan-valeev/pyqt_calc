# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mycalc.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 200)
        MainWindow.setMinimumSize(QtCore.QSize(600, 200))
        MainWindow.setMaximumSize(QtCore.QSize(600, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtNum1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNum1.setGeometry(QtCore.QRect(10, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtNum1.setFont(font)
        self.txtNum1.setObjectName("txtNum1")
        self.txtNum2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNum2.setGeometry(QtCore.QRect(200, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txtNum2.setFont(font)
        self.txtNum2.setMaxLength(2)
        self.txtNum2.setObjectName("txtNum2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 40, 16, 41))
        self.label.setObjectName("label")
        self.lblSum = QtWidgets.QLabel(self.centralwidget)
        self.lblSum.setGeometry(QtCore.QRect(410, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblSum.setFont(font)
        self.lblSum.setText("")
        self.lblSum.setObjectName("lblSum")
        self.btnResult = QtWidgets.QPushButton(self.centralwidget)
        self.btnResult.setGeometry(QtCore.QRect(10, 110, 361, 61))
        self.btnResult.setObjectName("btnResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мой калькулятор для Систем счисления"))
        self.txtNum1.setToolTip(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:12pt;\">Введите число в системе счисления от </span><span style=\" font-size:12pt; font-weight:600;\">2</span><span style=\" font-size:12pt;\"> до </span><span style=\" font-size:12pt; font-weight:600;\">36</span><span style=\" font-size:12pt;\"> и результат будет в </span><span style=\" font-size:12pt; font-weight:600;\">10</span><span style=\" font-size:12pt;\">-ной сс.</span></p></body></html>"))
        self.txtNum2.setToolTip(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:12pt;\">Система счисления от </span><span style=\" font-size:12pt; font-weight:600;\">2</span><span style=\" font-size:12pt;\"> до </span><span style=\" font-size:12pt; font-weight:600;\">36</span><span style=\" font-size:12pt;\">!</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "="))
        self.btnResult.setText(_translate("MainWindow", "Выполнить"))
