# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sergi\pythontraining\UI\fightGame.ui'
#
# Created: Thu Apr  2 15:04:54 2020
#      by: pyside2-uic  running on PySide2 5.11.0a1.dev1527942350
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fighter1label = QtWidgets.QLabel(self.frame)
        self.fighter1label.setObjectName("fighter1label")
        self.horizontalLayout.addWidget(self.fighter1label)
        self.fighter1NameEdit = QtWidgets.QTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fighter1NameEdit.sizePolicy().hasHeightForWidth())
        self.fighter1NameEdit.setSizePolicy(sizePolicy)
        self.fighter1NameEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fighter1NameEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.fighter1NameEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fighter1NameEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fighter1NameEdit.setObjectName("fighter1NameEdit")
        self.horizontalLayout.addWidget(self.fighter1NameEdit)
        self.fighter2label = QtWidgets.QLabel(self.frame)
        self.fighter2label.setObjectName("fighter2label")
        self.horizontalLayout.addWidget(self.fighter2label)
        self.fighter2NameEdit = QtWidgets.QTextEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fighter2NameEdit.sizePolicy().hasHeightForWidth())
        self.fighter2NameEdit.setSizePolicy(sizePolicy)
        self.fighter2NameEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.fighter2NameEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.fighter2NameEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fighter2NameEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.fighter2NameEdit.setObjectName("fighter2NameEdit")
        self.horizontalLayout.addWidget(self.fighter2NameEdit)
        self.fightButton = QtWidgets.QPushButton(self.frame)
        self.fightButton.setObjectName("fightButton")
        self.horizontalLayout.addWidget(self.fightButton)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.fighter1label.setText(QtWidgets.QApplication.translate("MainWindow", "Fighter 1", None, -1))
        self.fighter2label.setText(QtWidgets.QApplication.translate("MainWindow", "Fighter 2", None, -1))
        self.fightButton.setText(QtWidgets.QApplication.translate("MainWindow", "FIGHT", None, -1))

myWindow = Ui_MainWindow()
myWindow.show()