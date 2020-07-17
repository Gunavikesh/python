# python
python startup
                                 #day-1
                                #STRINGS

print("hello world")#printing a message

#by calling a variable
message = 'hello Gunavikesh'
print(message)

#length of a string
print(len(message))

#printing of messages by calling a number of array
print(message[4])

#printing of letters at certain range
print(message[0:5])

#negative indexing
print(message[-1:-5])
#slicing
print(message[0:])
print(message[:7])

#upper case strings
print(message.upper())

#lower case strings
print(message.lower())

#string count()
print(message.count('hello'))

print(message.count('l')) #it displays number of l's in a message

#string find()
print(message.find('universe'))

print(message.find('hello'))

#string replace()
message = "Hello Gunavikesh"
new_message = message.replace('Hello','Sana')
print(new_message)

#string concatenation()
greeting = 'hello'
name = 'guna'
message = greeting + ','+name + '.welcome!'
print(message)

Message = '{}.{}.welcome!'.format(greeting,name)
print(Message)

#f strings
greeting = 'hello'
name = 'guna'

message = f'{greeting},{name.upper()}.welcome!'
print(message)
#String Format:-Use the format() method to insert numbers into strings:
age = 20
txt = "My Name is Vikesh,and Iam {}"
print(txt.format(age))

#string dir()
print(dir(name))

#multiline strings
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#strip() is  method removes any whitespace from the beginning or the end:
a = " Hello,   World! "
print(a.strip())
#strin split
a = "guna vikesh sana"
print(a.split())

#Check String by using 'in'
txt = "The rain in Spain stays mainly in the plain"
x = "spain" in txt
print(x)

#Check String by using 'not'
txt = "The rain in Spain stays mainly in the plain"
x = "spain" not in txt
print(x)

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
