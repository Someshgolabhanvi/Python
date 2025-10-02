# 1.Basics of functions

A function is a reusable block of code that performs a specific task when called.  
Functions help organize code and reduce redundancy.

---

# Definning a function
You can define a function using the `def` keyword followed by the function name and parentheses `()` and a colon`:`.

**Syntax:**
```python
def function_name(parameters):
    # function body
```

**Example: Basic function**
```python
def greet():
    print("I'm learning functions in python")
greet()
```
**Output:**
```
I'm learning functions in python
```

---

# Function parameters
You can pass parameters to a function by using the `parameters` in the function definition.  
Parameters are like variables that are used to pass values to a function.

**Syntax:**
```python
def function_name(parameter1, parameter2, ...):
    # function body
```

**Example: Function with parameters**

```python
def greet(name):
    print("Hello",name)
greet("Enari Coding")
```

**Output:**
```
Hello Alice
```

---

# Returning a value from a function
You can return a value from a function using the `return` keyword followed by the value you want to return.

**Syntax:**
```python
def function_name(parameters):
    # function body
    return value
```

**Example: Function with return statement**

```python
def add(x,y):
    return x+y
print(add(10,20))
```
**Output:**
```
30
```

---

# Positional and keyword arguments
Positional arguments are the arguments that are passed to a function in the same order as they are defined in the function definition.  
Keyword arguments are the arguments that are passed to a function using the `name=value` syntax.    
Keyword arguments are optional and can be used to pass values to a function in any order.

**Syntax:**
```python
def function_name(positional_argument1, positional_argument2, ..., keyword_argument1=value, keyword_argument2=value, ...):
    # function body
```

**Example: Function with positional and keyword arguments**
```python
def greet(name, greeting="Hello"):
    print(greeting,name)
greet("Enari Coding")
greet("Enari Coding","Welcome")
```
**Output:**
```
Hello Enari Coding
Welcome Enari Coding
```

---

# Default arguments
Default arguments are the values that are used if a positional argument is not provided when calling a function.      
Default arguments are optional and can be used to provide default values for positional arguments.

**Syntax:**
```python
def function_name(positional_argument1, positional_argument2, ..., keyword_argument1=value, keyword_argument2=value, ...):
    # function body
```

**Example: Function with default arguments**
```python
def greet(name, greeting="Hello"):
    print(greeting,name)
greet("Enari Coding")
greet("Enari Coding","Welcome")
```
**Output:**
```
Hello Enari Coding
Welcome Enari Coding
```

---

# Variable scope
Variable scope refers to the visibility and accessibility of variables in a program.  
Variables can be accessed from different parts of a program and can be used in different functions.

**Example: Variable scope**
```python
x = 10
def add(y):
    return x+y
print(add(20))
```
**Output:**
```
30
```

---


# Returning values from functions
You can return values from functions using the `return` keyword followed by the value you want to return.

**Syntax:**
```python
def function_name(parameters):
    # function body
    return value
```

**Example: Returning values from functions**

```python
def add(x,y):
    return x+y
print(add(10,20))
```
**Output:**
```
30
```

---


# HomeWork:

## 1 Geet Function
Write a function named `greet` that takes a name as a parameter and prints a greeting message with the name.

## 2 Add Function
Write a function named `add` that takes two parameters `x` and `y` and returns their sum.

## 3 Tables Function
Write a function named `tables` that takes a parameter `j` and prints the multiplication table for `j` from 1 to 10.

## 4 Functions
Write a function named `calculate_area` that takes two parameters `length` and `width` and returns the area of a rectangle.

## 5 Functions
Write a function named `calculate_volume` that takes three parameters `length`, `width`, and `height` and returns the volume of a rectangular prism.

## 6 Functions
Write a function named `calculate_perimeter` that takes two parameters `length` and `width` and returns the perimeter of a rectangle.

## 7 Functions
Write a function named `calculate_circumference` that takes one parameter `radius` and returns the circumference of a circle.

## 8 Parameterizing Functions
Write a function named `greet` that takes a name as a parameter and prints a greeting message with the name.