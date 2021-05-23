from PyQt5.QtWidgets import *
from module.db_parking import viewData_byCategory
from datetime import datetime
from module.log_decorator import _generate_log
logger = _generate_log()
def login(username, password):
    while True:
        if (username == "ashwini") and (password == "123"):
            #messageBox("Congrats","You are logged in")
            return True
        else:
            return False
def messageBox(title,message):
    mess = QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)
    mess.setStandardButtons(QMessageBox.Ok)
    mess.exec_()
       
def warning(title,message):
    mess = QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)
    mess.setStandardButtons(QMessageBox.Ok)
    mess.exec_()

def get_Parking_Charges(v_type, index, exit_DT):
    data = viewData_byCategory(v_type)
    for row in data:
        if index == 0:
            bill = row[3]
        elif index == 1:
            charges = row[4] 
            bill = get_Renewed_Bill(int(charges), index, exit_DT)
        elif index == 2:
            charges = row[5]
            bill = get_Renewed_Bill(int(charges), index, exit_DT)
    print(str(bill))
    return str(bill) 
def get_Renewed_Bill(charges, index, exit_DT):
    exit_time = datetime.strptime(exit_DT, '%d-%m-%Y %I:%M %p') # convert string date to datetime format
    actual_exit_time = datetime.now()
    duration = actual_exit_time - exit_time # timedelta
    tot_sec = duration.total_seconds()
    hours = round(tot_sec/3600, 2)
    print()
    if index == 1:
        new_bill = charges + ((charges/24) * hours)
    elif index == 2:
        days = round(h/24, 2)
        new_bill = charges + ((charges/30)* days)
    logger.info(f"advanced charges:{charges} -> renewed Bill:{new_bill}")
    return round(new_bill, 2)  

def main():
    pass
    #get_Parking_Charges('Bike', 1)

if __name__ == '__main__':
    main()
