# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(935, 762)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1.setGeometry(QtCore.QRect(30, 20, 881, 71))
        self.groupBox_1.setObjectName("groupBox_1")
        self.pbURL_1 = QtWidgets.QPushButton(self.groupBox_1)
        self.pbURL_1.setGeometry(QtCore.QRect(780, 20, 91, 41))
        self.pbURL_1.setObjectName("pbURL_1")
        self.URLstring = QtWidgets.QLineEdit(self.groupBox_1)
        self.URLstring.setGeometry(QtCore.QRect(10, 20, 761, 41))
        self.URLstring.setObjectName("URLstring")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 100, 881, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.PrintRequests = QtWidgets.QLineEdit(self.groupBox_2)
        self.PrintRequests.setGeometry(QtCore.QRect(10, 50, 431, 241))
        self.PrintRequests.setObjectName("PrintRequests")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 431, 31))
        self.label.setObjectName("label")
        self.PrintHTTP = QtWidgets.QLineEdit(self.groupBox_2)
        self.PrintHTTP.setGeometry(QtCore.QRect(440, 50, 431, 241))
        self.PrintHTTP.setObjectName("PrintHTTP")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(440, 20, 431, 31))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 420, 881, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pbSucces_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pbSucces_2.setGeometry(QtCore.QRect(780, 20, 91, 41))
        self.pbSucces_2.setObjectName("pbSucces_2")
        self.PrintSuccesRequest = QtWidgets.QLineEdit(self.groupBox_3)
        self.PrintSuccesRequest.setGeometry(QtCore.QRect(10, 20, 761, 111))
        self.PrintSuccesRequest.setObjectName("PrintSuccesRequest")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 570, 881, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pbSite_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pbSite_3.setGeometry(QtCore.QRect(780, 20, 91, 41))
        self.pbSite_3.setObjectName("pbSite_3")
        self.SearchSite = QtWidgets.QLineEdit(self.groupBox_4)
        self.SearchSite.setGeometry(QtCore.QRect(10, 20, 761, 111))
        self.SearchSite.setObjectName("SearchSite")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_1.setTitle(_translate("MainWindow", "URL сайта"))
        self.pbURL_1.setText(_translate("MainWindow", "Поиск"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Выполнение запроса"))
        self.label.setText(_translate("MainWindow", "Вывод запросов"))
        self.label_2.setText(_translate("MainWindow", "Код состояния HTTP"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Вывод успешных запросов "))
        self.pbSucces_2.setText(_translate("MainWindow", "Вывести"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Вывод запросов на сайте "))
        self.pbSite_3.setText(_translate("MainWindow", "Вывести"))
