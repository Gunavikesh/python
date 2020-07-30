#oops in python
#class

class person:
    pass #an empty block

p = person()
print(p)

#CREATE AN OBJECT x1
class Num:
    x = 4
x1 = Num()
print(x1.x)

#METHODS



class Student:
    pass
Student_1 = Student()
Student_2 = Student()
print(Student_1)
print(Student_2)

Student_1.first = 'Nandan'
Student_1.last = 'Mallela'
Student_1.email = '189y1a0476@ksrmce.ac.in'


Student_2.first = 'Gunavikesh'
Student_2.last = 'Sana'
Student_2.email = '189y1a04c3@ksrmce.ac.in'


print(Student_1.email)
print(Student_2.email)

#The __init__() Function

class person:
    def __init__(self,name,age, email):
        self.name = name
        self.age =  age
        self.email = email
p1 = person('Gunavikesh',20,'gunavikeshsana345@gmail.com')
print(p1.name)
print(p1.email)

#Object method
class person:
    def __init__(self,name,age, email):
        self.name = name
        self.age =  age
        self.email = email
    def myfunc(self):
        print('Hi! My name is '+self.name)
p1 = person('Gunavikesh',20,'gunavikeshsana345@gmail.com')
p1.myfunc()

class person:
    def say_hello(self):
        print('hello,how are you?')

p = person()
p.say_hello()


# The Self Parameter
class Object:
    def __init__(myobject,name,quantity):
        myobject.name = name
        myobject.quantity = quantity
        
    def myfunc(say):
        print('objects are',say.quantity, say.name)
        
o1 = Object("laptop's",2)
o1.myfunc()


#Modify object properties

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("My age is",self.age)

p1 = Person("John", 36)

p1.age = 40
p1.myfunc()















