from PyQt5.QtWidgets import (QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QApplication, QGridLayout, QComboBox, QLineEdit)
from PyQt5.QtCore import pyqtSlot, QDate, QDateTime, pyqtSignal
import PyQt5.uic as uic
import sys
from UiList import Ui_List
from parking_slots import Parking_Slots

from module.Parking_All_Functions import *
from module.db_parking import add_Customer_Info, viewData_byCategory, view_CustomerInfo_byCatogory, get_customerID
from datetime import datetime, timedelta
from module.log_decorator import _generate_log
from parking_bill import Parking_Bill

class Customer_DataWindow(QMainWindow):
    
    def __init__(self):
        super(Customer_DataWindow, self).__init__()
        
        uic.loadUi(Ui_List.Customer_Data, self)
        self.logger = _generate_log()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Customer Data')
        self.vehicle_type = self.cb_vehicleTypes.currentText()
        self.label_findSlot.clicked.connect(self.findSlot)
    
        self.txt_dateTime.setDateTime(datetime.now())
        self.btn_park.clicked.connect(self.action)
        #self.cb_vehicleTypes.activated.connect(self.is_SpaceAvailable(self.vehicle_type))
    def action(self): # onclick Button Park
        index = self.cb_parkingType.currentIndex()
        #print(index)
        if index == 0:
            self.add_CustomerInfo(index)
        elif index == 1:
           self.payBill(index)
        elif index == 2:
            self.payBill(index)
            
    def payBill(self, index):
        print("Hiii")
        max_id, v_type, v_no, entry_time, exit_time, charges = self.get_Bill_Details(index)
        #print(max_id, v_type, v_no, entry_time, exit_time, charges)
        self.bill_window = Parking_Bill(max_id, v_type, v_no, entry_time, exit_time, charges, index)
        self.bill_window.payment_signal.connect(self.get_PaymentSignal)
        self.bill_window.show()

    def get_Exit_DateTime(self, index):
        print("GET Date")
        entry_time = datetime.now()
        if index == 0:
            exit_time = None
        elif index == 1:
            one_day = timedelta(days=1)
            end_day = entry_time + one_day 
            exit_time = end_day.strftime("%d-%m-%Y %I:%M %p")
        elif index == 2:
            month_delta = timedelta(days=30)
            end_day = entry_time + month_delta
            exit_time = end_day.strftime("%d-%m-%Y %I:%M %p") # I for hr clock, p for am/pm
        entry_time = entry_time.strftime("%d-%m-%Y %I:%M %p") 
        print(entry_time, exit_time)
        return entry_time, exit_time

    def get_Bill_Details(self, index):
        max_id = int(get_customerID()) + 1  # get last customer id from database
        v_type = self.cb_vehicleTypes.currentText()
        v_no = self.vehicle_no.text()
        print(str(max_id), v_type, v_no)
        #entry_time = self.txt_dateTime.dateTime().toString("dd-MM-yyyy hh:mm A")
        entry_time, exit_time = self.get_Exit_DateTime(index)
        charges = get_Parking_Charges(v_type, index, exit_time)
        
        return (str(max_id), v_type, v_no, entry_time, exit_time, charges)

    @pyqtSlot(int, int)
    def get_PaymentSignal(self, flag, index):
        if flag == 1:
            self.add_CustomerInfo(index)
        
    def findSlot(self, event):
        self.logger.info("Customer is finding free slot...")
        v_type = self.cb_vehicleTypes.currentText()
        space_available = self.is_SpaceAvailable(v_type)
        if space_available:
            self.window = Parking_Slots(v_type)
            self.window.signal_PassData.connect(self.getSlotName)
            self.window.show()
        
    @pyqtSlot(str)
    def getSlotName(self, txt):
        #self.text = txt
        self.lineEdit_4.setText(txt)

    def addCustomer_toDB(self, name, mob_no, v_type, v_no, entry_time, exit_time, slot_Name):

        result = add_Customer_Info(name, mob_no, v_type, v_no, entry_time, exit_time, slot_Name)
        if result:
            messageBox("Congrats", f"{name} you are Parked in successfully!")
            self.logger.info(f"Customer: {name} Parked in successfully!")
            
        else:
            warning("Alert","Something went Wrong!")
            self.logger.warning("Alert","Something went Wrong!")

    def add_CustomerInfo(self, index):
        print("add_CustomerInfo")
        name = self.txt_name.text()
        mob_no = self.txt_mobileNo.text()
        v_type = self.cb_vehicleTypes.currentText()
        v_no = self.vehicle_no.text()
        #entry_time = self.txt_dateTime.dateTime().toString("dd-MM-yyyy hh:mm A")
        slot_Name = self.lineEdit_4.text() 
        entry_time, exit_time = self.get_Exit_DateTime(index)
        
        if (not mob_no) or (not v_no) or (not slot_Name):
            warning("Alert","Please fill in all details")
        else:
            self.addCustomer_toDB(name, mob_no, v_type, v_no, entry_time, exit_time, slot_Name)

        #label.clicked.connect(self.send_SlotName)
    def is_SpaceAvailable(self, v_type):
        data = viewData_byCategory(v_type)
        slots_data = view_CustomerInfo_byCatogory(v_type) # get occupied slots
        #out = list(map(lambda x:x.strip(), for i in slots_data))
        occupied_slotsList = list(item.strip() for tup in slots_data for item in tup)
        for data_row in data:
                # check if all slots are occupied/ is Space available for parking
                if not data_row[2] == len(occupied_slotsList): 
                    self.logger.info(f"Occupied slots for {v_type} --> {occupied_slotsList}")
                    return True
                else:
                    messageBox("Sorry", "No Space Available")
                    #self.label_findSlot.setEnabled(False)
                    return False
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Customer_DataWindow()
    MainWindow.show()
    app.exec_()

