from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QMessageBox,QLineEdit
from PyQt5.QtCore import pyqtSlot
import PyQt5.uic as uic
import sys
from UiList import Ui_List
from Ui_editData_Page import EditDataPage
from module.db_parking import viewData_byCategory as view_Data
from module.Parking_All_Functions import *
from module.db_parking import view_addData_Table as getData
from module.log_decorator import _generate_log

class EditDataWindow(QMainWindow):
    def __init__(self):
        
        super(EditDataWindow, self).__init__()
        uic.loadUi(Ui_List.ManageRates, self)
        self.logger = _generate_log()
        self.initUi()
        
    def initUi(self): 
        self.setWindowTitle('Select Category to Edit')
        self.btn_editData.clicked.connect(self.func_selectCategory)
        self.btn_cancel.clicked.connect(self.func_cancel)
    
    @pyqtSlot()   
    def func_selectCategory(self):
        self.vehicle_type = self.cb_vehicles.currentText()
        print(self.vehicle_type)
        #index = self.cb_vehicles.findText(vehicle_type, QtCore.Qt.MatchFixedString)
        index = self.cb_vehicles.currentIndex()
        # pass index of selected item to next window
        self.nextWindow = EditDataPage(index, self.vehicle_type)
        #data = view_Data(self.vehicle_type)
       # print(data)
        self.viewData()
        
    @pyqtSlot()
    def func_cancel(self):
        self.hide()

    @pyqtSlot()
    def viewData(self):
        data = view_Data(self.vehicle_type)
        self.logger.info(f"Admin Editing -->{self.vehicle_type} Data (Vehicle_type,Parking Block, Slots, Rates of Parking)")
        if data:
            for row in data:
                
                self.nextWindow.txt_ParkingNo.setText(row[1])
                self.nextWindow.txt_TotalSlots.setText(str(row[2]))
                self.nextWindow.txt_HourlyRate.setText(str(row[3]))
                self.nextWindow.txt_DayPass_Rate.setText(str(row[4]))
                self.nextWindow.txt_MonthlyRate.setText(str(row[5]))
                self.nextWindow.txt_new.setText(str(row[6]))
                self.nextWindow.txt_Reserved.setText(str(row[7]))
            self.nextWindow.show()
            #window = EditDataWindow()
            self.hide()

        else:
            warning("Alert","Something went Wrong!")
            self.logger.warning("Alert","Something went Wrong!")

   
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditDataWindow()
    window.show()
    sys.exit(app.exec_())
'''