# Working with Date And Time.

import datetime
from datetime import date


  # Get today's date from the date class.
today = date.today()
print ("Today's date is ", today)

myDate = datetime.date(2018,6,9)

print(myDate)

print(myDate.year)

print(myDate.month)

print(myDate.day)


#Day-name,Month-name,Day-name,Year
print(myDate.strftime("%A,%B,%d,%Y"))