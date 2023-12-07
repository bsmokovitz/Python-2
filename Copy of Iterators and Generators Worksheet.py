# Python Iterators and Generators Worksheet
# Fill in the code sections marked with comments to complete each exercise.
# Example 1: Creating an Iterator
# Prompt:
# Create an iterator for a range of numbers from 1 to 5.
# class NumberIterator:
#  def __init__(self):
#  # Initialize variables here
#  pass

#  def __iter__(self):
#  # Make the object iterable
#  pass

#  def __next__(self):
#  # Define the logic to return the next element
#  pass

# # Test the iterator
# number_iterator = NumberIterator()
# for num in number_iterator:
#  print(num)

# Example 2: Creating a Generator
# Prompt:
# Write a generator function to yield even numbers up to 10.
# def even_numbers_generator():
#  # Define the logic to yield even numbers
#  pass

# # Test the generator
# for even_num in even_numbers_generator():
#  print(even_num)

class NumberIterator:
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number <= 5:
            return self.number
        else:
            raise StopIteration
        
number_iterator = NumberIterator()
for num in number_iterator:
    print(num)

def even_numbers_generator():
    number = 0
    while number <= 10:
        yield number
        number += 2

for even_num in even_numbers_generator():
    print(even_num)



# Example 3: Custom Iterator
# Prompt:
# Create an iterator for a custom iterable class that returns the length of words in a given sentence.
# class WordLengthIterator:
#  def __init__(self, sentence):
#  # Initialize variables here
#  pass

#  def __iter__(self):
#  # Make the object iterable
#  pass

#  def __next__(self):
#  # Define the logic to return the next element
#  pass

# # Test the iterator
# sentence_iterator = WordLengthIterator("This is a sample sentence.")
# for length in sentence_iterator:
#  print(length)

# Example 4: Yielding Squares
# Prompt:
# Write a generator function to yield squares of numbers from 1 to 5.
# def square_generator():
#  # Define the logic to yield squares
#  pass

# # Test the generator
# for square in square_generator():
#  print(square)

class WordLengthIterator:
    def __init__(self, sentence):
        self.words = sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.words:
            return len(self.words.pop(0))
        else:
            raise StopIteration
        
sentence_iterator = WordLengthIterator("This is a sample sentence.")
for length in sentence_iterator:
    print(length)

def square_generator():
    number = 1
    while number <= 5:
        yield number ** 2
        number += 1

for square in square_generator():
    print(square)



# Example 5: Infinite Generator
# Prompt:
# Create a generator function that generates an infinite sequence of Fibonacci numbers.

# def fibonacci_generator():
#  # Define the logic to yield Fibonacci numbers
#  pass

# # Test the generator
# count = 0
# for fib_num in fibonacci_generator():
#  print(fib_num)
#  count += 1
#  if count == 10:
#  break # Limit the output to 10 Fibonacci numbers

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

count = 0
for fib_num in fibonacci_generator():
    print(fib_num)
    count += 1
    if count == 10:
        break # Limit the output to 10 Fibonacci numbers




