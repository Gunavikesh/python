                            #LISTS


"""List is a collection which is ordered and changeable. Allows duplicate members.
A list can be defined as ['python','java','html','oracle']"""

courses = ['python','java','oracle','html']
print(courses[1])
print(courses[:3])

#list.append():- To add an item
courses.append('css')
print(courses)


#extend()
list_1 = ['history','math','physics','compsci']
list_2 = ['art','education']
list_1.extend(list_2)
print(list_1)

list_1.append(list_2)
print(list_1)

#remove()

list_1 = ['history','math','physics','compsci']
list_1.remove('history')
print(list_1)

#pop()# it removes last item
list_1 = ['history','math','physics','compsci']
list_1.pop()
print(list_1)

list_1 = ['history','math','physics','compsci']
popped = list_1.pop()
print(popped)
print(list_1)

#reverse()
list_1 = ['history','math','physics','compsci']
list_1.reverse()
print(list_1)

#sort()
courses = ['python','java','oracle','html']
nums = [1,3,6,4,9,2]
courses.sort()
nums.sort()
print(courses)
print(nums)


courses.sort(reverse = True)
nums.sort(reverse = True)
print(courses)
print(nums)

#sorting the list without altering
courses = ['python','java','oracle','html']
nums = [1,3,6,4,9,2]
sorted_courses = sorted(courses)
sorted_nums = sorted(nums)
print(sorted_courses)


#min()& max()
nums = [1,3,6,4,9,2]
print(min(nums),max(nums))
#sum()
print(sum(nums))
#bin(),hex(),oct()
print(bin(10))
print(hex(2020))
print(oct(45))


#index array
courses = ['python','java','oracle','compsci','html']
print(courses.index('compsci'))

#print(courses.index('art'))

# finding of elements by using "in"
print('art'in courses)

print('math'in courses)

#printing elemnts by using for loop
courses = ['python','java','oracle','html']
for item in courses:
    print(item)

#enumerate()
for index,courses in enumerate(courses):
    print(index,courses)

# enumerate starting from 1
for index,courses in enumerate(courses,start=1):
    print(index,courses)

# joining of elements in the list with "-" using join()

courses = ['python','java','oracle','html']
courses_str='-'.join(courses)
print(courses_str)


#split()
# printing the as usual
courses = ['python','java','oracle','html']
courses_str='-'.join(courses)
new_list = courses_str.split('-')
print(courses_str)
print(new_list)

#LIST CONSTRUCTOR
thislist = list(("apple", "banana", "cherry"))
print(thislist)

                                    #TUPLES

"""A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
it is denoted by ('history','math','physics','compsci')"""


'''They are two types 
1..MUTABLE (lists)
2..IMMUTABLE (tuples)'''



#MUTABLE
list_1 = ['history','math','physics','compsci']
list_2 = list_1
print(list_1)
print(list_2)
list_1[1] = 'biology'
print(list_1)
print(list_2)


#IMMUTABLE

#MUTABLE
tuple_1 = ('history','math','physics','compsci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
'''tuple_1[1] = 'biology'
print(tuple_1)
print(tuple_2)'''
# Tupple won't allows assigining of an element.So, it is called immutable


thistuple = tuple(["apple", "banana", "cherry"])
print(thistuple)

#INTERSECTION

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
new_courses = {'History', 'Math', 'Physics', 'design','art'}
print(cs_courses .intersection(new_courses))
#union
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
new_courses = {'History', 'Math', 'Physics', 'design','art'}
print(cs_courses .union(new_courses))
#difference
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
new_courses = {'History', 'Math', 'Physics', 'design','art'}
print(cs_courses .difference(new_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()




