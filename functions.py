

# def greet():
#     print("Hello,Good morning")
# greet()

# def add(x,y):
#     return x+y
# print(add(10,20))


# def greetWithName(name):
#     print("Hello",name,"Good morning")
# greetWithName("Alice")
# greetWithName("Bob")    

# def tables(j):
#     for i in range(1,11):
#         print(f"{j}X{i} = {j*i} ")
# tables(5)

students = [{"name":"Enari","age":20},{"name":"Alice","age":18},{"name":"Bob","age":22}]
students.sort(key=lambda x: x["age"])
print(students)