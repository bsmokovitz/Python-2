# Assignment 1: Math Module

# Objective: Practice using functions from the math module to perform mathematical operations.

# Write a Python program that calculates and prints the square root of a given number using the math.sqrt() function.
import math
number = float(input("Enter a number: "))
square_root = math.sqrt(number) 
print("Square root of", number, "is", square_root)

# Create a program that calculates and displays the value of pi (π) using the math.pi constant.
import math
print("The value of pi is", math.pi)

# Build a program that calculates the area of a circle. Prompt the user for the radius and use the math.pi constant and math.pow() function to calculate the area.
# Extend the previous program to calculate both the area and circumference of a circle.
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * math.pow(radius, 2)
print("Area of the circle is", area)
circumference = 2 * math.pi * radius
print("Circumference of the circle is", circumference)


# Assignment 2: Random Module

# Objective: Practice generating random numbers and working with the random module functions.

# Write a Python program that generates and prints a random integer between 1 and 10 using the random.randint() function.
import random
random_integer = random.randint(1, 10)
print("Random integer between 1 and 10 is", random_integer)

# Create a dice-rolling simulator that generates and displays the result of rolling a six-sided die using random.randint(1, 6).
import random
dice_roll = random.randint(1, 6)
print("Dice roll is", dice_roll)

# Build a program that randomly selects a name from a list of names. Define a list of names, and use the random.choice() function to select and print a random name.
import random
names = ["John", "Mary", "Bob", "Mosh", "Sarah"]
random_name = random.choice(names)
print("Random name is", random_name)


# Create a card-shuffling program. Define a list of playing cards (e.g., "Ace of Hearts," "King of Spades") and use the random.shuffle() function to shuffle the cards. Print the shuffled deck.
import random
cards = ["Ace of Hearts", "King of Spades", "Queen of Diamonds", "Jack of Clubs"]
random.shuffle(cards)
print("Shuffled deck is", cards)

# Assignment 3 (Combined Math and Random):

# Objective: Combine knowledge of the math and random modules to solve a problem.

# Ask the user for a number representing the radius of a circle.
# Calculate the area of the circle using the math.pi constant and the math.pow() function.
# Use the random.uniform() function to generate a random floating-point number between 0 and 1.
# Multiply the area of the circle by the random number generated in step 3.
# Display the result as the "adjusted area" of the circle.

import math
import random
radius = float(input("Enter the radius of the circle: "))
area = math.pi * math.pow(radius, 2)
random_number = random.uniform(0, 1)
adjusted_area = area * random_number
print("Adjusted area of the circle is", adjusted_area)



# Assignment 4 (Challenge):

# Objective: Create a more complex program that uses both modules creatively.

# Design a mini-quiz game where the computer generates random math problems for the user to solve. Here are the steps:

# Randomly generate two numbers between 1 and 20 using the random.randint() function.
# Randomly select an operator (+, -, *, or /).
# Present the math problem to the user (e.g., "What is 7 + 3?").
# Prompt the user for an answer.
# Check if the user's answer is correct.
# Keep track of the user's score and display it at the end.
# This assignment will require students to use the random module to generate numbers and the math module for basic arithmetic operations.

# These assignments provide hands-on practice for students to reinforce their understanding of the math and random modules and to develop problem-solving skills in Python.
import random
import math
score = 0

for i in range(5):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*", "/"])
    print("What is", num1, operator, num2, "?")
    answer = float(input("Enter your answer: "))
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    if answer == result:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
print("Your score is", score)

