# variables
a=10
b=20
name="John"

# print
print("Hello World")
print(a)
print(b)
print(name)

# arithmetic
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b

# comparison
h=a>b
i=a<b
j=a==b
k=a!=b

# boolean
l=True
m=False

# if
if a>b:
    print("a is greater than b")
else:
    print("a is less than or equal to b")

# for
for i in range(10):
    print(i)

# while
i=0
while i<10:
    print(i)
    i=i+1

# break
i=0
while i<10:
    print(i)
    i=i+1
    if i==5:
        break

# continue
i=0
while i<10:
    print(i)
    i=i+1
    if i==5:
        continue

# pass    
if a>b:
    pass
else:
    print("a is less than or equal to b")

# function
def add(a,b):
    return a+b

print(add(10,20))

# class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hi(self):
        print("Hi, my name is",self.name)
    def say_age(self):
        print("I am",self.age,"years old")

p=Person("John",25)
p.say_age() 

Person.say_hi(p)

a = 10
b = 20
c = a # c=10
a = b # a=20
b = c # b=10
print(a,b)

#List        
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [1,2,3,4,5,"a","b","c","d","e"]
print(list1)
print(list2)
print(list3)

#Tuple 
tuple1 = (1,2,3,4,5)
tuple2 = ("a","b","c","d","e")
tuple3 = (1,2,3,4,5,"a","b","c","d","e")
print(tuple1)
print(tuple2)
print(tuple3)

#Dictionary
dict1 = {"name":"John","age":25,"city":"New York"}
dict2 = {"name":"John","age":25,"city":"New York","country":"USA"}
dict3 = {"name":"John","age":25,"city":"New York","country":"USA","hobby":"programming"}
print(dict1)
print(dict2)
print(dict3)

#Set        
set1 = {1,2,3,4,5}
set2 = {"a","b","c","d","e"}
set3 = {1,2,3,4,5,"a","b","c","d","e"}
print(set1)
print(set2)
print(set3)

#Range
for i in range(10):
    print(i)
for i in range(1,10):
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(10,0,-1):
    print(i)

#String
str1 = "Hello World"
str2 = 'Hello World'
str3 = """Hello World"""
print(str1)
print(str2)
print(str3)

#Comment
# This is a comment

#Import
import math
import random
from math import *

#Function
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def remainder(a,b):
    return a%b
def power(a,b):
    return a**b

print(add(10,20))
print(subtract(10,20))
print(multiply(10,20))
print(divide(10,20))
print(remainder(10,20))
print(power(10,20))

#Class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hi(self):
        print("Hi, my name is",self.name)
    def say_age(self):
        print("I am",self.age,"years old")

p=Person("John",25)
p.say_age() 

Person.say_hi(p)

#Module
import math
print(math.pi)
print(math.e)
print(math.sqrt(25))

#Exception
try:
    print(1/0)
except ZeroDivisionError:
    print("Error: Division by zero")
except:
    print("Error: An unknown error occurred")
finally:
    print("This will always be executed")      

#File Handling
#Write        
f=open("hello.txt","w")
f.write("Hello World")
f.close()

#Read
f=open("hello.txt","r")
print(f.read())
f.close()

#Append
f=open("hello.txt","a")
f.write("Hello Again")
f.close()

         