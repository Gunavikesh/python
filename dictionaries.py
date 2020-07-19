                                       #DICTIONARIES

# PRINTING OF DICTIONARY
student = {'name':'guna','age':20,'courses':['btech','engineerung']}
print(student['courses'])
# searching of elements using get()

student = {'name':'guna','age':20,'courses':['btech','engineerung']}
print(student.get('phone'))
# adding of elemnts in dictionary
student['phone'] = '5454545'
print(student.get('phone','not found'))

student['name']='vikesh'
print(student)


#UPDATE()
student.update({'name':'jhon','age':23,'phone':'2223355'})
print(student)

#del()
del student['courses']

#pop()
age = student.pop('age')
print(student)

# len()
student = {'name':'guna','age':20,'courses':['btech','engineerung']}
print(len(student))

#items()
student = {'name':'guna','age':20,'courses':['btech','engineerung']}
print(student.items())


#printing of elements using for loop

student = {'name':'guna','age':20,'courses':['btech','engineerung']}
for key,values in student.items():
    print(key,values)
    
