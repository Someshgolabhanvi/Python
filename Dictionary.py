#Dictionary
#Dictionary is a collection of key-value pairs
#Key is a unique identifier
#Value is the data associated with the key
# dict1 = {"name":"John","age":25,"city":"New York"}
# dict2 = {"name":"John","age":25,"city":"New York","country":"USA"}
# dict3 = {"name":"John","age":25,"city":"New York","country":"USA","hobby":"programming"}
# print(dict1)
# print(dict2)
# print(dict3)

#Accessing values
# name = dict1["name"]
# age = dict1["age"]
# city = dict1["city"]
# country = dict2["country"]
# hobby = dict3["hobby"]
# print(name)
# print(age)
# print(city)
# print(country)
# print(hobby)

# #Accessing keys
# for key in dict1:
#     print(key)
# for key in dict2:
#     print(key)
# for key in dict3:
#     print(key)

# #Accessing values using in operator
# for value in dict1.values():
#     print(value)
# for value in dict2.values():
#     print(value)
# for value in dict3.values():
#     print(value)

# #Accessing keys using in operator
# for key in dict1.keys():
#     print(key)
# for key in dict2.keys():
#     print(key)
# for key in dict3.keys():
#     print(key)

# #Accessing items
# for item in dict1.items():
#     print(item)
# for item in dict2.items():
#     print(item)
# for item in dict3.items():
#     print(item)

# #Accessing keys and values
# for key,value in dict1.items():
#     print(key,value)
# for key,value in dict2.items():
#     print(key,value)
# for key,value in dict3.items():
#     print(key,value)

# meanings = {
#     'hello':'a greeting',
#     'where':'to ask about location',
#     'how': 'to ask about condition or manner',
#     'why': 'to ask about reason or cause',
#     'what': 'to ask about what',
#     'who': 'to ask about who',
# }
# print(meanings['how'])
# #mutaion
# meanings['how'] = 'to ask about manner or condition'
# print(meanings['how'])

#using dic() function
meanings = dict()
# meanings['hello'] = 'a greeting'
# meanings['where'] = 'to ask about location'
# meanings['how'] = 'to ask about manner or condition'
# meanings['why'] = 'to ask about reason or cause'
# meanings['what'] = 'to ask about what'
# meanings['who'] = 'to ask about who'
# print(meanings)

#sets
set1 = {1,2,3,4,5}
#tuples
tuple1 = (1,2,3,4,5)
#lists
list1 = [1,2,3,4,5]

#dictionaries
dict1 = {"name":"John","age":25,"city":"New York"}

print(dict1.get("country","Not Found"))
print(dict1['name'])