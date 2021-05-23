from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtCore import pyqtSlot
import PyQt5.uic as uic
import sys
from UiList import Ui_List
from PyQt5.QtCore import QThread, pyqtSignal
from module.db_parking import viewData_byCategory as view_Data
from module.db_parking import updateData_byCategory as update_Data
from module.Parking_All_Functions import *
#from admin_dashboard import Dashboard
from module.log_decorator import _generate_log
vehicle_Types = ["Bike", "Car", "3_Wheeler", "Bus", "Truck"]

class EditDataPage(QMainWindow):
    
    def __init__(self, vehicle_index, vehicle_type):
        super(EditDataPage, self).__init__()
        self.vehicle_index = vehicle_index
        self.vehicle_type = vehicle_type
        uic.loadUi(Ui_List.EditRates, self)
        self.logger = _generate_log()
        self.initUi()
        
    def initUi(self):
        self.setWindowTitle('Edit Vehicle Data')
        self.fillCombobox()
        # Disable checkbox
        #index = self.vehicle_types.findText(self.vehicle_type, QtCore.Qt.MatchFixedString)
        self.vehicle_types.setCurrentIndex(self.vehicle_index)
        self.vehicle_types.setEnabled(False)
        #self.viewData()
        self.btn_saveChanges.clicked.connect(self.func_editData)
        self.btn_back.clicked.connect(self.func_cancel_Edit)

    def func_cancel_Edit(self):
       self.hide()
    
    def viewData(self):
        print(self.vehicle_type)
        data = view_Data(self.vehicle_type)
        print(data)
    
    @pyqtSlot()
    def fillCombobox(self):
        for v in vehicle_Types:
            self.vehicle_types.addItem(v)    

    def func_editData(self):
        
        v2 = self.txt_ParkingNo.text()
        v3 = self.txt_TotalSlots.text()
        v4 = self.txt_HourlyRate.text()
        v5 = self.txt_DayPass_Rate.text()
        v6 = self.txt_MonthlyRate.text()
        v7 = self.txt_new.text()
        v8 = self.txt_Reserved.text()
        #list_data = [v1,v2,v3,v4,v5,v6,v7,v8]
        updated_Data = update_Data(self.vehicle_type,v2,v3,v4,v5,v6,v7,v8) 
        if update_Data:
            messageBox("Congrats", f"{self.vehicle_type} data updated successfully!")
            self.logger.info(f"Admin has updated {self.vehicle_type} data successfully!")
        else:
            warning("Alert","Something went Wrong!")
            self.logger.warning(f"Something went Wrong while updating {self.vehicle_type} data!")

'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    editWindow = EditDataPage()
    editWindow.show()
    sys.exit(app.exec_())
'''