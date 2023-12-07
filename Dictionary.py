# # ? Dictionary
#
# # * Why we use Dictionary
# # * Because of limitations of lists, lists are not enough to represent real data
#
# # * Example
#
# user = ['Chaitanya', 22, ['Merc', 'Audi', 'BMW'], ['Blue', 'Green']]
# # * the list contains user_name, age, fav_car,fav_color
# # * You can do this but this is not a good way as we cannot get to know for what this data is
#
# # * What are dictionaries
# # * Unordered collections of data in key:value pair
#
# # * How to create dictionary
#
# user1 = {
#      'name': 'Chaitanya',
#      'age': 22,
#      'fav_car': ['Merc', 'Audi', 'BMW'],
#      'fav_color': ['Blue', 'Green']
# }
#
# # * How to access items
# print(user1['name'])
# print(user1['age'])
# print(user1['fav_car'])
# print(user1['fav_color'])
#
# # * How to add or change
# user1['fav_color'] = ['Blue', 'Green', 'Orange']
# print(user1)
#
#
# # * New way to create dictionary
#
# user2 = dict(name="Chaitanya", age="22", fav_food=["Pizza", "South-Indian"])
#
# print(user2)
#
#
# # * Can store any data types -> strings, int, lists, dictionary
# #
# # users = {
# #     user1: {
# #
# #     },
# #     user2: {
# #
# #     }
# # }
#
# # * How to add items to empty dictionary
# #
# # user_info = {}
# # user_info['name'] = 'Chaitanya'
# # print(user_info)



#* get()  method
# #* doesnot give any error if the value is not present
# person = {
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 25,
#     'favorite_colors': ['blue', 'green'],
#     'active': True
# }

# ssn = person.get('ssn')
# print(ssn)
#
# * add
# person['favourite_cars'] = ['Audi', 'BMW', 'Merc']

# print(person)
# # * modifying value
# person['first_name'] = 'Chaitanya'
# person['age'] = '22'
# person['last_name'] = 'Panchal'
#
# # * deleting value
# del person['active']
#
# print(person)
# * pop method
# popped_items= person.pop('favourite_cars')
# print(person)
# print(popped_items)  #-> returns list

# * popitem() method
# * It randomly deletes any key value pair from the dictionary
# new_pop = person.popitem()
# print(new_pop)

# * looping through dictionary
#
# for key in person:
#     print(key)
#
# for Key in person.keys():
#     print(Key)
#
# for value in person.values():
#     print(value)
#
# for key,value in person.items():
#     print(f"{key}:{value}")


# * Update Method
#
# new_info = {
#     'Hello' : "World"
# }
#
# person.update(new_info)
# print(person)



# * fromkeys
#
# dictionaries =  dict.fromkeys(['name','age'], 'unknown')
# dictionariesss =  dict.fromkeys(('abc'), 'unknown')
# print(dictionariesss) #{'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}
# print(dictionaries) # {'name': 'unknown', 'age': 'unknown'}
#
# dictionariess =  dict.fromkeys(range(1,11), 'unknown')
# print(dictionariess)

# d1 = dictionaries.copy()
# print(d1)
# # * HEre it creates a new copy of dictionaries
# print(d1 is dictionaries) # * It gives false because they are not the same dictionaries
# print(d1 == dictionaries) #* This will give true because d1 is equal to dictionaries
#
# d2 = dictionaries
# * THis will assign the values of dictionaries to d2 and if we delete
# * one element from d2 then that same delete will get deleted from dictionaries


# ! Exercise
# Output : {1: 1, 2: 8, 3: 27}

# def cube_return(n):
#     i = 1
#     dict1 = {}
#     for i in range(1,n+1):
#        dict1[i] = i**3
#        i += 1
#     return dict1
#
# n = int(input("Enter a number: "))
# output =cube_return(n)
# print(output)
# #

# ! Exercise Word Counter Using Dictionary

# def word_counter(str):
#     dict2 = {}
#     for char in str:
#         dict2[char] = str.count(char)
#     return dict2
#
# str = input("Enter a name: ").upper()
# print(word_counter(str))
#

# ! Exercise

#* sample :
# name:Chaitanya
# last_name:Panchal
# age:22
# Favorite_color:['Blue', 'Green']

#
# def usersdict(name,last_name,age,Favorite_color):
#     users1= {}
#     users1['name'] = name
#     users1['last_name'] = last_name
#     users1['age'] = age
#     users1["Favorite_color"] = Favorite_color
#
#     for key, value in users1.items():
#         print(f"{key}:{value}")
#
# name, last_name = input("Enter your name and fullname: ").split(",")
# age = int(input("Enter your age: "))
# Favorite_color = input("Enter your Favorite color: ").split(",")
# 
# usersdict(name,last_name,age,Favorite_color)
