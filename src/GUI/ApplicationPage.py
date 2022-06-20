# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ApplicationPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(110, 0, 561, 100))
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
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 130, 31, 331))
        self.progressBar.setProperty("value", 5)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 150, 121, 61))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 270, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 380, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 270, 121, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 380, 121, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 235, 151, 181))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 170, 151, 41))
        self.label_5.setObjectName("label_5")
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
        
        self.pushButton.clicked.connect(self.modelchosing)
        self.pushButton_2.clicked.connect(self.imagechosing)
        self.pushButton_3.clicked.connect(self.running)

    def modelchosing(self):
        #self.label.adjustSize()
        self.progressBar.setValue(33)
        fname = QFileDialog.getOpenFileName(self.MainWindow, 'Open file','../Models',"Model files (*.p)") # models are end with .p extention
        self.label.setText((str(fname[0]).split("Models/"))[1])
        print(str(fname))
    def imagechosing(self):
        #self.label.adjustSize()
        fname = QFileDialog.getOpenFileName(self.MainWindow, 'Open file','../Cxr_images',"Image files (*.png)") # models are end with .p extention
        self.label_2.setText("Image Selected\n\n"+(str(fname[0]).split("Cxr_images/"))[1])
        self.label_4.clear()
        self.label_4.setPixmap(QtGui.QPixmap(fname[0]))
        self.label_4.setScaledContents(True)

        self.progressBar.setValue(66)

    def running(self):
        self.label_3.setText("Button Pressed")
        #self.label.adjustSize()
        self.progressBar.setValue(99)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Detection of Covid-19 with Chest X-Ray Images"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.pushButton.setText(_translate("MainWindow", "Choose Model"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "Choose Image"))
        self.pushButton_3.setText(_translate("MainWindow", "RUN"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "RESULT : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

