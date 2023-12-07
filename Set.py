#? Set
# ? Set is an unordered collection  of unique items
# ? The order of items in set is not fixed
# ? In set we can add number, float, string data types
# ? We cannot add List and Dictionary in a Set
# ? Set donot have duplicate copy

# * How to define a set
# s = set()
# # print(s)
# # print(type(s))
#
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(1.0) # 1.0 will not print because set consider 1 and 1.0 same
# s.add("Hello")
# # print(s)
# #
# s1 = s.copy()
# print(s1)

# s1.remove(1)
# s1.remove(1.0)
# s1.remove(4)
# #* gives keyError as the set doesnot have that item present in it
# print(s1)

# s1.discard(1)
# s1.discard(4)
#* does not give keyError if the item is not present
# print(s1)

#
# l = list((1,2,4,3,5,6,7,3,4,6))
# print(type(l))
# print(l)
#
# # * now to remove duplicate number from list l convert it to set and then again convert into list
# s3 = set(l)
# print(s3)
# # * Here now the duplicate item has been removed now again convert it into list
# final_list = list(s3)
# print(final_list)

#* in short
# * To remove duplicate items from a list
# l = list((1, 2, 4, 3, 5, 6, 7, 3, 4, 6))
# finallist = list(set(l))
# print(l)
# print(finallist)


# * loop in set

s = {1,2,3,5,6}
#
# if 1 in s:
#     print("present")
# else:
#     print("Not present")
#
#
# for i in s:
#     print(i, end=" ")
#
# * Union
# * can use .union() or | for union
#
# s2 = {2,4,5,6,7}
# s3 = s2.union(s)
# print(s3)

# * OR with using | operator
#
# s2 = {2,4,5,6,7}
# s3 = s2 | s
# print(s3)

#* Intersection
# * Intersection using .intersection()
# s2 = {1,2,4,5,6,7,'Hello'}
# s4 = s2.intersection(s)
# print(s4)

#* Intersection using & operator
# s2 = {1,2,4,5,6,7,'Hello'}
# s4 = s2 & s
# print(s4)
#
# ! Sets are mainly used to remove duplicate copies and for mathematical solutions

