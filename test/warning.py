# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(517, 563)
        MainWindow.setMinimumSize(QtCore.QSize(517, 552))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 1251))
        MainWindow.setBaseSize(QtCore.QSize(521, 552))
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
        self.input_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_2.sizePolicy().hasHeightForWidth())
        self.input_2.setSizePolicy(sizePolicy)
        self.input_2.setMinimumSize(QtCore.QSize(100, 20))
        self.input_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_2.setBaseSize(QtCore.QSize(0, 25))
        self.input_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_2.setObjectName("input_2")
        self.gridLayout.addWidget(self.input_2, 1, 1, 1, 1)
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
        self.scroll8.setMinimum(180)
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
        self.input_11 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_11.sizePolicy().hasHeightForWidth())
        self.input_11.setSizePolicy(sizePolicy)
        self.input_11.setMinimumSize(QtCore.QSize(100, 20))
        self.input_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_11.setBaseSize(QtCore.QSize(0, 25))
        self.input_11.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_11.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_11.setObjectName("input_11")
        self.gridLayout.addWidget(self.input_11, 10, 1, 1, 1)
        self.input_1 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.input_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_1.sizePolicy().hasHeightForWidth())
        self.input_1.setSizePolicy(sizePolicy)
        self.input_1.setMinimumSize(QtCore.QSize(100, 20))
        self.input_1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_1.setBaseSize(QtCore.QSize(0, 25))
        self.input_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_1.setObjectName("input_1")
        self.gridLayout.addWidget(self.input_1, 0, 1, 1, 1)
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
        self.input_14 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_14.sizePolicy().hasHeightForWidth())
        self.input_14.setSizePolicy(sizePolicy)
        self.input_14.setMinimumSize(QtCore.QSize(100, 20))
        self.input_14.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_14.setBaseSize(QtCore.QSize(0, 25))
        self.input_14.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_14.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_14.setObjectName("input_14")
        self.gridLayout.addWidget(self.input_14, 13, 1, 1, 1)
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
        self.input_4 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_4.sizePolicy().hasHeightForWidth())
        self.input_4.setSizePolicy(sizePolicy)
        self.input_4.setMinimumSize(QtCore.QSize(100, 20))
        self.input_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_4.setBaseSize(QtCore.QSize(0, 25))
        self.input_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_4.setObjectName("input_4")
        self.gridLayout.addWidget(self.input_4, 3, 1, 1, 1)
        self.res3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res3.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res3.setFont(font)
        self.res3.setObjectName("res3")
        self.gridLayout.addWidget(self.res3, 2, 2, 1, 1)
        self.input_9 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_9.sizePolicy().hasHeightForWidth())
        self.input_9.setSizePolicy(sizePolicy)
        self.input_9.setMinimumSize(QtCore.QSize(100, 20))
        self.input_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_9.setBaseSize(QtCore.QSize(0, 25))
        self.input_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_9.setObjectName("input_9")
        self.gridLayout.addWidget(self.input_9, 8, 1, 1, 1)
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
        self.input_3 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_3.sizePolicy().hasHeightForWidth())
        self.input_3.setSizePolicy(sizePolicy)
        self.input_3.setMinimumSize(QtCore.QSize(100, 20))
        self.input_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_3.setBaseSize(QtCore.QSize(0, 25))
        self.input_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_3.setObjectName("input_3")
        self.gridLayout.addWidget(self.input_3, 2, 1, 1, 1)
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
        self.input_13 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_13.sizePolicy().hasHeightForWidth())
        self.input_13.setSizePolicy(sizePolicy)
        self.input_13.setMinimumSize(QtCore.QSize(100, 20))
        self.input_13.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_13.setBaseSize(QtCore.QSize(0, 25))
        self.input_13.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_13.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_13.setObjectName("input_13")
        self.gridLayout.addWidget(self.input_13, 12, 1, 1, 1)
        self.input_16 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_16.sizePolicy().hasHeightForWidth())
        self.input_16.setSizePolicy(sizePolicy)
        self.input_16.setMinimumSize(QtCore.QSize(100, 20))
        self.input_16.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_16.setBaseSize(QtCore.QSize(0, 25))
        self.input_16.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_16.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_16.setObjectName("input_16")
        self.gridLayout.addWidget(self.input_16, 15, 1, 1, 1)
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
        self.input_7 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_7.sizePolicy().hasHeightForWidth())
        self.input_7.setSizePolicy(sizePolicy)
        self.input_7.setMinimumSize(QtCore.QSize(100, 20))
        self.input_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_7.setBaseSize(QtCore.QSize(0, 25))
        self.input_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_7.setObjectName("input_7")
        self.gridLayout.addWidget(self.input_7, 6, 1, 1, 1)
        self.res8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res8.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.res8.setFont(font)
        self.res8.setStyleSheet("#res8 {\n"
                                "    color: red;\n"
                                "}")
        self.res8.setObjectName("res8")
        self.gridLayout.addWidget(self.res8, 7, 2, 1, 1)
        self.input_6 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_6.sizePolicy().hasHeightForWidth())
        self.input_6.setSizePolicy(sizePolicy)
        self.input_6.setMinimumSize(QtCore.QSize(100, 20))
        self.input_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_6.setBaseSize(QtCore.QSize(0, 25))
        self.input_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_6.setObjectName("input_6")
        self.gridLayout.addWidget(self.input_6, 5, 1, 1, 1)
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
        self.input_5 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_5.sizePolicy().hasHeightForWidth())
        self.input_5.setSizePolicy(sizePolicy)
        self.input_5.setMinimumSize(QtCore.QSize(100, 20))
        self.input_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_5.setBaseSize(QtCore.QSize(0, 25))
        self.input_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_5.setObjectName("input_5")
        self.gridLayout.addWidget(self.input_5, 4, 1, 1, 1)
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
        self.input_15 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_15.sizePolicy().hasHeightForWidth())
        self.input_15.setSizePolicy(sizePolicy)
        self.input_15.setMinimumSize(QtCore.QSize(100, 20))
        self.input_15.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input_15.setBaseSize(QtCore.QSize(0, 25))
        self.input_15.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_15.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_15.setObjectName("input_15")
        self.gridLayout.addWidget(self.input_15, 14, 1, 1, 1)
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
        self.warning = QtWidgets.QLabel(MainWindow)
        self.warning.setGeometry(QtCore.QRect(40, 520, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.warning.setFont(font)
        self.warning.setText(" ")
        self.warning.setObjectName("warning")

        self.retranslateUi(MainWindow)
        self.scroll8.valueChanged['int'].connect(self.res8.setNum)
        self.scroll10.valueChanged['int'].connect(self.res10.setNum)
        self.scroll12.valueChanged['int'].connect(self.res12.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.input_1, self.input_2)
        MainWindow.setTabOrder(self.input_2, self.input_3)
        MainWindow.setTabOrder(self.input_3, self.input_4)
        MainWindow.setTabOrder(self.input_4, self.input_5)
        MainWindow.setTabOrder(self.input_5, self.input_6)
        MainWindow.setTabOrder(self.input_6, self.input_7)
        MainWindow.setTabOrder(self.input_7, self.input_9)
        MainWindow.setTabOrder(self.input_9, self.input_11)
        MainWindow.setTabOrder(self.input_11, self.input_13)
        MainWindow.setTabOrder(self.input_13, self.input_14)
        MainWindow.setTabOrder(self.input_14, self.input_15)
        MainWindow.setTabOrder(self.input_15, self.input_16)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Варианты гидравлических героторных двигателей"))
        MainWindow.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        self.label.setText(_translate("MainWindow", "Варианты гидравлических героторных двигателей"))
        self.label_11.setText(_translate("MainWindow", "Высота крышки, мм"))
        self.res16.setText(_translate("MainWindow", "16"))
        self.label_8.setText(_translate("MainWindow", "Диаметр двигателя, мм"))
        self.label_3.setText(_translate("MainWindow", "Рабочий объем, см3"))
        self.input_1.setHtml(_translate("MainWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                        "type=\"text/css\">\n "
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                        "font-size:8.25pt; font-weight:400; font-style:normal;\">\n "
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                        "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                        "font-size:10pt;\">0.9</span></p></body></html>"))
        self.res1.setText(_translate("MainWindow", "1"))
        self.label_12.setText(_translate("MainWindow", "Ном. давление, МПа"))
        self.res11.setText(_translate("MainWindow", "11"))
        self.res7.setText(_translate("MainWindow", "7"))
        self.label_2.setText(_translate("MainWindow", "Номинальный крутящий момент, Н/м"))
        self.label_4.setText(_translate("MainWindow", "Ном. расх. гидр. жидк., л/мин"))
        self.res3.setText(_translate("MainWindow", "3"))
        self.res9.setText(_translate("MainWindow", "9"))
        self.res13.setText(_translate("MainWindow", "13"))
        self.label_10.setText(_translate("MainWindow", "Высота ротора, мм"))
        self.res10.setText(_translate("MainWindow", "15"))
        self.label_15.setText(_translate("MainWindow", "Удельная мощность, кВт/кг"))
        self.label_7.setText(_translate("MainWindow", "Ном. механическая мощность,кВт"))
        self.res12.setText(_translate("MainWindow", "20"))
        self.res6.setText(_translate("MainWindow", "6"))
        self.res8.setText(_translate("MainWindow", "180"))
        self.label_9.setText(_translate("MainWindow", "Высота двигателя, мм"))
        self.label_14.setText(_translate("MainWindow", "Масса, кг"))
        self.res5.setText(_translate("MainWindow", "5"))
        self.label_5.setText(_translate("MainWindow", "Ном. частота вращения, мин-1"))
        self.res14.setText(_translate("MainWindow", "14"))
        self.res4.setText(_translate("MainWindow", "4"))
        self.label_6.setText(_translate("MainWindow", "Ном. гидравлическая мощность,кВт"))
        self.label_1.setText(_translate("MainWindow", "КПД"))
        self.res2.setText(_translate("MainWindow", "2"))
        self.res15.setText(_translate("MainWindow", "15"))
        self.label_16.setText(_translate("MainWindow", "Ориентировочная стоимость, руб"))
        self.label_13.setText(_translate("MainWindow", "Макс. давление, МПа"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
