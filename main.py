from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QMessageBox,QLineEdit
from PyQt5.QtCore import pyqtSlot
import PyQt5.uic as uic
import sys
from UiList import Ui_List

vehicle_Types = ["Bike", "Car", "3 Wheeler", "Bus", "Truck"]
class DataWindow(QMainWindow):
    def __init__(self):
        super(DataWindow, self).__init__()
        uic.loadUi(Ui_List.AddRates, self)

        self.setWindowTitle('Add Vehicle Data')
        self.fillCombobox()
        
        #self.login = Ui_MainWindow()
        
        #self.first.change_btn.clicked.connect(self.go_to_secon)
        # find button with name btn_save
        
        self.btn_save.clicked.connect(self.virajData)
        
        self.Vehicle_Type = self.findChild(QLineEdit, 'vehicle_types')
        self.Parking_No = self.findChild(QLineEdit, 'txt_ParkingNo')
        self.Total_slots = self.findChild(QLineEdit, 'txt_TotalSlots')
        self.Hourly_Rate = self.findChild(QLineEdit, 'txt_HourlyRate')
        self.Day_Pass_Rate = self.findChild(QLineEdit, 'txt_DayPass_Rate')
        #self.Discount_Rate = self.findChild(QLineEdit, 'txt_DiscountRate')
        #self.Reserved_Park_Rate = self.findChild(QLineEdit, 'txt_ReservedRate')
        
    def virajData(self):
        
        self.txt_show.setText(self.txt_ParkingNo.text())
        
    '''def printButtonPressed(self):
        self.txt_ParkingNo.setText("hello")

        alert = QtWidgets.QMessageBox()
        alert.setText("You clicked the button!")
        alert.exec_()'''
    
    def saveData(self):
        
        # executed when button is pressed
        '''alert = QMessageBox()
        alert.setText("You clicked")
        alert.exec_()'''
        vehicle_Type = self.Vehicle_Type.currentText()
        
        parking_No = self.Parking_No.text()
        total_slots = self.Total_slots.text()
        hourly_Rate = self.Hourly_Rate.text()
        day_Pass_Rate = self.Day_Pass_Rate.text()
        monthly_Rate = self.Monthly_Rate.text()
        self.txt_show.setText(vehicle_Type+parking_No+total_slots+day_Pass_Rate+monthly_Rate)
        #discount_Rate = self.Discount_Rate.text()
        #reserved_Park_Rate = self.Reserved_Park_Rate.text()
    
        #list_data = [Vehicle_Type,Parking_No,Total_slots,Hourly_Rate,Day_Pass_Rate,Monthly_Rate,Discount_Rate,Reserved_Park_Rate]'''

        #from db_parking import addRate_of_Parking
        #addRate_of_Parking(list_data)
        
        
        

    @pyqtSlot()
    def fillCombobox(self):
        for v in vehicle_Types:
            self.vehicle_types.addItem(v)

def showWindow():
    app = QApplication(sys.argv)
    window = DataWindow()
    window.show()
    sys.exit(app.exec_())
showWindow()
'''
if __name__ == "__main__":   
    showWindow() '''
    

'''import sysbbQApplication
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType(“tax_calc.ui”)

class MyApp(QMainWindow):
def __init__(self):
super(MyApp, self).__init__()
self.ui = Ui_MainWindow()
self.ui.setupUi(self)
self.ui.calc_tax_button.clicked.connect(self.CalculateTax)

def CalculateTax(self):
price = int(self.ui.price_box.toPlainText())
tax = (self.ui.tax_rate.value())
total_price = price + ((tax / 100) * price)
total_price_string = “The total price with tax is: ” + str(total_price)
self.ui.results_window.setText(total_price_string)

if __name__ == “__main__”:
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
'''