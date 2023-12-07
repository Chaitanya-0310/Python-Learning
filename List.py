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


# ? LIST COMPREHENSION

#? Syntax: newList = [ expression(element) for element in oldList if condition ]

#* expression: Represents the operation you want to execute on every item within the iterable.
#* element: The term “variable” refers to each value taken from the iterable.
#* iterable: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
#* condition: (Optional) A filter helps decide whether or not an element should be added to the new list




#! Exercise
# ! create list -> [-1,0,1]

# # * Normal way
# def createlist(r1,r2):
#     emptylist = []
#     for i in range(r1,r2+1):
#         emptylist.append(i)
#     return emptylist
#
# r1,r2 = -1,1
# print(createlist(r1,r2))

# * Now using list comprehension way
# r1,r2 = -1,1
# emptylist3 = [i for i in range(r1,r2+1)]
# print(emptylist3)
# [-1, 0, 1]




# ! Practice
#! 1
# emptylist = [i**2 for i in range(1,11)]
# print(emptylist)
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#! 2
# emptylist2 = [-i for i in range(1,4)]
# print(emptylist2)
# [-1, -2, -3]
#! 3
# name = ["Hello","World","Hii"]
# new_name = [names[0] for names in name]
# print(new_name)
# ['H', 'W', 'H']

# ! Exercise
# l = ["abc","cda","efg"]

# def reverse_string(l):
#     reversed_string_list = []
#     for reverseStr in l:
#       reversed_string_list.append(reverseStr[::-1])
#     return reversed_string_list
#
# print(reverse_string(l))

# * Now using list comprehension

# reversed_string_list = [reverseStr[::-1] for reverseStr in l ]
# print(reversed_string_list)
# ['cba', 'adc', 'gfe']

# * Using function
# def reversed_string(l):
#     return [reverseStr[::-1] for reverseStr in l ]
# print(reversed_string(l))
# ['cba', 'adc', 'gfe']


#! Exercise
#
# def new_function(entered_list):
#     result = []
#     for newList in entered_list:
#         if type(newList) == int or type(newList) == float:
#             result.append(str(newList))
#     return result

# entered_list = [True,False,"hello",1,2.0,3]
# output = new_function(entered_list)
# print(output)

# * Now using list comprehension
# #
# def new_function(entered_list):
#     result_list = []
#     return [str(newList) for newList in entered_list if (type(newList) == int or type(newList) == float)]
#
# print(new_function([True,False,"hello",1,2.0,3]))
#


# def factorial(n):
#     result = 1
#     for num in range(1, n + 1):
#         result = result*num
#     return result
#
#
# user_num = int(input("Enter a single digit number: "))
# print(factorial(user_num))