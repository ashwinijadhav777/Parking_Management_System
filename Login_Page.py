from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QMessageBox,QLineEdit
from PyQt5.QtCore import pyqtSlot, Qt
import PyQt5.uic as uic
import sys
from UiList import Ui_List
from module.log_decorator import _generate_log
from module.Parking_All_Functions import *
from module.db_parking import *
#from module.parking_functions import *
from module.Parking_All_Functions import *
from admin_dashboard import *
from customer_dataWindow import Customer_DataWindow

class Ui_LoginWindow(QMainWindow):
    def __init__(self):
        super(Ui_LoginWindow, self).__init__()
        uic.loadUi(Ui_List.LOGIN, self)
        self.setWindowTitle('Login')
        self.btn_login.clicked.connect(self.sign_in)
        self.customer_checkbox.stateChanged.connect(self.clickAction2)
        self.admin_checkbox.stateChanged.connect(self.clickAction)
        self.logger = _generate_log()
        #self.show()
    
    @pyqtSlot()
    def admin_dashboard(self):
        self.nextWindow = Dashboard()
        self.nextWindow.show()
        MainWindow.hide()
        
    def clickAction(self, state):
        if state == Qt.Checked:
            self.frame.setEnabled(True)
            self.customer_checkbox.setChecked(False)

    def clickAction2(self, state):
        if state == Qt.Checked:
            self.frame.setEnabled(False)
            self.admin_checkbox.setChecked(False)

    
    @pyqtSlot()
    def sign_in(self):
        # checking if admin_checkbox is checked ? 
        if self.admin_checkbox.isChecked():
            username = self.txt_username.text()
            password = self.txt_password.text()
            result = login(username, password)
            if result:
                messageBox(f"Congrats {username}","You are logged in succesfully!")
                self.logger.info(f"Admin : {username} logged in...")
                self.admin_dashboard()
            
            else:
                warning("Alert","Enter correct details")
                self.logger.info(f"Admin has entered Incorrect Details...")
        elif self.customer_checkbox.isChecked():
            self.custo_Window = Customer_DataWindow()
            self.custo_Window.show()
            MainWindow.hide()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Ui_LoginWindow()
    MainWindow.show()
    app.exec_()
'''
self.b.stateChanged.connect(self.clickBox)
        self.b.move(20,20)
        self.b.resize(320,40)

    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')
'''