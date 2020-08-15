#Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()

print(x)

#Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#Create Date Object:
import datetime

x = datetime.datetime(2020,5,25)

print(x)


#Display the name of the month:

import datetime
x = datetime.datetime(2018,11,24)

print(x.strftime("%c"))


#Day of month 01-31

import datetime

x = datetime.datetime.now()

print(x.strftime("%d"))

