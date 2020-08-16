#Python JSON
'''Json is a syntax for storing and exchanging of data
** JSON is text , written with Javascript object notation'''
# python has built in package called json,which can be used to work with JS"On data

#EXAMPLES

'''Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.'''

import json

#some json
x = '{"name":"Gunavikesh","age":20,"course":"BTech"}'

# prase x
y = json.loads(x)

#the result is python dictionary:

print(y['name'])


import json

a = '["apple","banana","cherry","dates"]'

b = json.loads(a)

print(a)


# convert from python to json:
import json

#a python object(dict):
x = {"name" : "vikesh",
     "age": 20,
     "city":"Kadapa"
     }

#convert into json:
y = json.dumps(x)

#the result is a json string:
print(y)

'''You can convert Python objects of the following types, into JSON strings:

*dict
*list
*tuple
*string
*int
*float
*True
*False
*None'''

#convert python objects into JSON strings ,and print the values:


import json

print(json.dumps({"name": "vikesh", "age": 20}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(25))
print(json.dumps(41.22))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#convert a python object containing all the legal data types:

import json
x = {
    "name":"vikesh",
    "age":20,
    "courses":["python","java","HTML","C Language"],
    "married" : False,
    "divorced" : False,
    "children" : None,
    "cars" : [{"model" : "ferari 812","mileage":"9.0kmpl"},
              {"model" : "BMW Z3","mileage":"10.37kmpl"}]
    
     }

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

'''Format the Result
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result:'''

# 1)Use the indent parameter to define the number of indents:

import json
x = {
    "name":"vikesh",
    "age":20,
    "courses":["python","java","HTML","C Language"],
    "married" : False,
    "divorced" : False,
    "children" : None,
    "cars" : [{"model" : "ferari 812","mileage":"9.0kmpl"},
              {"model" : "BMW Z3","mileage":"10.37kmpl"}]
    
     }
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))



#2)Use the separators parameter to change the default separator:
x = {
    "name":"vikesh",
    "age":20,
    "courses":["python","java","HTML","C Language"],
    "married" : False,
    "divorced" : False,
    "children" : None,
    "cars" : [{"model" : "ferari 812","mileage":"9.0kmpl"},
              {"model" : "BMW Z3","mileage":"10.37kmpl"}]
    
     }

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

#Order the Result
'''The json.dumps() method has parameters to order the keys in the result:'''

#Example
'''Use the sort_keys parameter to specify if the result should be sorted or not:'''

x = {
    "name":"vikesh",
    "age":20,
    "courses":["python","java","HTML","C Language"],
    "married" : False,
    "divorced" : False,
    "children" : None,
    "cars" : [{"model" : "ferari 812","mileage":"9.0kmpl"},
              {"model" : "BMW Z3","mileage":"10.37kmpl"}]
    
     }

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))






















