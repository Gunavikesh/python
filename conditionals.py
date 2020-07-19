
                     #CONDITIONALS AND BOOLEANS


language = 'python'
if language == 'python':
    print('language is python')
else:
    print('no match')
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

#else condition

language = 'c'
if language == 'python':
    print('language is python')
else:
    print('no match')


#elif
language = 'python'
if language == 'python':
    print('language is python')
elif language == 'java':
    print('language is java')
elif language == 'java script':
    print('language is java script')
else:
    print('no match')


#and
#or
#not

user = 'Admin'
logged_in = True

if user =='Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')

user = 'Admin'
logged_in = False

if user =='Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')

#or
    
user = 'Admin'
logged_in = True

if user =='Admin' or logged_in:
    print('Admin page')
else:
    print('Bad creds')


user = 'Admin'
logged_in = False

if user =='Admin' or logged_in:
    print('Admin page')
else:
    print('Bad creds')



#not
    
user = 'Admin'
logged_in = True

if  not logged_in:
    print('please login')
else:
    print('welcome')

a = [1, 2, 3]# a and b is not equal both are different
b = [1, 2, 3]# because of id's are different
print(id(a))
print(id(b))
print(a is b)
print(id(a) != id(b))



# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.


condition =' '

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')



condition = True

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')









    

