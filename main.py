# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:58:00 2022

@author: talha
"""

import sys

from PyQt5 import QtWidgets

from src.GUI.LoginPage import Ui_MainWindow as LoginPage


file_name = "logs/users.json"

import threading

def show_page(ui_window):
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    return app
    
def load_initial_data():
        import os, json
        global file_name
        users_data = []

        current_place = os.getcwd()
        print(f"My current location : {current_place}")
        
        with open(file_name,"r") as f:
            for jsonObj in f:
                data = json.loads(jsonObj)
                users_data.append(data)
        
        return users_data

def login_page_task(lgpage):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    lgpage.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    
    print("Program started ... ")
   
    lgpage = LoginPage()
    login_page = threading.Thread(target = login_page_task(lgpage))
    login_page.daemon = True
    login_page.start()

