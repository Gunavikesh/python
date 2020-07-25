                                                   #MODULES

#Making & Importing of Your Own Modules
'''first we have to write a python file then save it as .py module in same file. '''
import mymodule
mymodule.nums(6,5)

#importing of random module
import random
courses = ['math','physics','history','compsci']
random_course = random.choice(courses)
print(random_course)


#program for random numbers
import random
print(random.randint(0,4))

#importing of math module
import math
rads = math.radians(180)
print(math.sin(rads))

from math import factorial,sqrt,exp

b = sqrt(4)
c = factorial(3)
print(c)
print(b)
#power of a number
a = pow(2,5)
print(a)

#importing of datetime
import datetime
import calendar

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))


#importing of current work directory
import os
print(os.getcwd())
print(os.__file__)

