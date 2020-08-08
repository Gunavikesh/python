# PYTHON INHERITANCE

'''*Inheritance allows us to define a class that inherits all the methods and properties from another class.

*Parent class is the class being inherited from, also called base class.

*Child class is the class that inherits from another class, also called derived class.'''

#PARENT CLASS
class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        

    def name(self):
        print(self.firstname,self.lastname)
      

x = person("Guna","vikesh Sana")
x.name()



#CHILD CLASS
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        

    def mydetails(self):
        print(self.firstname,self.lastname)
       
        
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x = Student("Guna","vikesh Sana")
x.mydetails()


#Use the super() Function


class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        

    def mydetails(self):
        print(self.firstname,self.lastname)
       
        
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

x = Student("Guna","vikesh Sana")
x.mydetails()

#Add properties
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        

    def mydetails(self):
        print(self.firstname,self.lastname)
       
        
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year = year

x = Student("Guna","vikesh Sana",2020)
x.mydetails()
print(x.year)

#add methods
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        

    def mydetails(self):
        print(self.firstname,self.lastname)
       
        
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year = year

    def myfun(self):
        print("welcome" ,self.firstname,self.lastname,"year of",self.year)

x = Student("Guna","vikesh Sana",2020)
x.myfun()

#example program


class Objects:
    def __init__(self,otype,ocost):
        self.objecttype = otype
        self.objectcost = ocost

    def myfav(self):
        print(self.otype,self.ocost)

class Toys(Objects):
    def __init__(self,otype,ocost):
        Objects.__init__(self,otype,ocost)

    def liked(self):
        print("My favourite toy is ",self.objecttype,"It's cost is ",self.objectcost)

class Games(Objects):
    def __init__(self,otype,ocost):
        Objects.__init__(self,otype,ocost)

    def loved(self):
        print("My favourite game is ",self.objecttype,"It's size is ",self.objectcost)

x = Toys("Teddy",2000)
y = Games("pubg","2.00GB")

x.liked()
y.loved()
        



