#While loops


# i = 0
# while i < 5:
#     print(i)
    # i = i + 1

# for i in range(5):
#     print(i)

# for i in range(5):
#     print(i)
#     i=i+2

# a=0
# while a<5:
#     print(a)
#     a=a+1
#     if a==3:
#         break
# print("after break")

# a=0
# while a<5:
#     if a==2:
#         a=a+1
#         continue
#     print(a)
#     a=a+1
# print("after continue") 

# i=0
# while i<10:
#     x=0
#     while x<i:
#         print("somesh" ,end="_")
#         x=x+1
#     print("Hi")
#     i=i+1
# print("after while")

# pin = 1234
# triales = 1
# while triales <=3:
#     user_pin = int(input(f"Trails number is {triales} Enter your pin: "))
#     triales = triales + 1
#     if user_pin == pin:
#         print("Correct pin")
#         break
#     else:
#         print("Wrong pin")
#         # triales = triales + 1
#         # if triales == 3:
#         #     print("You have used all the trials")
#             # break
# # print("You have used all the trials")


#for loops

# name = "somesh"
# for index,letters in enumerate(name): #enumerate returns index and letters
#     print(letters*(index+1))

# d = {"name":"somesh","age":24,"city":"Bangalore"}
# # print(d.items()) #prints key value pairs
# for key,value in d.items():
#     print(key,value)

# for i in range(1,11):
#     # print(f"2 X {i} = {2*i}")
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}")
#     print("")

#sum
# l = [1,2,3,4,5]
# print(sum(l))
# sum1 = 0
# for i in l:
#     sum1 = sum1 + i
# print(sum1)

# students = ["somesh","rahul","anil"]
# marks = [90,80,70]
# studenrs_marks = {}
# # for student,mark in zip(students,marks):
# #     print(f"{student} has scored {mark}")
    
# for index,student in enumerate(students):
#     # print(f"{student} has scored {marks[index]}")
#     studenrs_marks[student] = marks[index]
# print(studenrs_marks) 

#list comprehension
# l = [1,2,3,4,5]
# print(l)
# # print([i*2 for i in l])
# print([i for i in l if i%2==0])

#split()
s = "somesh is a good boy"
print(s.split())
print(s.split(" "))
print(s.split("is"))
print(s.split("is",1))
print(s.split("is",2))

