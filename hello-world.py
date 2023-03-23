"""
Your module description
"""
# print("hello World")
# Variables declared here
# string_to_print = "Variable a"
# print("string_to_print")
# int_to_print = 10
# print(int_to_print)
# # print("10")

# intVar = 10
# charvar = "Charlie"
# boolVar = True
# floatVar = 100.50

# print(type(intVar), intVar)
# print(type(charvar), charvar)
# print(type(boolVar), boolVar)
# print(type(floatVar), floatVar)
#-------------------------------------

# apples = 2
# oranges = 4
# apples = oranges
# print(apples)

# -------------------------------
#Lists [Lists are mutable - they can be changed]

# class_roster = ["Shravani","Samira","Prabhjort", "a", "b", "c", "c"] 
# test_scores = [86,93,80]


# print(class_roster) 
# print(test_scores)

# print("class_roster is a type of ", type(class_roster))
# print("Printing first element of class_rooster: ", class_roster[2])


#-----------------------------
#loop thru lists

# for xyz in class_roster: 
#     print(xyz)
# print()
# for score in test_scores: 
#     print(score)
# print()

#-----------------------------
# add new elements to list

# class_roster.append('Charlie')
# for student in class_roster: 
#     print(student)
# print()

# class_roster.insert(3,"Natacha")
# for student in class_roster: 
#     print(student)

# update a list element

# print(class_roster[1])
# class_roster[1]= "Freddie"
# print(class_roster[1])
# print(class_roster)

# -------------------------------
# Tuples (Tuples are immutable - they can NOT be changed)
# Tuples are indexed ( starting with an index value of 0)
# Tuples allow duplicate values
# Tuples are ordered - and that order cannot change

# class_rosterT = ("Shravani","Samira","Prabhjort",  "pear", "banana", "apple",)

# print("Tuple students ", class_rosterT) 


# class_rosterL = ["Shravani","Samira","Prabhjort", "Shravani"]
# print("List students ", class_rosterL) 

# print("class_roster is a type of ", type(class_rosterT))
# print(len(class_rosterT))
# print("Printing first element of class_rooster: ", class_rosterT[-1])


# for student in class_rosterT:
#     print(student)
    
# # Is this a touple?
# thistuple = ("apple",)
# print(type(thistuple))

# # NOT a tuple
# thistuple = ("apple")
# print(type(thistuple)) 

# tuple1 = ("abc", 34, True, 40, "male")
# for item in tuple1:
#     print("this is a:", item, " of ", type(item))


# Tuples are immutable - so you cannot change them once they are created
# but there is a workaround  ;-)
# turn it into a list, change the list and turn it back into a tuple
# for this we need to use a programming language 'thing' called a constructor.
# list() and tuple() are examples of constructors
# Definition of Constructor
# object-oriented programming
# In class-based, object-oriented programming, a constructor is a special type of subroutine 
# called to create an object. It prepares the new object for use, often accepting arguments that 
# the constructor uses to set required member variables.

# x = ("apple", "banana", "cherry")
# print("here x is the original tuple", x, type(x))
# y = list(x)
# print("Now it is a ",type(y))
# y[1] = "kiwi"
# x = tuple(y)
# print("here x is a " , type(x))
# print(x) 

# unpacking - yesterday Mervis (I think...) asked about this

# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)


# more loops using indexes

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1 
# print("im done now")
# -----------------------------
# Dictionaries {}
# A dictionary is ordered, changable and do not allow duplicates
# dictionaries store data in key:value pairs


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# print(thisdict["brand"])

# duplicate values will overwrite existing values
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "brand": "BMW"
# }
# print(thisdict)

# print(thisdict["brand"])

# # dicts allow all datatypes:

# thisdict =	{
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# } 

# print(thisdict)

#  Just like you can use the list and the tuple constructors, there is a dict constructor
# this can be used to create a dictionary

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict) 
# print(thisdict["name"])


# ---------------------------------------------------
# working with files

# # Files

# print("Working with Files")
# f = open('python1','w')
# f.write('Hello from Python!!\n')
# f.write('Working wih files is easy...\n')
# f.write('It is cool ...')
# f.close


# print("Reading file")
# f=open('python1','r')
# line1=f.readline()
# line2=f.readline()
# line3=f.readline()
# print('-----')
# print(line1, end='')
# print(line2, end='')
# print(line3, end='')
# f.close()
# # ##

# f=open('python1','r')
# i=0
# for line in f:
#     print(i,":", line, end='')
#     i=i+1
# f.close()

# # ##
# f=open('python1','r')
# l=[line.upper() for line in f]
# f.close()
# print(l)
# ##
# f=open('python1','r')
# try:
#     for line in f:
#         print(line, end='')
# finally:
#     f.close()
#
# with open('python1','r') as f:
#     print("Last example")
#     for line in f:
#         print(line, end='')




# ---------------------------------
# Conditional logic
#

# --- IF statements
#
# a = 200
# b = 33
# if b < a:
#   print("b is greater than a")
# #elif a == b:
# #  print("a and b are equal")
# else:
#   print("a is greater than b")
  
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

# x = 11

# if x > 10:
#   print("Above ten,")
# elif x == 11:
#     print("but not above 20.") 
# else:
#     print("it is equal to 10!")

# names = ["charlie", "natacha", "kåre"]

# for name in names:
#     newName = name.capitalize()
#     print(newName)
    
# for name in names:
#     newUpper = name.upper()  
#     print(newUpper)
    
#     name.lower()
##
# While loops
#

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# i = 1
# while i < 6:
#   if i == 3:
#     break
#   print(i)
#   i += 1 


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
# #   if x == "banana":
# #     break
#   print(x)


# #var_1 = “this is a word set of double quotes”
# var_2 = "this is a word set of double quotes"
# msg1 = "I’m a message" , "more stuff"
# print(msg1)
# msg2 = "I’m a message" + " " + "more stuff"
# print(msg2)


# for x in "banana":
#   print(x)
# ---------------------------------
# Functions

# def add_3(x):
#   y = x + 3
#   return y
  
# print(add_3(4))


# def greetuser(): 
#     print("Hello there!")
    
# greetuser()

# def greet_userP(name): 
#     print("Hello " + name)
# greet_userP("Sam")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Mickey", "Mouse") 

# def my_function(fname, lname):
#   print(str(fname) + " " + str(lname))

# my_function("lastname", "firstname") 

# If you don't know HOW many arguments will arrive... *in front of the arg name
# def my_function(*kids):
#   print("The youngest child is " + kids[-1])

# my_function("Emil", "Tobias","a", "b", "c", "one more not youngest kid", "Linus") 

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3, end='')
#   print("child 2 is " + child2 + " and child 1 is " + child1)
#   print("child 2 is " + child2,  end='')
#   print("child 1 is " + child1)

# my_function(child3 = "Linus", child2 = "Tobias",  child1 = "Emil" ) 

#default parameter value
# def my_function(country = "Denmark"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil") 

# parameter is a list
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)
# dinner = ("Chilli Con Carne", "BBQ", "Spinach")
# my_function(dinner)

# def my_function(x):
#   return 5 * x

# print(my_function(3))  # called with 3 as a param value
# print(my_function(5))
# print(my_function(9)) 


# Functions can call themselves:
# Recursion is the process of a function calling itself from within its own code. 
# You can think of it as another way to accomplish a looping construct. 
# The recursion pattern appears in many scenarios in the real world, and we’ll cover
# some examples of recursion in Python here. 
# A recursive function just keeps calling itself until it has completed the problem at hand. 
# That brings up a good point, and that is to make sure that your recursive function actually 
# terminates and returns at some point. Otherwise, the recursive function will run forever, 
# exhaust your memory, and crash your computer. Having a step where the function actually 
# finishes is known as a breaking condition.

# The Fibonacci sequence happens everywhere in the world and in all of nature. 
# The sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on is the Fibonacci sequence. 
# Each successive number is found by adding up the two numbers before it. 
# Here is how we compute the Fibonacci sequence in Python using a recursive function.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = 14

print('Fibonacci sequence:')
for i in range(number):
    print(fibonacci(i))



# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# ------------------------------------------
# Maths in python
#
# import math

# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print("min number in x list is: ", x)
# print("max number in y list is: ", y) 

# x = pow(4, 3)
# print(x) 

# x = math.sqrt(64)
# # print(x) 

# absolute = -5.999 
# floor_test = 198.42
# result1 = math.fabs(absolute) 
# result2 = math.floor(floor_test)
# print(result1, " is the absolute value of ", absolute) 
# print(result2, " is the floor of ", floor_test)

# def div_by_zero_try(number):
#     try:
#         value = 5 / number
#     except ZeroDivisionError:
#         print('Divide by zero error')
#         value = 9999999
#     return value
    
# def div_by_zero(number):
#     value = 5 / number
#     return value
  

# print(div_by_zero_try(2))
# print(div_by_zero_try(0))
# print(div_by_zero_try(2))
# #print(div_by_zero(0))
# print(div_by_zero(20))
    
#print(div_by_zero(0))




# ------------------------------------------
# OS in python
#


# import os 

# dirs = os.listdir() 
# print(dirs)
# print()
# os.mkdir("newFolder") 
# dirs = os.listdir() 
# print(dirs)
# print()
# os.rmdir("newFolder") 
# dirs = os.listdir() 
# print(dirs)
# user = os.getlogin()
# print(user)


# Json example from book - does not work
# ------------------------------
# import json
# filename = "userName.json"
# name = ''
# # print(filename)
# # Check for a history file 
# try:
#     with open(filename, 'r') as r: # Load the user's name from the history file 
#         name = json.load(r)
# except IOError: 
#     print("First-time login")
#     # If the user was found in the history file, welcome them back 
# if name != "": 
#     print("Welcome back, " + name + "!")
# else: # If the history file doesn't exist, ask the user for their name
#     name = input("Hello! What's your name? ") 
#     print("Welcome, " + name + "!")
#   # Save the user's name to the history file 
# try:
#     with open(filename, 'w') as f: 
#         json.dump(name, f)
# except IOError: 
#      print("There was a problem writing to the history file.")


# import json

# try:
#     # Try to open the JSON file
#     with open('data1.json', 'r') as file:
#         # Load the data from the file
#         data = json.load(file)  #read
#         print(f"Welcome back, {data['name']}!")
        
# except IOError:
#     # If the file does not exist, ask the user for a name
#     name = input("Please enter your name: ")
#     data = {"name": name}
    
#     # Write the data to a new JSON file
#     with open('data1.json', 'w') as file:
#         json.dump(data, file)   #write
#         print(f"Welcome, {name}! Your name has been saved.")

#---------------
# import os
# import json

# # Check if the file exists
# if os.path.isfile('data.json'):
#     # Open the JSON file
#     with open('data.json', 'r') as file:
#         # Load the data from the file
#         data = json.load(file)
#     # Print the data
#     print(data)
# else:
#     # Ask the user for their name
#     name = input('Enter your name: ')
#     # Create a dictionary with the user's name
#     data = {'name': name}
#     # Open the JSON file for writing
#     with open('data.json', 'w') as file:
#         # Write the data to the file in JSON format
#         json.dump(data, file)
        
# ---------------------------------------
# pip installer
# --------------------------------------
# The requests library is the de facto standard for making HTTP requests in Python. 
# It abstracts the complexities of making requests behind a beautiful, simple API so 
# that you can focus on interacting with services and consuming data in your application.
#  https://realpython.com/python-requests/


# in a terminal window run 
# pip show requests
# pip install requests 

# f-strings - they are your friend.  :-)

# name = "Eric"
# age = 74
# shoesize = 9
# print(f"Hello, {name}. You are {age}. And your shoesize is {shoesize}" )
# print("Hello, {name}. You are {age}.And your shoesize is {shoesize}")
# print("Hello", name,". You are", age, ". And your shoesize is", shoesize, end='')

#------------------------------
# debugging
#-------------------------------

# # # Python program with 2 errors 
# var = "Double Value" 
# sumvalue = (var , 4)


# def dosomething(valuetocheck): 
#     if valuetocheck > 4: 
#         print("Bad indent")

# dosomething(5)

# def logage(age):
#     assert (age <= 0), "Age must be greater than 0"
#     if age == 5:
#         print("yay")

# logage(0)
# logage(5)

#print(var, 4)

# Ask the user for a value and confirm the supplied value is greater than 0
# def checkvalue(valuetocheck): 
#     assert (type(valuetocheck) is int), "You must enter a number."
#     assert (valuetocheck > 0), "Value entered must be greater than 0" 
#     if valuetocheck > 4: 
#         print("Value is greater than 4")

# var = int(input("Enter a number greater than 0: ")) 
# checkvalue(var)


# import os

# def new_user():
#     confirm = "N"
#     while confirm != 'Y':
#         username = input("Enter the username ")
#         print("use the username '" + username + "'? Y/N")
#         confirm = input().upper()
#     os.system("sudo adduser " + username)
    
# def del_user():
#     confirm = "N"
#     while confirm != 'Y':
#         username = input("Enter the username ")
#         print("use the username '" + username + "'? Y/N")
#         confirm = input().upper()
#     os.system("sudo userdel " + username)
    
# #new_user()
# del_user()