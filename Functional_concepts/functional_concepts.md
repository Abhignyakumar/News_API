# DECORATORS, GENERATORS,LAMBDA,DICT,LIST - CRUD Fast API and API
# Overview
In this concept we will get to learn about the Decorators, Generators, Lambda, Dict, List - CRUD Fast API and API. In FastAPI CRUD applications, we commonly use lists to store multiple records and dictionaries to represent each record’s details (like a user’s name, age, etc.). Lambda functions help with quick operations like sorting or filtering data. Generators are used to handle data efficiently by yielding one item at a time, useful when working with large datasets. Decorators allow us to wrap API functions with extra functionality like logging, authentication, or access control
# Prerequisites
Python 3.12+ installed (Download Python)</br>
Code editor (VS Code recommended) with Python extension</br>
Basic understanding of programming concepts</br>

# DECORATOR IN PYTHON:
What is a Decorator in Python?</br>A decorator is a higher-order function — it takes another function as an argument and returns a new function that extends or modifies the behavior of the original, without altering its source code.

## Common Use Cases:
| Use Case         | Description                                             |
|------------------|---------------------------------------------------------|
| Logging          | Automatically log function calls and results           |
| Authentication   | Check if a user is authenticated before running a function |
| Access Control   | Grant or deny access based on roles/permissions        |
| Execution Timing | Measure how long a function takes to run               |
| Retry Mechanisms | Retry a function if it fails due to transient issues   |
| Data Validation  | Validate inputs before executing the function          |

### Simple Example:
```
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
```

### Output:
Before the function runs
Hello!
After the function runs







# GENERATOR IN PYTHON
What is a Generator in Python?</br>A generator is a special type of iterator that lets you generate values one at a time, only as needed, using the yield keyword — which allows functions to produce a lazy sequence of values instead of returning them all at once.


Common Use Cases:
| Case               | Description                                                         |
|--------------------|---------------------------------------------------------------------|
| Large Data Sets    | Process large files or streams without loading everything into memory |
| Pipelining         | Create data processing pipelines                                    |
| Infinite Sequences | Generate endless series like Fibonacci or counters                 |
| Custom Iterators   | Implement your own iteration behavior for classes or functions     |
| Lazy Evaluation    | Avoid unnecessary computation by delaying evaluation               |


### Simple Example:
```
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)
```

### output
5
4
3
2
1









# LAMBDA FUNCTION IN PYTHON

What is a Lambda Function in Python?</br>A lambda function is a small anonymous function defined using the lambda keyword.
It's often used for short, throwaway operations especially where defining a full function is unnecessary.

Common Use Cases:
| Use Case | Example             |
|----------|---------------------|
| Sorting  | Custom sort keys    |
| Filtering | `filter()` function |
| Mapping  | `map()` function     |
| Reducing | `reduce()` function  |


Simple example
# Regular function
```
def add(x, y):
    return x + y
```

# Equivalent lambda function
```
add_lambda = lambda x, y: x + y

print(add_lambda(2, 3)) 
```
 ### Output: 5

# Using lambda with filter()
```
nums=[1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even) 
odd = list(filter(lambda x: x % 2 != 0, nums))
print(odd)  
 ```
### Output: [2] 

# Using lambda with map()
```
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print(squared)  
```
### Output: [1, 4, 9]








# DICTIONARY(DICT) IN PYTHON 
What is a Dictionary (dict) in Python?</br>A dictionary is a built-in Python data structure that stores data in key-value pairs.
Each key in the dictionary is unique, and is used to access its corresponding value.
Common Use Cases:
| Use Case            | Description                                                       |
|---------------------|-------------------------------------------------------------------|
| Storing structured data | Like user profiles, settings, or JSON-like objects              |
| Lookup tables        | Fast access to values using unique keys                          |
| Counting items       | Use keys to count frequency (with loops or `collections`)        |
| Configuration        | Store application settings or environment variables              |
| Grouping data        | Based on keys like categories, user IDs, etc.                    |

###Simple Example:
```
person = {
    "name": "Abhi",
    "age": 25,
    "city": "Hyderabad"
}

print(person["name"]) 
print(person["name"], "of age", person["age"], "from", person["city"]) 
```
### Output: Abhi
### output: Abhi of age 25 from Hyderabad





















#LIST IN PYTHON
What is a List in Python?</br>A list in Python is an ordered, mutable collection of items.
Lists can hold any data type, including numbers, strings, other lists, or even a mix of types.
Common use cases:
| Use Case             | Description                                              |
|----------------------|----------------------------------------------------------|
| Store multiple items | Like numbers, names, results, etc.                       |
| Iterate over sequences | Using loops (`for`, `while`)                            |
| Dynamic data changes | Append/remove items on the fly                          |
| Temporary containers | Grouping values temporarily for processing              |
| Nested structures    | Lists inside lists (matrices, grids, etc.)              |

	
| Operation         | Example                          | Result/Effect                          |
|-------------------|----------------------------------|----------------------------------------|
| Access by index   | `fruits[0]`                      | `"apple"`                              |
| Update item       | `fruits[1] = "kiwi"`             | Changes `"banana"` to `"kiwi"`         |
| Append item       | `fruits.append("orange")`        | Adds `"orange"` to the end             |
| Insert item       | `fruits.insert(1, "grape")`      | Inserts `"grape"` at index 1           |
| Remove by value   | `fruits.remove("apple")`         | Removes `"apple"`                      |
| Remove by index   | `fruits.pop(0)`                  | Removes item at index 0                |
| Check existence   | `"banana" in fruits`             | Returns `True` if exists               |
| Sort list         | `fruits.sort()`                  | Sorts in ascending order               |
| Reverse list      | `fruits.reverse()`               | Reverses the order of the list         |
| Get length        | `len(fruits)`                    | Returns number of elements             |

# DECORATORS, GENERATORS,LAMBDA,DICT,LIST by using CRUD Fast API and API

| Operation  | What Happens                               |
| ---------- | ------------------------------------------ |
| **Create** | Add a new dict to the list                 |
| **Read**   | Loop through the list and return dicts     |
| **Update** | Find a dict by `id` and update values      |
| **Delete** | Remove a dict from the list using its `id` |


We’ll use a mini User Management API as an example.

## User Data (List of Dicts)
```
users = [
    {"id": 1, "name": "Abhi", "age": 25},
    {"id": 2, "name": "Kumar", "age": 30}
]
```
# List & Dict in CRUD
## Get All Users (Read)
```
@app.get("/users")
def get_users():
    return users  # List of dictionaries
```
### Add New User (Create)
```
@app.post("/users")
def add_user(user: dict):
    users.append(user)  # Add dict to list
    return {"message": "User added"}
```
### Update a User (Update)
```
@app.put("/users/{user_id}")
def update_user(user_id: int, new_data: dict):
    for user in users:
        if user["id"] == user_id:
            user.update(new_data)
            return {"message": "User updated"}
    return {"error": "User not found"}
```
### Delete a User (Delete)
```
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [user for user in users if user["id"] != user_id]
    return {"message": "User deleted"}
```

# Lambda Function
Sort users by age:
```
@app.get("/users/sorted")
def sort_users():
    return sorted(users, key=lambda x: x["age"])  # Lambda for sorting
 ```
# Generator function 
```
def user_generator():
    for user in users:
        yield user  # returns one user at a time

@app.get("/users/stream")
def stream_users():
    return list(user_generator())  # convert generator to list for FastAPI response
```
# Decorator for Logging API Access
```
def log_request(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@app.get("/users/logged")
@log_request
def get_users_logged():
    return users
```

























Interview questions 
1.	What is a decorator in Python?
2.	How do you define a decorator in Python?
3.	How do you apply a decorator to a function?
4.	What is a generator in Python?
5.	What is the difference between yield and return?
6.	What happens when a generator is exhausted?
7.	What is a lambda function in Python?
8.	Why do we use lambda functions?
9.	What is the syntax of a lambda function?
10.	What is a dictionary in Python?
11.	What happens if you try to access a key that doesn't exist?
12.	Can dictionary keys be mutable types like lists?
13. Why Use List & Dict Together in CRUD?
































Python Decorators
1. What is a decorator in Python?</br>Answer:A decorator is a higher-order function that takes another function as input and returns a new function with added or modified behavior — without changing the original function's code.
________________________________________
2. How do you define a decorator in Python?</br>Answer:You define a decorator by writing a function that wraps another function. It uses an inner function (wrapper) and returns it.
Syntax:
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
________________________________________
3. How do you apply a decorator to a function?</br>Answer:Using the @decorator_name syntax just above the target function.
Syntax:
@my_decorator
def say_hello():
    print("Hello")
________________________________________
 Python Generators
 4. What is a generator in Python?</br>Answer:
A generator is a function that returns an iterator and uses yield to produce values one at a time, pausing between each.
________________________________________
5. What is the difference between yield and return?</br>Answer:
return	yield
Exits the function	Pauses and saves state
Returns a value	Returns a generator object
Cannot be resumed	Can be resumed later
________________________________________
6. What happens when a generator is exhausted?</br>Answer:It raises a StopIteration exception when there are no more values to yield.
________________________________________
Lambda function in Python
7.  What is a lambda function in Python?
Answer:A lambda function is an anonymous (unnamed) function defined using the lambda keyword. It can take any number of arguments but only one expression.
Python
________________________________________
8. Why do we use lambda functions?</br>Answer:Lambda functions are used when you need a short function for a single use, especially inside functions like map(), filter(), or sorted()
________________________________________
9.What is the syntax of a lambda function?</br>Answer:lambda arguments: expression
________________________________________
Dictionary in Python
10.  What is a dictionary in Python?</br>Answer:A dictionary is a key-value pair data structure. Keys must be unique and immutable, while values can be of any type.
________________________________________
11.  What happens if you try to access a key that doesn't exist?</br>Answer:Python raises a KeyError. To avoid this, you can use the .get() method.
________________________________________
12.  Can dictionary keys be mutable types like lists?</br>Answer:No. Keys must be immutable types like strings, numbers, or tuples. Lists and other dictionaries cannot be used as keys.
----------------------------------------------
13.Why Use List & Dict Together in CRUD?</br>Answer:In FastAPI, when you're not using a database yet, you need a way to store and manage multiple data entries



