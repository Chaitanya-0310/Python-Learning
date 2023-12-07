#?  Recursion Function
#
#* 1) Recursion Function   sum(n)
#* 2) Create Recursion Case   n + sum(n-1)
#* 3) Create Base Case  n==1 return 1

# ! Exercise

# ! Sum of n natural numbers
#
# def sum(n):
#     if (n==1):
#         return 1
#     return n + sum(n-1)
#
# n=5
# print(sum(n))


#! Write a Python program to sum recursion lists.
# def recursive_list_sum(data_list):
# 	total = 0
# 	for element in data_list:
# 		if type(element) == type([]):
# 			total = total + recursive_list_sum(element)
# 		else:
# 			total = total + element
#
# 	return total
# print( recursive_list_sum([1, 2, [3,4],[5,6]]))


#  ! Factorial of non negative integer
#
# def factorial(n):
# 	if n <= 1:
# 		return 1
# 	return n * (factorial(n-1))
# print(factorial(5))
#


def add(a,b):
	return a+b
#
# S=add(2,4)
# x = add
#
# print(S)
# print(x)
#
# print(x is add)
# print(x == add)



