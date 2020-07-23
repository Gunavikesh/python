                                  #FUNCTIONS


#Function Parameters    
def myfunc(x,y):
    if x > y:
        print(x,' is greater than', y)
    elif x == y:
        print(x, 'equals to', y)
    elif x < y:
        print(x,' is less than', y)
    else:
        print(x,' is not equals to', y)
myfunc(5,5)

#LOCAL VARIABLES

x = 'python'
def mylang(x):
    print(x,'is my favourite language')
mylang(x)


y = 5
def mynum(y):
    y =3
    print('changed local y to',y)
mynum(y)
print('num is stil',y)

# GLOBAL VARIABLE
language = 'python'

def mylang():
    global language
    
    print(language,'is my favourite programming language')
    language = 'java'
    print(' global language is changed to',language)
mylang()
print(language,'is language')

#defualt arguments

def say(message, times=1):
    print(message * times)
say('Hello')
say('World', 5)


#keyword arguments
def name(a, b=3, c=100):
    print('a is ',a, 'b is',b, 'c is',c)
name(2,3)
name('python','java','c++')


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
courses =['math', 'art']
info = {'name': 'guna','age':33}
student_info(*courses,**info)


# return
def strings(a,b):
    if len(a)>len(b):
        return a
    else:
        return b
print(strings('python','java'))
        
