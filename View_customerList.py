from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,  QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
import PyQt5.uic as uic
import sys
from PyQt5.QtCore import pyqtSlot
from UiList import Ui_List
from module.db_parking import view_Customer_Info, viewData_byCategory, delete_Customer_Info
from parking_bill import Parking_Bill
from datetime import datetime
from module.log_decorator import _generate_log
from module.Parking_All_Functions import *
class View_Customers(QMainWindow):
    def __init__(self):
        super(View_Customers, self).__init__()
        uic.loadUi(Ui_List.View_CustomerData, self)
        self.logger = _generate_log()
        self.setWindowTitle('View Customers Data')
        #self.customer_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        header = self.customer_tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
        #header.setSectionResizeMode(9,QtWidgets.QHeaderView.Stretch)
        self.customer_tableWidget.resizeColumnsToContents()
        self.create_CustomerTable()
    
    
    def create_CustomerTable(self):
        result = view_Customer_Info()
        
        self.customer_tableWidget.setRowCount(0)
        # retrieve customer data from database
        for row_no, customer_data in enumerate(result): #tuples list
            self.customer_tableWidget.insertRow(row_no)
            
            for column_no, customer in enumerate(customer_data): # insert each element of tuple in table_row
                self.customer_tableWidget.setItem(row_no, column_no, QTableWidgetItem(str(customer)))
                btn_exit = QPushButton('Exit')
                #btn_exit.setObjectName('Exit' + str(row_no+1))
                btn_exit.clicked.connect(self.exit_parking)
                self.customer_tableWidget.setCellWidget(row_no, 8, btn_exit)
        
    def exit_parking(self):
        exit_button = self.sender()
        row  = self.customer_tableWidget.currentRow()
        exit_time = datetime.now()
        exit_DT = exit_time.strftime("%d-%m-%Y %I:%M %p") 
        # get data from table row
        ID, name, vehicle, vehicle_no, entry, exit = self.readValues_fromTableRow(row)
        self.logger.info(f"Customer named {name} Exiting Parking...")
        
        entry_time = datetime.strptime(entry, '%d-%m-%Y %I:%M %p') # convert string date to datetime format
        bill = self.calc_Bill(exit_time, entry_time, vehicle)
        #print(dt_now-my_time)
        if exit == str(None):
            self.bill_window = Parking_Bill(ID, vehicle, vehicle_no, entry, exit_DT, bill, 0)
            self.bill_window.hourly_paid_signal.connect(self.delete_HourlyRecord)
            self.bill_window.show()
            self.hide()
        else:
            delete_Customer_Info(ID)
        

        #self.hide()
    @pyqtSlot(int, str)
    def delete_HourlyRecord(self, paid, id):
        print("delete")
        if paid == 1:
            delete_Customer_Info(id)

    def calc_Bill(self, exit_DT, entry_DT, vehicle_type):
        duration = exit_DT - entry_DT
        totsec = duration.total_seconds()
        h = round(totsec/3600, 2) # hours
        #print(type(h))
        #m = (totsec%3600) // 60  # minutes
        charges = get_Parking_Charges(vehicle_type, 0, None) # get hourly parking Rate
        if round(h) == 0:
            return int(charges)
        else:
            return (int(charges*h))    
           
    def readValues_fromTableRow(self, currentRow):
        ID = self.customer_tableWidget.item(currentRow, 0)
        NAME = self.customer_tableWidget.item(currentRow, 1)
        VEHICLE = self.customer_tableWidget.item(currentRow, 3)
        VEHICLE_NO = self.customer_tableWidget.item(currentRow, 4)
        ENTRY_DATE_TIME = self.customer_tableWidget.item(currentRow, 5)
        EXIT_DATE_TIME = self.customer_tableWidget.item(currentRow, 6)
        return (ID.text(), NAME.text(), VEHICLE.text(), VEHICLE_NO.text(), ENTRY_DATE_TIME.text(), EXIT_DATE_TIME.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = View_Customers()
    MainWindow.show()
    app.exec_()
'''
def deleteProduct(self):
        row = self.products_table.currentRow()
        if row > -1:
           product_id = (self.products_table.item(row, 0).text(), )
           query = session.query(Product).filter(Product.product_id=='product_id').first()
           session.delete(query)
           session.commit()
            #self.dbCursor.execute("""DELETE FROM Main WHERE username=?""", currentUsername)
            #self.dbConn.commit()
           self.products_table.removeRow(row)'''