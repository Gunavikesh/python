                                        #LOOPS AND ITERATIONS

# FOR LOOP
'''A for loop is used for iterating over a sequence
(that is either a list, a tuple, a dictionary, a set, or a string).'''


A = ['apple', 'banana', 'mango', 'watermelon', 'orange']
for fruits in A:
    print(fruits)


# for loop using break statement
'''break: With the break statement we can stop the loop before it has looped through all the items'''
    
A = [1, 2, 3, 4, 5]
for nums in A:
    if nums == 4 :
        break
    print(nums)



A = ['apple', 'banana', 'mango', 'watermelon', 'orange']
for fruits in A:
    if fruits == 'mango' :
        print(fruits)
        break



# for loop using CONTINUE statement
'''With the continue statement we can stop the current iteration, and continue with the next:'''
A = ['apple', 'banana', 'mango', 'watermelon', 'orange']
for fruits in A:
    if fruits == 'mango' :
         continue
    print(fruits)




A = [1, 2, 3, 4, 5]
for nums in A:
    if nums == 4 :
         print(nums)
         continue
        


#NESTED FOR LOOP
        
adj = ["RED", "WHITE", "BLACK"]
cars = ["BMW", "AUDI", "MERCIDES"]

for x in adj:
  for y in cars:
    print(x, y)

   
nums = [1, 2, 3, 4, 5]
for num in nums :
    for letter in 'a':
        print(num,letter)


# range()
for i in range(10):
    print(i)


for i in range(1,11):
    print(i)


#WHILE LOOP:With the while loop we can execute a set of statements as long as a condition is true.

    
x = 0

while x < 10:
    print(x)
    x += 1


x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1




    i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result

