from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QMessageBox,QLineEdit
from PyQt5.QtCore import pyqtSlot
import PyQt5.uic as uic
import sys
from UiList import Ui_List
from PyQt5.QtCore import QThread, pyqtSignal
#from threading import *
vehicle_Types = ["Bike", "Car", "3_Wheeler", "Bus", "Truck"]
import time
from module.db_parking import addRate_of_Parking as addData
from module.db_parking import get_Added_Vehicles as getData
from module.Parking_All_Functions import *
from module.log_decorator import _generate_log
#from admin_dashboard import Dashboard
class addData_Window(QMainWindow):
    def __init__(self):
        super(addData_Window, self).__init__()
        uic.loadUi(Ui_List.AddRates, self)
        self.setWindowTitle('Add Vehicle Data')
        self.fillCombobox()
        #t1 = Thread(target=MyThread().virajData(self))
        self.btn_save.clicked.connect(self.add_VehicleData)
        self.btn_back.clicked.connect(self.func_cancel)
        self.logger = _generate_log()
    @pyqtSlot()
    def fillCombobox(self):
        # check whether data of vehicle-type is already inserted in database
        data = getData()
        # get all items of combobox(i.e list of vehicles)
        AllItems = [self.vehicle_types.itemText(i) for i in range(self.vehicle_types.count())]
        print(str(self.vehicle_types.count()))
        print(AllItems)
        if data:
            for row in data:
                if row[0] in AllItems:
                    # findText() finds index of text(Vehicle_type)
                    self.txt_show.append(row[0])
                    print(row[0])
                    self.vehicle_types.removeItem(self.vehicle_types.findText(row[0]))
        
    @pyqtSlot()
    def func_cancel(self):
        self.hide()

    def add_VehicleData(self):
        v1 = self.vehicle_types.currentText()
        self.logger.info(f"Admin Adding -->{v1} Data (Vehicle_type,Parking Block, Slots, Rates of Parking)")
        v2 = self.txt_ParkingNo.text()
        v3 = self.txt_TotalSlots.text()
        v4 = self.txt_HourlyRate.text()
        v5 = self.txt_DayPass_Rate.text()
        v6 = self.txt_MonthlyRate.text()
        v7 = self.txt_new.text()
        v8 = self.txt_Reserved.text()
        if (not v2) or (not v3) or (not v4) or (not v5) or (not v6) or (not v7) or (not v8):
            warning("Alert","Please fill in all details")
        else:
            self.add_VehicleData_toDB(v1, v2, v3, v4, v5, v6, v7, v8)
        
    
    def add_VehicleData_toDB(self, v1, v2, v3, v4, v5, v6, v7, v8):
        result = addData(v1, v2, v3, v4, v5, v6, v7, v8)
        if result:
            messageBox("Congrats", f"{v1} Data saved to DB successfullly!")
            self.logger.info(f"{v1} Data including Parking Rates saved to DB successfullly!")
        else:
            warning("Alert","Something went Wrong!")
            self.logger.warning("Alert","Something went Wrong!")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    addWindow = addData_Window()
    addWindow.show()
    app.exec_()

