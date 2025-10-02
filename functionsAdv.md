# Functions - Adavenced Concepts / Level 2
in this section we will learn about more advanced concepts of functions, like recursion,lambda functions, variable lenght arguments.

# 1. Variable Lenght Arguments
In python, we can pass a variable number of arguments to a function. This is called variable lenght arguments.

You can pass a variable number of arguments to a function by using the `*` symbol before the parameter name,like this: `*args`,`**kwargs`.

`*args` is used to pass a variable number of positional arguments to a function.

`**kwargs` is used to pass a variable number of keyword arguments to a function.

**Syntax:**
```python
def function_name(*args, **kwargs):
    # function body
```

**Example: Variable Lenght Arguments**
```python
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3,4,5))
```
**Output:**
```
15
```

```python
def greet(**kwargs):
    print(f"Hello {kwargs['name']}")
greet(name="Enari Coding")
```
**Output:**
```
Hello Enari Coding
```
---

# 2. Lambda Functions
Lambda functions are anonymous functions that can be defined in-line without a name. They are useful when you need to define a small function without the need for a full function definition.

**Syntax:**
```python
lambda arguments: expression
```

**Example: Lambda Functions**
```python
add = lambda x,y: x+y
print(add(10,20))
```
**Output:**
```
30
```
**Example 2:**
```python
students = [{"name":"Enari","age":20},{"name":"Alice","age":18},{"name":"Bob","age":22}]
students.sort(key=lambda x: x["age"])
print(students)
```
**Output:**
```
[{'name': 'Alice', 'age': 18}, {'name': 'Enari', 'age': 20}, {'name': 'Bob', 'age': 22}]

```
---

# 3.Recursion

Recursion is a technique where a function calls itself to solve a problem. It is useful when a problem can be broken down into smaller subproblems that can be solved using the same function.

**Syntax:**
```python
def function_name(parameters):
    # function body
    if condition:
        return function_name(parameters)
```

**Example: Recursion**
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
```
**Output:**
```
120
```

---

# 4.Nasted Functions
You can define a function inside another function. This is called nested functions.

**Syntax:**
```python
def outer_function():
    def inner_function():
        # function body
    return inner_function()
```

**Example: Nested Functions**
```python
def outer_function():
    def inner_function():
        print("Hello")
    return inner_function()
outer_function()
```
**Output:**
```
Hello
```

--- 

# HomeWork:

## 1 factorial function
Write a function named `factorial` that takes a parameter `n` and returns the factorial of `n`.

## 2 Fibonacci function
Write a function named `fibonacci` that takes a parameter `n` and returns the `n`th Fibonacci number.

## 3 Recursion
Write a function named `is_prime` that takes a parameter `n` and returns `True` if `n` is a prime number, and `False` otherwise.

## 4 Recursion
Write a function named `sum_of_primes` that takes a parameter `n` and returns the sum of all prime numbers less than or equal to `n`.

## 5 Recursion
Write a function named `power` that takes two parameters `base` and `exponent` and returns the result of raising `base` to the power of `exponent`.

## 6 Recursion
Write a function named `fibonacci_series` that takes a parameter `n` and returns a list of the first `n` Fibonacci numbers.

## 7 Recursion
Write a function named `factorial_tail` that takes a parameter `n` and returns the factorial of `n` using recursion.

## 8 Recursion
Write a function named `fibonacci_tail` that takes a parameter `n` and returns the `n`th Fibonacci number using recursion.

## 9 Recursion
Write a function named `is_prime_tail` that takes a parameter `n` and returns `True` if `n` is a prime number, and `False` otherwise using recursion.

## 10 Recursion
Write a function named `sum_of_primes_tail` that takes a parameter `n` and returns the sum of all prime numbers less than or equal to `n` using recursion.