# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QDateTime, Qt, QTimer

#maini çalıştırıken bunu , burdan çalıştırırken altı
from src.GUI.RegisterPage import Ui_MainWindow as RegisterPage

#birbirlerine olan konumları önemli
#from RegisterPage import Ui_MainWindow as RegisterPage

createdby = "M. N. Talha Kilic"
version = "1.0.1"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(240, 240, 125, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 240, 128, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(240, 280, 107, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 280, 128, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_Enter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Enter.setGeometry(QtCore.QRect(440, 350, 101, 23))
        self.pushButton_Enter.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../imgs/checked.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_Enter.setIcon(icon)
        self.pushButton_Enter.setIconSize(QtCore.QSize(40, 20))
        self.pushButton_Enter.setCheckable(False)
        self.pushButton_Enter.setAutoRepeat(False)
        self.pushButton_Enter.setAutoExclusive(False)
        self.pushButton_Enter.setObjectName("pushButton_Enter")
        self.pushButton_Register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Register.setGeometry(QtCore.QRect(330, 350, 101, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../imgs/202788-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_Register.setIcon(icon1)
        self.pushButton_Register.setIconSize(QtCore.QSize(40, 25))
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.pushButton_Renew = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Renew.setGeometry(QtCore.QRect(214, 350, 111, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../imgs/178338_19122016_53141887.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_Renew.setIcon(icon2)
        self.pushButton_Renew.setIconSize(QtCore.QSize(40, 20))
        self.pushButton_Renew.setObjectName("pushButton_Renew")
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
        self.label_createdby = QtWidgets.QLabel(self.centralwidget)
        self.label_createdby.setGeometry(QtCore.QRect(40, 470, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_createdby.setFont(font)
        self.label_createdby.setObjectName("label_createdby")
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(600, 470, 62, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_version.setFont(font)
        self.label_version.setObjectName("label_version")
        self.createdby_text = QtWidgets.QLabel(self.centralwidget)
        self.createdby_text.setGeometry(QtCore.QRect(140, 470, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.createdby_text.setFont(font)
        self.createdby_text.setObjectName("createdby_text")
        self.version_text = QtWidgets.QLabel(self.centralwidget)
        self.version_text.setGeometry(QtCore.QRect(670, 470, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.version_text.setFont(font)
        self.version_text.setObjectName("version_text")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(600, 30, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
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
        
        self.rgspage = RegisterPage()

        self.initalize_timer()
        self.startTimer()
        self.setupconnections()
        
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
        self.label_time.setText(time.toString(Qt.ISODate))
        
    def setupconnections(self):
        self.pushButton_Register.clicked.connect(self.openRegisterPage)
        
    def openRegisterPage(self):
        self.stopTimer()
        self.rgspage.setupUi(self.MainWindow)
        
        #setup Return Page Connections
        self.rgspage.ReturnButton.clicked.connect(self.openLoginPage)

        self.MainWindow.show()
        
    def openLoginPage(self):
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_username.setText(_translate("MainWindow", "username :"))
        self.label_password.setText(_translate("MainWindow", "password :"))
        self.pushButton_Enter.setText(_translate("MainWindow", "Enter"))
        self.pushButton_Register.setText(_translate("MainWindow", "Register"))
        self.pushButton_Renew.setText(_translate("MainWindow", "Renew Password"))
        self.label_title.setText(_translate("MainWindow", "Detection of Covid-19 with Chest X-Ray Images"))
        self.label_createdby.setText(_translate("MainWindow", "Created By : "))
        self.label_version.setText(_translate("MainWindow", "Version :"))
        self.createdby_text.setText(_translate("MainWindow", createdby))
        self.version_text.setText(_translate("MainWindow", version))
        self.label_time.setText(_translate("MainWindow", "-"))
        
        #make adjustment
        self.createdby_text.adjustSize()
        self.version_text.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

