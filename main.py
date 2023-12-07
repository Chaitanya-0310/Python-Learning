#? Python_Learning
#
# My_Name = "Chaitanya"
# My_Favourite_Color = "Blue"
# print("My Name is " + My_Name + " and my favourite color is " + My_Favourite_Color)
# import random

#? Mutliple assignment => allows us to assign multiple variables at the same time in one line of code

# raj = 30
# ram = 20
# raju = 23
#
# print(raj)
# print(raju)
# print(ram)
#
# raj, ram , raju =30,20,23
# Name, age, id = "Chaitanya", 21, 3
#
# print(raj)
# print(raju)
# print(ram)
#
# print(Name)
# print(age)
# print(id)

#hello = world
#hi = world
#hellloww = world
#
# hello = hi = 30
#
# print(hello)
# print(hi)
#

#
# # ?  Type casting = convert the data type of a value to another data types
#
# x = 1 #int
# y = 2.0 #float
# z = "3" #string



# print(float(x))
# print(int(y))
# print(int(z))
# print(z)
# print(z*3)
# print(int(z)*3)
#
# !print("X value is "+ x) # gives error --> can only concatenate str with str, here x is a integer value
# !print("Y value is "+ y)# gives error --> can only concatenate str with str, here x is a float value

# !Therefore here we will use typecasting

# print("X value is " + str(x))
# print("Y value is " +  str(y))
# print("Z value is " +  str(z))


#? User Input
#
# EnterName = input("Enter your Name: ")
# EnterAge = int(input("Enter your Age: "))
# EnterHeight = float(input("Enter your Height: "))
# age = input("Enter your age again: ")
#
#! EnterAge += 1 #here it will come an error --> can only concatenate str (not int) to str
#
# print("My name is " + EnterName + " and my age is " + str(EnterAge) + " and my age is is  " + str(age) + " and my height is " + str(EnterHeight))


# ? Math Function

# function
#
# import math
#
# pi = 3.14
#
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(pow(3,3))
# print(math.sqrt(27))
# print(max(1,2,4))
#
# x, y, z = 3,2,4
# print(min(x,y,z))
#

# ? String Slicing => create a substring by extracting elements from another string
# ?                   indexing[] or slice()
# ?                => [start:stop:step]
#
# aRandomString = "Chaitanya Panchal"
# firstName = aRandomString[0:9]  # // or [:9] -> [start:9]
# #*                       [inclusive : exclusive]
#
# lastName = aRandomString[10:] #[10:end]  OR [10:17]
# fullName = aRandomString[:]
# funkyName = aRandomString[0:9:2] #skipping 2 letters
# reversedName = aRandomString[::-1] #used for reversing the Name
#
#
# print(firstName)
# print(lastName)
# print(fullName)
# print(funkyName)
# print(reversedName)


# website = "http://google.com"
# website1 = "http://microsoft.com"
# website2 = "http://amazon.com"
#
# DomainName = slice(7,-4)  #Only difference is of comma
# print(website[DomainName])
# print(website1[DomainName])
# print(website2[DomainName])

#? If Statement => a block of code that will execute if it's condition is true

# Age = int(input("Enter your age =  "))
#
# if age == 100:
#     print("you are a century old")
# elif age >= 18:
#     print("Your are an adult")
# elif age <= 15
#     print("You are a teenager")
# else:
#     print("You are a child")
#

# ? Logical Operators
# ? and, or & not => used to check if two or more conditional statements
#
# if temp>= 0 and temp<=30:
# if temp< 0 or temp>30:
# if not(temp< 0 or temp>30):

# ? while loop
# ?     => a statement that will execute it's block of code as long as it's
# ?        condition remains true

# ? For loop
# ?


# ? Array / List  => used to store multiple items in a single variable
# * can be updated later
#
# fruit = ["Apple","Banana"]
#
# fruit.append("Mango")
# fruit.append("Pineapple")
# fruit.pop()
# fruit.remove("Banana")
# fruit.insert(1,"Chickoo")
# fruit.sort()
# # print(fruit[0])
# # print(fruit)
#
#
# for i in fruit:
#     print(i)
#
#  # ? 2D Array / List
#
# Heelllo = ["Hello","hii"]
# World = ["world", "Worlllddd"]
#
# two_array = [Heelllo,World]
#
# print(two_array[1])
# print(two_array[1][1])


# ? Tuple = Collection which is ordered and unchangeable used to group related data

# student = ("Chaitanya", 21, "Male", 3)
# print(student.count(21))
# print(student.count("Chaitanya"))
# print(student.index("Chaitanya"))
#
# for x in student:
#     print(x)
#
# if "Chaitanya" in student:
#     print("Chaitanya is present")
#

# ? Set
# ? =>    A set is a collection which is unordered, unindexed.
# ?        No duplicate value is allowed
#
# fruits = {"Apple" , "Banana", "Mango", "kiwi"}
# vegetable = {"Tomato", "ladyfinger", "Mango"}
#
# fruits.add("JackFruit")
# fruits.remove("JackFruit")
# fruits.clear()
# fruits.update(vegetable)
# vegetable.update(fruits)
# fruitsAndVege = fruits.union(vegetable)
#
# print(fruits.difference(vegetable))
# print(vegetable.intersection(vegetable))
# print(fruits)
# print(fruitsAndVege)

# ? Dictionary =>  A changable, unordered collection of unique key:value pairs
# ?                 Fast because they use hashing, allow us to access a value quickly
#
#
# capitals = {'India': 'Delhi',
#             'USA' : 'Washington DC',
#             'Russia' : 'Moscow',
#             'China': 'Beijing'}
#
# capitals.update({'Germany': 'Berlin'})
# #
# print(capitals["Germany"])
# print(capitals['India'])
# print(capitals.get('India'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
#
# for key,value in capitals.items():
#     print(key,value)
#
# for x in capitals:
#     print(x)


# ? FUNCTION
# ?         => a block of code which is executed only when it is called

#
# def hello(name,surname):
#     print("Hello" + " " +name +" " + surname )
#
# hello("chaitanya","panchal")



# ? Return Statement => Functions send python values/objs back to the caller
#                     ?  These values/objs are knows as the function's return value





# ? Scope => A region where the variable is recognized
#          ? A variable is only available from inside the region it is created ,A globally and locally scope variable can be created

#
# name = Galu     # Global scope available everywhere inside and outside of the function
#

# def display_name():
#     name = "Chaitanya"  # Local scope availble only inside the function
#     print(name)
#
# display_name()       # Chaitanya
#
# print(name)      # Galu
#
# #* Python follows LEGB (Local->Enclosed->Global->Built-in) sequence
#


# ? *args
# ? parameter that will pack all arguments into a tuple
# ? useful so that a function can accept a varying amount of arguments

# def your_name(first_Name, last_Name):
#     print("Hello " + first_Name +" "+ last_Name)
#
# your_name("Chaitanya", "Panchal")

# * instead of this use *args => args is the common naming convention you can use it any name
# def your_name(*fullname):
#     return fullname
#
# print(your_name("Chaitanya", "Panchal"))
#
# # * else
#
# def add(*digits):
#     sum = 0
#     for i in digits:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,4,5,6))



#  ?   **kwargs = parameter that will pack all arguments into a dictionary
# ?               useful so that a function can accept a varying amount of a keyword arguments
#
# def name(**kwargs):
#     # print("Hello"+" "+kwargs["first_Name"] +" "+kwargs["last_Name"])
#     print("Hello",end=" ")
#     for key,value in kwargs.items():
#         print(value, end=" ")
#
# name(last_Name="Panchal", first_Name="Chaitanya")



# ?  str.format()
# ? Optional method that gives users more control when displaying output

# firstName = "Chaitanya"
# LastName = "Panchal"
# ID = 3
# def name():
    # print("My name is {} and my surname is {} and my id is {}".format("Chaitanya","Panchal",3))
    # print("My name is {} and my surname is {} and "
    #       "my id is {}".format(firstName,LastName,ID))
    #
    # print("My name is {firstName} and my surname is {LastName} and "
    #       "my id is {ID}".format(firstName="Chaitanya",LastName="Panchal",ID=3))
    #
    # print("My name is {0} and my surname is {1} and "
    #       "my id is {2}".format(firstName,LastName,ID))

# name()
#
# name = "chaitanya"
#
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:15}. Nice to meet you".format(name))
# print("Hello, my name is {:<1  5}. Nice to meet you".format(name))
# print("Hello, my name is {:>15}. Nice to meet you".format(name))
# print("Hello, my name is {:^15}. Nice to meet you".format(name))

#
# number = 3.1472
# newNumber = 1000000
#
# print("The number pi is {:.2f}".format(number)) #after point 2 digits
# print("The number pi is {:,}".format(newNumber))
# print("The number pi is {:b}".format(newNumber)) #convert to binary
# print("The number pi is {:o}".format(newNumber))# to octa
# print("The number pi is {:x}".format(newNumber))


# ? RANDOM NUMBER
#
# import random
#
# x=random.randint(1,10)
# print(x)
# y=random.random()
# print(y)
#
# myList = ["Rock","Paper","scissor"]
# Game = random.choice(myList)
# print(Game)
#
# Deck = [1,2,3,4,5,6,7,8,9,"A","K","Q","J"]
# random.shuffle(Deck)
# print(Deck)

# ? Exception Handling
# ? events detected during execution that interupt the flow of a program

# numerator = int(input("Enter the value: "))
# denomenator = int(input("Enter the value: "))
# result = numerator/denomenator
#
# print(result)

# ! But here if i divide 5 with 0 it will give me error which interupts the flow of a program
# ! so here i dont want program to give error rather than that it will print a statement that cant divide with 0
#
# try:
#     numerator = int(input("Enter the value: "))
#     denomenator = int(input("Enter the value: "))
#     result = numerator/denomenator
# except ZeroDivisionError as a:
#     print(a)
#     print("Cannot divide with 0")
# except ValueError as b:
#     print(b)
#     print("cannot divide with string")
# except Exception as c:               # Exception is a standard function for any kind of problem
#     print(c)
#     print("Something went wrong")
# else:
#     print(result)
# finally:
#     print("This is mandatory line")


# ? File Detection
#
# import os
#
# #* Use double back slash in the path
# path = "C:\\Users\\chait\\OneDrive\\Desktop\\NEW2.txt"
# path = "C:\\Users\\chait\\OneDrive\\Desktop\\New folder 2"

# if os.path.exists(path):
#     print("The path exist")
#     if os.path.isfile(path):
#         print("This is a file")
#     elif os.path.isdir(path):
#         print("This is a directory/folder")
#     elif os.path.islink(path):
#         print("This is a link")
#     else:
#         print("Cannot Recognize")
# else:
#     print("The path doesnt exist")

# ? Read a file

# normal
#
# with open('new.txt') as file:
#     print(file.read())
#
# #* now to avoid program crashing use exception handling
# try:
#     with open('C:\\Users\\chait\\OneDrive\\Desktop\\NE.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("The file was not found")


# ? Write a file
# # ! Write a function will overwrite the text present in the file
# text="HEY There\nthis is your boii Chaitanya\n"
# # ! Here 'w' means you are writing, it means you are in writing mode, there are various other modes
# with open('new.txt','w') as file:
#     file.write(text)
#
# # ! to append some text to the file need to use 'a' mode
# text2 = "HEY there, How you doing"
# with open('new.txt','a') as file:
#     file.write(text2)



# ? Copy file

#* copyfile() = copies contents of a file
#* copy() = copygfile() + permission mode + destination can be a directory
#* copy2() = copy() + copies metadata(files creation and modification times)

# ! syntax --> (sourcefile->src, destinationfile->dst)

# import shutil
#
# shutil.copyfile('new.txt','new2.txt')
# shutil.copy('new.txt','C:\\Users\\chait\\OneDrive\\Desktop\\NEW3.txt')



# ? Move a file
#
# import shutil
#
# shutil.copy('new.txt','test.txt')
#
# * now i want to move this test file to desktop folder
#
# import os
#
# source = "test.txt"
# destination = "C:\\Users\\chait\\OneDrive\\Desktop\\test.txt"
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source + " Moved Succesfully")
# except FileNotFoundError:
#     print("There is a problem "+source+" Not Found")
#

# ? Delete file
# # * to delete a file we use  -->  os.remove(path)
# # * To delete a empty folder we need to use -->  os.rmdir(path)
# # * To delete a folder which has files in it ---> shutil.rmtree

#
# import os
# import shutil
#
# # path = "new.txt"
# path = "NewProject"
#
# try:
#     # os.remove(path)  #* --> to delete a file
#     # os.rmdir(path) #* --> to delete an empty folder
#     # shutil.rmtree(path) #* --> to delete a folder containing files
#
# except FileNotFoundError:
#     print("File not exist")
# except PermissionError:
#     print("You donot have permission to delete that folder")
# except OSError:
#     print("You cannot delete a folder containing file with os.rmdir function")
# else:
#     print(path+" Deleted Succesfully")
#


# ? Modules

# * 1st Method

# import newfile
#
# newfile.hello()
# newfile.world()

# * 2nd Method

# import newfile as BigB
#
# BigB.hello()
# BigB.world()
#
# * 3rd Method

# from newfile import hello,world
# # from newfile import *
#
# hello()
# world()




# ? Rock Paper Scissor Game
#
# import random
#
# choices= ["Rock", "Paper", "Scissor"]
#
# computer = random.choice(choices)
# Player = None
#
# while Player not in choices:
#       Player = input("Choose your sign: ").capitalize()
#
# print("Player's Choice: ", Player)
# print("Computer's Choice: ", computer)
#
# if Player==computer:
#     print("tie")
# elif Player == "Rock":
#     if computer == "Paper":
#         print("Computer Wins")
#     elif computer == "Scissors":
#         print("Player Wins")
#
# elif  Player == "Paper":
#     if computer == "Scissors":
#         print("Computer Wins")
#     elif computer == "Rock":
#         print("Player Wins")
#
# elif Player == "Scissors":
#     if computer == "Rock":
#         print("Computer Wins")
#     if computer == "Paper":
#         print("Player Wins")




#? Python3 program for explaining
#? use of list, tuple, set and
#? dictionary
#
# #* Lists
# l = []
#
# # Adding Element into list
# l.append(5)
# l.append(10)
# print("Adding 5 and 10 in list", l)
#
# # Popping Elements from list
# l.pop()
# print("Popped one element from list", l)
# print()
#
# #* Set
# s = set()
#
# # Adding element into set
# s.add(5)
# s.add(10)
# print("Adding 5 and 10 in set", s)
#
# # Removing element from set
# s.remove(5)
# print("Removing 5 from set", s)
# print()
#
# #* Tuple
# t = tuple(l)
#
# # Tuples are immutable
# print("Tuple", t)
# print()
#
# #* Dictionary
# d = {}
#
# # Adding the key value pair
# d[5] = "Five"
# d[10] = "Ten"
# print("Dictionary", d)
#
# # Removing key-value pair
# del d[10]
# print("Dictionary", d)



# ? Break And Continue Keyword

# * Break to break the flow of the code

# for i in range(10,20):
#     print(i, end=" ")
#
#     if i == 17:
#         break
#     else:
#         pass
#
# print("\n")
#
#
# # * We use continue keyword to skip a particular element
# i=0
#
# while i<11:
#
#     if i == 7:
#         i = i+1
#         continue
#     else:
#         print(i, end=" ")
#     i += 1

# ? Two input from users in one line
#
# name = input("Enter your name: ")
# age = input ("Enter your age: ")
#
# print(name,"\n",age)
#
# * Rather than doing this we can take input in one line
#
# name,age = input("Enter your name and age: ").split()
# print(name,age)
#
# # * you can also do this .split(",") or any sign if you dont want to use space
#

# ? String formatting
# ? python 3.6
#
# name = "chaitanya"
# age = 22
#
# print(f"MY name is {name} and my age is {age}")



# ! Exercise
#
# num_1,num_2,num_3 = input(" Enter 3 digits: ").split(",")
#
# avg = (int(num_1) + int(num_2) + int(num_3))/3
#
# print(f"Avg of {num_1},{num_2},{num_3} is {avg} ")

# ? String Slicing
#
# p   0    -6
# y   1    -5
# t   2    -4
# h   3    -3
# o   4    -2
# n   5    -1
#
# [inclusive(start):exclusive(end):step]
#
# print("Python"[5::-1])
# print("Python"[::-1])  #trick
# print("Python"[-1::-1])


# name = input("Enter your name: ")
#
# print(name[::-1])
#


# print(len("chaitanya"))
#
# name = "chaitanya"
#
# name.upper()
# name.lower()
# name.title()
# print(name.count("a"))
#
# name, character = input("Enter the name and a single character = ").split(",")
#
# print("Name of the User: ", name.strip())
# print(f"Character count: {name.strip().lower().count(character.strip().lower())}")
#
#
# ? strip() method to remove spaces
# NAme = "   Chaitanya    "
# # * To remove space from the string we use strip method
#
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())

#
# # ? REPLACE
# NAME = ".....CHAITANYA....."
# print(NAME.replace(".....",""))
#
#


# ? Ternary Operator
#* value_if_true if condition else value_if_false
# ticket_price = 20 if int(age) >= 18 else 5
#


# ! In python we can change value of variable anytime
# * Here we are not changing the string of the variable
# # * We are changing the value of variable name
# name = "Chai"
# name += name + "tanya"
# print(name)
#
# age = 21
# age = 21+1
# print(age)
#




# ! Summary


# * Strings
# name = "Chaitanya"

# # * string slicing
# print(name[-1:0:-1])
#
# # *take user input
# age = int(input("Enter age: "))
# print(age)
#
# # * take two user inputs
# user_name, age = input("Enter name and age: ").split(",")
# print(user_name,age)
#
# # * len function
# print(ln(name))
#
# # * lower, upper and title method
# print(name.lower())
# print(name.upper())
# print(name.title())

#* find, replace and center method
#
# post_1 = name.find("a")
# pos_2 = name.find("a",post_1+1)
# print(post_1)
# print(pos_2)
#
# print(name.replace("C","c"))
#
# print(name.center(11,"$"))

# ! Exercise

# ! GUESS THE NO. GAME
#
# winning_number =int(input("Guess a random number between 1 to 20: "))
# guess_number = random.randint(1,20)
# print("Computer Generated no. : ",guess_number)
#
# if winning_number == guess_number:
#     print("You WIN")
# elif winning_number>guess_number:
#     print("You Entered a higher no., TOO HIGH ")
# elif winning_number<guess_number:
#     print("You Entered a lower no., TOO LOW")
#

# ! Exercise

#
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print(user_name)
# print(user_age)
#
# if  (user_name[0] == 'a' or user_name[0]=='A') and user_age >= 10 :
#     print("You can watch movie")
# else:
#     print("You cannot watch movie")

#
# if "a" in "Chaitanya":
#     print("a is present")
# else:
#     print("Not present")
#
# for i in "cahitan":
#     print(i, end="," )
# #

#* While loop
#
# user_number = int(input("Enter a number which u want to sum upto: "))
# print(user_number)
#
# total = 0
# i= 1
# while i<=user_number:
#     total+=i
#     i+=1
# print(total)

# # ! Exercise
# user_number = input("Enter a 4 digit no. : ")
# print("Entered Value",user_number)
# #

# print(f"Sum of the entered value is {int(user_number[0])}+ {int(user_number[1])} + {int(user_number[2])} + {int(user_number[3])}")
# sum = int(user_number[0]) + int(user_number[1]) + int(user_number[2]) + int(user_number[3])
# print("Sum of the entered four digit no. ",sum)

#* OR

# total = 0
# i = 0
# while i < len(user_number):
#     total+=int(user_number[i])
#     i+=1
# print(total)]


# user_name = input("Enter your name : ")
# print(user_name)
#
# C : 1
# H : 1
# A : 1
# I : 1
# T:  1
# A : 2
# N : 1
# Y : 1
# A : 3
#
# i = 0
# while i < len(user_name):
#     print(f"{user_name[i]}:{user_name.count(user_name[i])}")
#     i+=1

# * now i want this to be printed
# C : 1
# H : 1
# A : 1
# I : 1
# T:  1
# N : 1
# Y : 1
#
# temp_var = ""
# i = 0
# while i < len(user_name):
#     if user_name[i] not in temp_var:
#         temp_var += user_name[i]
#         print(f"{user_name[i]}:{user_name.count(user_name[i])}")
#         i+=1
#
 # * Exercise

 # 1234
#
# number = input("Enter a number: ")
# print(number)
#
# total = 0
# i=0
# for i in range(len(number)-1):
#     total = total + int(number[i])
#     i=i+1
# print(total)
#

#
# user_name = input("Enter your name: ")
# print(user_name)
#
# i=0
# temp = ""
#
# for i in range(len(user_name)-1):
#     if user_name[i] not in temp:
#         temp+=user_name[i]
#         print(f"{user_name[i]} : {user_name.count(user_name[i])} ")
#         i+=1


# ! Exercise Guess Random No.

# import random
#
# user_number = int(input("Enter a number between 1 and 100: "))
# print("User No.: ",user_number)
#
# winning_number = (random.randint(1,100))
#
#
# guess = 1
# game_over = False
#
# while not game_over:
#     if user_number ==  winning_number:
#        print(f"you guess correct number")
#        game_over=True
#     elif user_number > winning_number:
#        print("Too High")
#        guess+=1
#        user_number = int(input("Guess again: "))
#     elif user_number < winning_number:
#        print("Too low")
#        guess += 1
#        user_number = int(input("Guess again"))
#
#
#
# print(f"Correct No. is {winning_number} and You guessed correct and you guess in {guess} round")



# ! Exercise --> Find Greatest Value
# def greater_num(a,b):
#     if a > b:
#         return a
#     return b
# num_1 = int(input("Enter a number: "))
# num_2 = int(input("Enter a number: "))
# greater=greater_num(num_1,num_2)
# print(greater)

# ! Exercise Palindrome
# #
# user_name = input("Enter a name to check if it is a palindrome or not: ").upper()
#
# def palindrom(user_name):
#     if user_name == user_name[::-1]:
#         print(f"Input String {user_name} and reverse string {user_name[::-1]}")
#         print("Entered Word is palindrom word")
#     else:
#         print(f"Input String {user_name} and reverse string {user_name[::-1]}")
#         print("Entered Word is not a palindrom word")
#
# palindrom(user_name)

# ! Exercise Fibonacci Series
# ! Remaining
# 1 ---> 0
# 2 ---> 0 1
# 3 ---> 0 1 1
# 4 ---> 0 1 1 2
#
# user_number = input("Enter a number: ")
#
#
# def fibonacci_series(user_number):
#     i = 0
#     series = 0
#     while i <= user_number:
#         series  =
#         series = series + i

# ? List

# * methods to add items in list
# * append, extend, insert

# * methods to delete items from list
# * pop, remove, del

# * Some IMP methods of list

# list = ["orange","mango","kiwi","banana","apple","apple"]
# * Count
# print(list.count("apple"))  # 2

# * Sort method
# ! new sorted list will be changed to the old list
# list.sort()
# print(list)

# * Sorted function
# ! Sorted function does not change the original list sequence
# print(sorted(list))
# print(list)
#
# # * reverse
# list.reverse()
# print(list)

# # * clear
# list.clear()
# print(list) # []

# # * copy
# list_copy = list.copy()
# print(list_copy)


# ? IS AND == OPERATOR
#
# * == Operator
# To compare objects based on their values, Python’s equality operators (==) are employed.
# It calls the left object’s __eq__() class method, which specifies the criteria for determining equality.
# However, these constraints are typically written so that the equality operator == returns True if two objects,
# have the same value, and returns False if both have different value

#* What is the ‘is’ Operator?
# Python identity operators (is, is not) are used to compare objects based on their identity.
# When the variables on either side of an operator point at the exact same object,
# the “is” operator’s evaluation is true.
# Otherwise, it would provide us with a false assessment.

# list1 = []
# list2 = []
# list3 = list1

# # case 1
# if (list1 == list2):
#     print("True")
# else:
#     print("False")
#
# # case 2
# if (list1 is list2):
#     print("True")
# else:
#     print("False")
#
# # case 3
# if (list1 is list3):
#     print("True")
# else:
#     print("False")
#
# # case 4
# list3 = list3 + list2
#
# if (list1 is list3):
#     print("True")
# else:
#     print("False")


# ? Split Method

# name,age = input("Enter your name and age: ").split(" ")
# print(name,age)
#
# # * this will convert string to list
# user_nameandage = input("Enter your name and age").split(",")
# print(user_nameandage)

# * From where you want to break your string for eg when space,comma comes
# user_name = "Chaitanya galu".split()
# print(user_name)
# user_new = "Chaitanya&galu".split("&")
# print(user_new)

#? join method
# * convert list to string

# new_list = ["1","2","Hello"]
# print(",".join(new_list))
# print(" ".join(new_list))
# print("$".join(new_list))
#
# print(new_list)



# ? List vs Array

#
# in python list and array are different
#
# In list we can store multiple data types such as int,string,float
# Whereas in array we can only store similiar data types for eg only int or int string or only float
#
#     list is more flexible than array
#
# we use numpy array over python array
#
# javascript array is similiar to python's list



#? Strings and list

# * Strings are immutable
# * List are mutable
#
# string1 = "Hello"
# print(string1.lower())
# print(string1)
#
#
# list = ["1","2"]
# # print(list.append('3')) # this will not work
# list.append('3')
# print(list)

# ! Because = operator check the identity as both have same identity
# ! that is same location both will change
# list1 = ["1","2"]
# list2 = list1
# list2.append('4')
# print(list2)
# print(list1)


# list4 = ["1"]
# list5 = ["1"]
# list4.append('2')
# print(list4)
# print(list5)


# ! Exercise
#
# def find_square(list_n):
#     square_list = []
#     for i in list1:
#         square_list.append(i**2)
#     print(square_list)
#
#
# list_n = int(input("Enter the values for list: "))
# list1 = list(range(1, list_n))
# print(f"list is {list1}")
# find_square(list_n)
#
# ! Exercise
# * Method 1
# def reverse_string(l):
#     reverse_list = []
#     reverse_list = list1[::-1]
#     print(reverse_list)
#
# user_number = int(input("Entered a number: "))
# list1 = list(range(1,user_number+1))

# reverse_string(list1)

# ! Exercise Reverse a list using append and pop
# def reverse_list(l):
#     final_reverse_list = []
#     for i in range(len(original_list)):
#          popped_item = original_list.pop()
#          final_reverse_list.append(popped_item)
#     return final_reverse_list
#
# user_number = int(input("Enter a number: "))
# original_list = list(range(1,user_number+1))
# print("Original List",original_list)
# answer = reverse_list(original_list)
# print("Reversed List",answer)


# ! Exercise Reverse Elemnts of strings
#
# def reverse_elements(lists):
#     reverse_elements_list = []
#     for i in lists:
#      reverse_elements_list.append(i[::-1])
#     return reverse_elements_list
#
# lists = ["abc","def"]
# print(lists)
# print(reverse_elements(lists))

# ! Exercise filter odd and even

# def odd_even(numbers):
#     odd_numbers = []
#     even_numbers = []
#     odd_even_numbers = []
#
#     for i in numbers:
#         if(i%2==0):
#             even_numbers.append(i)
#         else:
#             odd_numbers.append(i)
    # odd_even_numbers.append(odd_numbers)
    # odd_even_numbers.append(even_numbers)
# OR
#     odd_even_numbers = [odd_numbers,even_numbers]
# print("Odd number list = ",odd_numbers)
    # print("Even number list = ",even_numbers)
    # return odd_even_numbers

# numbers = list(range(1,11))
# print("Original list = ",numbers)
# print("Odd and Even number list = ",(odd_even(numbers)))


# ! Exercise compare and gather common elements from 2 seperate list 
#
# def compare(list1,list2):
#
#     common_elements = []
#     for i in list1:
#         if i in list2:
#             common_elements.append(i)
#     return common_elements
#
#
#
# list1 = [1,2,3,4]
# list2 = list(range(1,9))
# print(list1)
# print(list2)
#
# print(compare(list1,list2))



# # ? *args and **kwargs
# # ! How to user all the parameters together
# # * Use this sequence to use all the parameters together
# #? order --> PADK
# # ?Parameter, *args, Default and **kwargs
#
# def func2(name,*args, last_name = "Unknown", **kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)
#
# func2('Chaitanya', 1,2,3, color="blue",hello = "world")


