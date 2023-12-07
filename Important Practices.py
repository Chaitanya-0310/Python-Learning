
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




# ! Exercise on *args

# def to_power(num,*list_1):
#     new_list = []
#     new_list= (i**num for i in list_1)
#     return new_list
#
#
# num = int(input("Enter a number: "))
# list_number_A = int(input("Enter a starting number: "))
# list_number_B = int(input("Enter a Ending number: "))
# list_1 = []
# for i in range(list_number_A,list_number_B):
#     list_1.append(i)
# print(list_1)
#
# output=to_power(num,*list_1)
# print(list(output))


# # ! Exercise
# def new_function(list_1,reverse_str):
#     anotherNewList = []
#     if reverse_str == "True":
#         for new_list in list_1:
#             anotherNewList.append(new_list[::-1].capitalize())
#     elif reverse_str=="False":
#         for new_list in list_1:
#             anotherNewList.append(new_list.capitalize())s
#     return anotherNewList
#
# list_1 = ['chaitanya','panchal']
# reverse_str = input("Enter True or False: ")
# print(new_function(list_1,reverse_str ))



# ! Above exercise using list comprehension and **kwargs
#
#
# def new_function(list_1,**kwargs):
#     if kwargs.get('reverse_str') == True:
#         return [newList[::-1].capitalize() for newList in list_1]
#     else:
#         return [newList.capitalize() for newList in list_1]
#
# list_1 = ['chaitanya','panchal']
# print(new_function(list_1, reverse_str = True ))
# # *                        This will get  converted to key-value pair due to **kwargs
#
#








