# Admin Dashboard

from PyQt5.QtWidgets import (QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QApplication, QGridLayout)
import PyQt5.uic as uic
import sys
from UiList import Ui_List
from editData_Page import *
from addData_Page import *
from module.log_decorator import _generate_log
from View_customerList import View_Customers
from Login_Page import Ui_LoginWindow


class Dashboard(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi(Ui_List.Admin_Dashboard, self)
        self.logger = _generate_log()
        self.initUi()
           
    def initUi(self):
        self.setWindowTitle('Admin Dashboard')
        self.addData.clicked.connect(self.add_Data)
        self.editData.clicked.connect(self.edit_Data)
        self.customer_info.clicked.connect(self.View_customerInfo)
        self.logout.clicked.connect(self.admin_Logout)
   
    def View_customerInfo(self):
        self.view_customer = View_Customers()
        self.logger.info("Admin clicked -->View Customer Info")
        self.view_customer.show()

    def admin_Logout(self):
        self.logger.info("Admin logged out...")
        self.login_window = Ui_LoginWindow()
        self.login_window.show()
        #Window.close()
        self.hide()

    def add_Data(self):
        self.add_window = addData_Window()
        self.logger.info("Admin clicked -->Add Vehicle Data")
        self.add_window.show()
        #self.hide()
        #Window.close()
        #Window = Dashboard()
    
    def edit_Data(self):
        self.edit_window = EditDataWindow()
        self.logger.info("Admin clicked -->Edit Vehicle Data")
        self.edit_window.show()
        #Window.close()
        #Window.hide()
        #Window = Dashboard()
        
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Dashboard()
    Window.show()
    app.exec_()
