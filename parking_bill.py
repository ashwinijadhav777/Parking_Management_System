
from PyQt5.QtWidgets import (QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QApplication)
import PyQt5.uic as uic
import sys
from UiList import Ui_List
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from module.log_decorator import _generate_log
from module.Parking_All_Functions import *
#from addData_Page import *

class Parking_Bill(QMainWindow):
	payment_signal = pyqtSignal(int, int)
	hourly_paid_signal = pyqtSignal(int, str)
	def __init__(self, ID, vehicle, vehicle_no, entry, exit, bill, index):
		super(Parking_Bill, self).__init__()
		self.TicketNo = ID
		self.Vehicle = vehicle
		self.Vehicle_No = vehicle_no
		#print(self.vehicle_no)
		self.Entry_DT = entry
		self.Exit_DT = exit
		self.bill = bill
		self.pass_index = index 

		self.logger = _generate_log()
		#print(self.Exit_DT - self.entry_DT)
		uic.loadUi(Ui_List.Parking_Bill, self)

		self.initUi()
	
	def initUi(self):
		self.setWindowTitle("Parking Bill")
		self.ticket_No.setText(self.TicketNo)
		#print(self.entry_DT)
		self.vehicle_type.setText(self.Vehicle)
		self.vehicle_no.setText(self.Vehicle_No)
		self.entry_dateTime.setText(self.Entry_DT)
		self.exit_dateTime.setText(self.Exit_DT)
		self.parking_charges.setText("Rs "+str(self.bill))
		if self.pass_index == 0: #check if parking type is not Hourly
			self.btn_pay.clicked.connect(self.on_PaidAction)
		else:
			self.btn_pay.clicked.connect(self.send_PaymentSignal)
	def on_PaidAction(self):
		self.logger.info(f"Customer with ID:{self.TicketNo} and vehicle_no:{self.Vehicle_No} has paid Rs:{self.bill}")
		messageBox("Payment Success", "Thank you, Visit Again...")
		self.hourly_paid_signal.emit(1, self.TicketNo)
		self.close()
	
	@pyqtSlot()
	def send_PaymentSignal(self):
		self.logger.info(f"Customer with ID:{self.TicketNo} and vehicle_no:{self.Vehicle_No} has paid Rs:{self.bill}")
		self.payment_signal.emit(1, self.pass_index)
		self.close()
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Parking_Bill()
    Window.show()
    app.exec_()
'''