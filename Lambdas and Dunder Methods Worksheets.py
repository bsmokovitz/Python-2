# Lambdas methods
# 1
add = lambda x, y: x + y
# 2
subtract = lambda x, y: x - y
# 3
multiply = lambda x, y: x * y
# 4
divide = lambda x, y: x / y
# 5
is_even = lambda x: x % 2 == 0
# 6
is_odd = lambda x: x % 2 != 0  
# 7
square = lambda x: x ** 2
# 8
cube = lambda x: x ** 3
# 9
starts_with = lambda x, y: x.startswith(y)
# 10
ends_with = lambda x, y: x.endswith(y)
# 11
to_upper = lambda x: x.upper()
# 12
to_lower = lambda x: x.lower()
# 13
concatenate = lambda x, y: x + y
# 14
string_length = lambda x: len(x)
# 15
contains_substring = lambda x, y: y in x
# 16
is_empty_list = lambda x: len(x) == 0
# 17
list_contains = lambda x, y: y in x
# 18
find_max = lambda x: max(x)
# 19
find_min = lambda x: min(x)
# 20
sort_list = lambda x: sorted(x)


# Dunder methods

# Exercise 1
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and is in grade {self.grade}."
    
    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.grade})"
    
    def __add__(self, other):
        return self.age + other.age
    
    def __len__(self):
        return self.age

# Exercise 2
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"This car is a {self.year} {self.make} {self.model}."
    
    def __repr__(self):
        return f"Car({self.make}, {self.model}, {self.year})"
    
    def __add__(self, other):
        return self.year + other.year
    
    def __len__(self):
        return self.year

# Exercise 3
class Book:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date
    
    def __str__(self):
        return f"{self.title} by {self.author} was published in {self.publication_date}."
    
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.publication_date})"
    
    def __add__(self, other):
        return self.publication_date + other.publication_date
    
    def __len__(self):
        return self.publication_date

