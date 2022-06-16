# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RenewPasswdPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, Qt, QTimer

import json

file_name = "logs/users.json"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 30, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(130, 110, 561, 100))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setAutoFillBackground(False)
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setScaledContents(False)
        self.label_title.setWordWrap(True)
        self.label_title.setObjectName("label_title")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 300, 128, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(300, 220, 125, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 220, 128, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(300, 300, 107, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(460, 360, 101, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imgs/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setIconSize(QtCore.QSize(30, 20))
        self.saveButton.setCheckable(False)
        self.saveButton.setAutoRepeat(False)
        self.saveButton.setAutoExclusive(False)
        self.saveButton.setObjectName("saveButton")
        self.ReturnButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReturnButton.setGeometry(QtCore.QRect(340, 360, 101, 23))
        self.ReturnButton.setObjectName("ReturnButton")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(570, 220, 31, 21))
        self.toolButton.setObjectName("toolButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 260, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.initalize_timer()
        self.startTimer()
        
        self.toolButton.clicked.connect(self.check_user)
       
    def initalize_timer(self):
        self.timer = QTimer()
        #self.timer.setSingleShot(True)  
        self.timer.timeout.connect(self.showTime)
       
    def startTimer(self):
        self.timer.start(1000)
   
    def stopTimer(self):
        self.timer.stop()

    def showTime(self):
        time=QDateTime.currentDateTime()
        
        self.label.setText(time.toString())
    
    def check_user(self):
        user = { "username":  str(self.lineEdit.text())}
        try:
            with open(file_name, 'r+') as f:
                file_data = json.load(f)    # take the all data
                for usrs in file_data["user_data"]:
                    if user["username"] == usrs["Username"]:
                        print("User exist")
                        self.label_2.setText(str(usrs))
                        self.label_2.adjustSize()
                        return
        except:
            print("Error occured in saving user file")
                        
            
        self.label_2.setText("No user found")
        self.label_2.adjustSize()
        
       
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ". . ."))
        self.label_title.setText(_translate("MainWindow", "Detection of Covid-19 with Chest X-Ray Images"))
        self.label_username.setText(_translate("MainWindow", "username :"))
        self.label_password.setText(_translate("MainWindow", "password :"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.ReturnButton.setText(_translate("MainWindow", "Return Login Page"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

