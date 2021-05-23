from datetime import datetime, timedelta
from log_decorator import _generate_log
from Parking_All_Functions import *
list1 = ['Slot 1', 'Slot 2']
if 'Slot 1' in list1:
	print("Hiiii")

dt_now = datetime.now()
one_day = timedelta(days=1)
print(one_day)
next_day = dt_now + one_day
print(dt_now)
exit = next_day.strftime("%d-%m-%Y %I:%M %p") 
exit = "27-06-2020 09:04 AM"
#exit = dt_now.strftime("%d-%m-%Y, %I:%M %p")
       
#fn = r"C:\Users\anku\AppData\Roaming\Sublime Text 3\Packages\User\Parking_Management\log_file.txt"
logger = _generate_log()
logger.info("This is an practise message")
charges = get_Parking_Charges('Bike', 1, exit)
print(charges)



        #fmt = "%d-%m-%Y %I:%M" # The format 

'''
import datetime

today = datetime.date.today()
print 'Today    :', today

one_day = datetime.timedelta(days=1)
print 'One day  :', one_day

yesterday = today - one_day
print 'Yesterday:', yesterday

tomorrow = today + one_day
print 'Tomorrow :', tomorrow

print 'tomorrow - yesterday:', tomorrow - yesterday
print 'yesterday - tomorrow:', yesterday - tomorrow'''