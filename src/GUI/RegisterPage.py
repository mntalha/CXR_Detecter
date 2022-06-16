# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QDateTime, Qt, QTimer

import json

file_name = "/logs/users.json"

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(460, 380, 101, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imgs/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setIconSize(QtCore.QSize(30, 20))
        self.saveButton.setCheckable(False)
        self.saveButton.setAutoRepeat(False)
        self.saveButton.setAutoExclusive(False)
        self.saveButton.setObjectName("saveButton")
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 200, 128, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(300, 200, 125, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 240, 128, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_surname = QtWidgets.QLabel(self.centralwidget)
        self.label_surname.setGeometry(QtCore.QRect(300, 240, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_surname.setFont(font)
        self.label_surname.setObjectName("label_surname")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 280, 128, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(300, 320, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 320, 128, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(300, 280, 125, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.ReturnButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReturnButton.setGeometry(QtCore.QRect(340, 380, 101, 23))
        self.ReturnButton.setObjectName("ReturnButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 30, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
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
        
        self.setupconnections()
    def setupconnections(self):
        self.saveButton.clicked.connect(self.save_user_info)
            
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

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.label_title.setText(_translate("MainWindow", "Detection of Covid-19 with Chest X-Ray Images"))
        self.label_name.setText(_translate("MainWindow", "Name         :"))
        self.label_surname.setText(_translate("MainWindow", "Surname    :"))
        self.label_password.setText(_translate("MainWindow", "Password   :"))
        self.label_username.setText(_translate("MainWindow", "Username  :"))
        self.ReturnButton.setText(_translate("MainWindow", "Return Login Page"))
        self.label.setText(_translate("MainWindow", " . . ."))

    def save_user_info(self):
        
        user = { "Name":  str(self.lineEdit.text()),
                 "Surname": str(self.lineEdit_2.text()),
                 "Username": str(self.lineEdit_3.text()),
                 "Password" : str(self.lineEdit_4.text())
            }
        try:
            with open(file_name, 'r+') as f:
                file_data = json.load(f)    # take the all data
                for usrs in file_data["user_data"]:
                    if user["Username"] == usrs["Username"]:
                        print("Change username")
                        return
                

                file_data["user_data"].append(user)
                f.seek(0)
                json.dump(file_data, f, indent = 4)
        except:
            print("Error occured in saving user file")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

