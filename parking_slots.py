from PyQt5.QtWidgets import (QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QApplication, QGridLayout)
from PyQt5.QtCore import pyqtSlot, pyqtSignal
import PyQt5.uic as uic
import sys
from UiList import Ui_List
from module.Parking_All_Functions import *
from module.db_parking import viewData_byCategory, view_CustomerInfo_byCatogory
from module.log_decorator import _generate_log

class Parking_Slots(QMainWindow):
    signal_PassData = pyqtSignal(str)
    
    def __init__(self, vehicle_type):
        super(Parking_Slots, self).__init__()
        self.vehicle_type = vehicle_type
        uic.loadUi(Ui_List.Parking_Slots, self)
        self.logger = _generate_log()

        self.initUi()
        
        #self.parent = parent
        
    def initUi(self):

        self.setWindowTitle('Parking Slots')
        self.btn_close.clicked.connect(self.close_Window)
        self.color_red.setStyleSheet("background-color: #FF4040")
        self.color_green.setStyleSheet("background-color: #32CC99")
        
        self.vertical_layout = QVBoxLayout()
        self.gridLayout = self.gridLayout
        #self.gridLayout.setSpacing(0)
        self.vertical_layout.addLayout(self.gridLayout)
        self.vertical_layout.addStretch()
        self.viewSlots()
        self.show()

    def total_OccupiedSlots(self):
        data = viewData_byCategory(self.vehicle_type)
        slots_data = view_CustomerInfo_byCatogory(self.vehicle_type) # get occupied slots
        #out = list(map(lambda x:x.strip(), for i in slots_data))
        slots_info = list(item.strip() for tup in slots_data for item in tup)
        self.logger.info(f"Occupied slots for {self.vehicle_type} --> {slots_info}")
        return data,slots_info
    @pyqtSlot()
    def viewSlots(self):
        # get occupied slots list
        data, occupied_slotsList = self.total_OccupiedSlots()

        if data:
            for data_row in data:
                # check if all slots are occupied/ is Space available for parking
                if not data_row[2] == len(occupied_slotsList): 
                    row = 0
                    col = 0
                    # Loop from 1 to total_slots for Vehicle_type
                    for i in range(1, (data_row[2]+1)):
                        label = QPushButton("Slot " + str(i))
                        label.setObjectName("Slot " + str(i))
                        label.clicked.connect(self.send_SlotName)  
                        slot = label.text()
                    
                        if slot in occupied_slotsList:
                        
                            label.setStyleSheet("background-color: #FF4040 ; color: white ; width: 100px ; height: 100px")
                            label.setEnabled(False)
                        else:
                            label.setStyleSheet("background-color: #32CC99 ; width: 100px ; height: 100px")
                    
                        if col%5 == 0:
                            col = 0
                            row = row + 1
                        self.gridLayout.addWidget(label, row, col)
                        col = col + 1
                else:
                    messageBox("Sorry", "No Space Available")
                    
        
        
    
    
    def send_SlotName(self):
        sending_button = self.sender()
        self.logger.info(f"Customer selected {sending_button.text()} to park {self.vehicle_type}")
        
        self.signal_PassData.emit(sending_button.text())
        #self.hide()
     
    def close_Window(self):
        self.hide()

'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Parking_Slots()
    Window.show(s)
    sys.exit(app.exec_())
'''
