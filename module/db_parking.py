# Database operations
import sqlite3
from sqlite3 import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from module.log_decorator import _generate_log
##################################################################################
database = r'Parking_Management.db'
conn = None
list_data = []
logger = _generate_log()

addData_table_sql = """ CREATE TABLE IF NOT EXISTS addData_table (
                        Vehicle_Type TEXT PRIMARY KEY NOT NULL,
                        Parking_No TEXT NOT NULL,
                        Total_slots INT NOT NULL,
                        Hourly_Rate INT NOT NULL,
                        Day_Pass_Rate INT NOT NULL,
                        Monthly_Rate INT NOT NULL,
                        Discount_Rate INT NOT NULL,
                        Reserved_Rate INT NOT NULL
                        ); """

userData_table_sql = """ CREATE TABLE IF NOT EXISTS userData (
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                        ); """

customerInfo_table_sql = """ CREATE TABLE IF NOT EXISTS Customer_Info (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        mobile_no TEXT NOT NULL,
                        vehicle_type TEXT NOT NULL,
                        vehicle_no TEXT NOT NULL,
                        entry_time TEXT NOT NULL,
                        exit_time TEXT,
                        occupied_slotName TEXT 
                        ); """
slotsInfo_table_sql = """ CREATE TABLE IF NOT EXISTS slotsInfo (
                        vehicle_type TEXT PRIMARY KEY NOT NULL,
                        total_slots INT NOT NULL,
                        occupied_slots INT,
                        free_slots INT
                        ); """

####################################################################################3
def create_connection(db_file, create_table_sql):
    """ create a database connection to the SQLite database 
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        with sqlite3.connect(db_file) as connection:
            create_table(connection, create_table_sql)
        return connection
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
     """
     
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def addRate_of_Parking(Vehicle_Type,Parking_No,Total_slots,Hourly_Rate,Day_Pass_Rate,Monthly_Rate,Discount_Rate,Reserved_Rate):
    #list_data = [Vehicle_Type,Parking_No,Total_slots,Hourly_Rate,Day_Pass_Rate,Monthly_Rate,Discount_Rate,Reserved_Rate]
    conn = create_connection(database, addData_table_sql)
    cursor = conn.cursor()
    query = ("INSERT INTO addData_table VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
    data = cursor.execute(query,(Vehicle_Type,Parking_No,Total_slots,Hourly_Rate,Day_Pass_Rate,Monthly_Rate,Discount_Rate,Reserved_Rate))
    #print(list_data)
    conn.commit()
    if data:
        logger.info(f"{Vehicle_Type} data added in DB Successfully")
        return True
    else:
        return False
def viewData_byCategory(vehicle_type):
    conn = create_connection(database, addData_table_sql)
    cursor = conn.cursor()
    query = ("SELECT * FROM addData_table WHERE Vehicle_Type=?")
    cursor.execute(query, (vehicle_type,))
    result = cursor.fetchall()
    return result

def updateData_byCategory(vehicle_type, v1,v2,v3,v4,v5,v6,v7):
    conn = create_connection(database, addData_table_sql)
    cursor = conn.cursor()
    query = """ UPDATE addData_table
                SET Parking_No = ?,
                    Total_slots = ?,
                    Hourly_Rate = ?,
                    Day_Pass_Rate = ?,
                    Monthly_Rate = ?,
                    Discount_Rate = ?,
                    Reserved_Rate = ?
                    WHERE Vehicle_Type = ? """
    data = (v1,v2,v3,v4,v5,v6,v7,vehicle_type)
    cursor.execute(query,data)
    conn.commit()
    result = cursor.fetchall()
    logger.info(f"{vehicle_type} with data:{data} updated in DB")  
    return result            

def deleteData_byCategory(vehicle_type):
    conn = create_connection(database, addData_table_sql)
    cursor = conn.cursor()
    query = ("DELETE FROM addData_table WHERE Vehicle_Type=?")
    cursor.execute(query, (vehicle_type,))
    conn.commit()

def view_addData_Table():
    conn = create_connection(database, addData_table_sql)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM addData_table")
    result = cursor.fetchall()
    print(result)
    return result
def get_Added_Vehicles():
    conn = create_connection(database, addData_table_sql)
    cursor = conn.cursor()
    cursor.execute("SELECT Vehicle_Type FROM addData_table")
    result = cursor.fetchall()
    print(result)
    return result

def add_Customer_Info(name, mobile_no, vehicle_type, vehicle_no, entry_time, exit_time, occupied_slotName):
    conn = create_connection(database, customerInfo_table_sql)
    cursor = conn.cursor()
    #total_rows = cursor.execute("SELECT COUNT(*) FROM customerInfo")
    params = (name, mobile_no, vehicle_type, vehicle_no, entry_time, exit_time, occupied_slotName)
    
    query = ("INSERT INTO Customer_Info (name, mobile_no, vehicle_type, vehicle_no, entry_time, exit_time, occupied_slotName) VALUES (?, ?, ?, ?, ?, ?, ?)")
    data = cursor.execute(query, params)
    conn.commit()
    if data:
        logger.info(f"Customer with data:{params} added to DB")
        return True
    else:
        return False
   

def view_Customer_Info():
    conn = create_connection(database, customerInfo_table_sql)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customer_Info")
    result = cursor.fetchall()
    print(result)
    return result

def view_CustomerInfo_byCatogory(vehicle_type):
    conn = create_connection(database, customerInfo_table_sql)
    cursor = conn.cursor()
    query = ("SELECT occupied_slotName FROM Customer_Info WHERE vehicle_type = ?")
    cursor.execute(query, (vehicle_type,))
    result = cursor.fetchall()
    print(result)
    return result

def delete_AllCustomerS_Info():
    conn = create_connection(database, customerInfo_table_sql)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Customer_Info")
    conn.commit()
    print(f"Deleted total {cursor.rowcount} records from Customer_Info")

def delete_Customer_Info(cust_id):
    conn = create_connection(database, customerInfo_table_sql)
    cursor = conn.cursor()
    query = "DELETE FROM Customer_Info WHERE ID = ?"
    cursor.execute(query, (int(cust_id),))
    conn.commit()
    logger.info(f"Customer with ID:{cust_id} deleted from DB")

'''def get_customerID():
    conn = create_connection(database, customerInfo_table_sql)
    cursor = conn.cursor()
    cursor.execute('SELECT max(ID) FROM Customer_Info')
    max_id = cursor.fetchone()[0]
    return max_id'''

def get_customerID(): # get last insert row ID (Autoincremented Value)
    conn = create_connection(database, customerInfo_table_sql)
    cursor = conn.cursor()
    cursor.execute('SELECT ID from Customer_Info order by ID DESC limit 1')
    max_id = cursor.fetchone()[0]
    return max_id
def main():
    pass
    #deleteData_byCategory("Bus")
    
    #view_addData_Table()
    #view_Customer_Info()
    
if __name__ == '__main__':
    main()