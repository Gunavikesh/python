                            #ARRAYS
'''AN ARRAY IS USED TO COLLECT DATA OF ELEMENTS'''


#Get the value of the  array item:

fruits = ['apple','banana','cherry','orange']
print(fruits[1])

#Modify the value of the first array


fruits = ['apple','banana','cherry','orange']
fruits[0] = 'mango'
print(fruits)

#length of an array
fruits = ['apple','banana','cherry','orange']
print(len(fruits))


#looping of an array
fruits = ['apple','banana','cherry','orange']

for x in fruits:
    print(x)
#Adding of one or more elements in an array
fruits = ['apple','banana','cherry','orange']
fruits.append('watermelon')
print(fruits)

fruits = ['apple','banana','cherry','orange']
fruits.insert(1,'mango')
print(fruits)


# remaoving of an element from an array
#1.pop()
fruits = ['apple','banana','cherry','orange']
fruits.pop(1)
print(fruits)


#2.remove()

fruits = ['apple','banana','cherry','orange']
fruits.remove('apple')
print(fruits)

#sorting of array elments

x = [2,6,5,4,0,1,8,7,9,3]
x.sort()
print(x)


# reversing of array elements

fruits = ['apple','banana','cherry','orange']
fruits.reverse()
print(fruits)

#clearing of an array
fruits = ['apple','banana','cherry','orange']
fruits.clear()
print(fruits)








