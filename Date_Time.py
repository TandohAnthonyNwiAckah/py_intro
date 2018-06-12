# Working with Date And Time.
import datetime

myDate = datetime.date(2018,6,9)

print(myDate)

print(myDate.year)

print(myDate.month)

print(myDate.day)


#Day-name,Month-name,Day-name,Year
print(myDate.strftime("%A,%B,%d,%Y"))