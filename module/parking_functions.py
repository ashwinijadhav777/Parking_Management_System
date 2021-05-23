# project PARKING MANAGEMENT
#Parking Lot - the entire place with areas to park
#Parking Slot - a section in the parking lot for one vehicle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3
import module.db_parking
username = "ashwini"
password = "123"
width = 100
phash = "-"*width
title = "PARKING MANAGEMENT"
database = r"F:\Python Important\project_parking\db_parking.db"
# from module.db_parking import cr
# dbc_in_file = module.db_parking.create_connection(database, )
# db_cursor = dbc_in_file.cursor()
########################################################################

def print_Header():
    print(f"\n{phash} \n{title.center(width)}\n{phash}\n")

def error_login_msg():
    print("Invalid username/password, input username & password again!\n")
def error_choice_msg():
    print("\nPlease enter valid choice (1/2/3):\n")

def addRate_of_Parking(list_data):
    '''Vehicle_Type = input("""
                             1: Bike
                             2: Auto
                             3: Car
                             4: Bus/Truck

                             Please enter your choice: """)
    Parking_No = input(f"Enter parking_No for {Vehicle_Type}: ")
    Total_slots = int(input(f"Enter total_slots for {Vehicle_Type}: "))
    Hourly_Rate = int(input("Enter Hourly Rate: "))
    Day_Pass_Rate = int(input("Enter Day_Pass Rate: "))
    Monthly_Rate = int(input("Enter Monthly Rate: "))
    Discount_Rate = int(input("Enter Discount Rate: "))
    Reserved_Park_Rate = int(input("Enter Reserved_Parking Rate: "))
    '''
    #list_data = [Vehicle_Type,Parking_No,Total_slots,Hourly_Rate,Day_Pass_Rate,Monthly_Rate,Discount_Rate,Reserved_Park_Rate]
    
    dbc_in_file.execute("INSERT INTO AddData VALUES (?, ?, ?, ?, ?, ?, ?, ?)",list_data)
   
    db_cursor.execute("SELECT * FROM AddData")
    print("*"*20)
    print(db_cursor.fetchall())
    dbc_in_file.commit()
    dbc_in_file.close()

def choose_optionsForAdmin():
    choice = input("""
    				A: Enter Data
    				B: Edit Data
    				C: Manage Slots
    				D: Manage Rate
    				E: Manage Parking

    				Please enter your choice: """)
    if choice == "A" or choice == "a":
        addRate_of_Parking()
        pass

def login(username, password):
    while True:
        if (username == "ashwini") and (password == "123"):
            #messageBox("Congrats","You are logged in")
            return True
        else:
            return False
            #warning("Alert","Enter correct details")
            
    '''while True:
        user = input("Enter username:")
        psw = input("Enter password:")
        if (user == username) and (psw == password):
            print(f"{user} logged in successfully\n")
            print_Header()
            choose_optionsForAdmin()
            break
        else:
            error_login_msg()
            continue
    '''
def common_login_screen():

    while True:
        print_Header()
        print("\nPlease select your choice from below menu:\n\n")
        print(f'1)Admin Login')
        print(f'2)Customer Login')
        print(f'3)Exit')
        option=input("\nEnter your choice 1(Admin)/2(Customer)/3(Exit):")
        if option == "1":
            login()
            break
        elif option == "2":
            pass
            break
        elif option == "3":
            break
        else:
            error_choice_msg()
            continue
def main():
    pass
if __name__ == '__main__':
    main()

