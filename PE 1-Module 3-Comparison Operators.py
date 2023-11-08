# Python Institute-Making Decisions in PythonLinks to an external site.
# Read the Module 3 slides 3.1.1.2-3.1.1.14 in Python Institute and complete the following labs

# LAB #1-3.1.1.4
# Objectives
# becoming familiar with the input() function;
# becoming familiar with comparison operators in Python.
# Scenario 
# Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.

# Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.

#Solution
n = int(input("Enter a number: "))
print(n >= 100)


# LAB #2-3.1.1.10
# Objectives
# becoming familiar with the input() function;
# becoming familiar with comparison operators in Python;
# becoming familiar with the concept of conditional execution.
# Scenario
 

# Write a program that utilizes the concept of conditional execution, takes a string as input, and:

# prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

# solution
plant = input("Enter the plant name: ")
if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", plant, "!")



# LAB  #3-3.1.1.11
# Objectives
# Familiarize the student with:

# using the if-else instruction to branch the control path;
# building a complete program that solves simple real-life problems.
# Scenario
# Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# Your task is to write a tax calculator.

# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
# Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.

# solution
income = float(input("Enter the annual income: "))
tax = 0
if income <= 85528:
    tax = (income * 0.18) - 556.02
else:
    tax = 14839.02 + ((income - 85528) * 0.32)
if tax < 0:
    tax = 0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")


# LAB # 4-3.1.1.12
# Objectives
# Familiarize the student with:

# using the if-elif-else statement;
# finding the proper implementation of verbally defined rules;
# testing code using sample input and output.
# Scenario
# As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
# Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.

# The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

# It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

# solution
year = int(input("Enter a year: "))
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4:
        print("Common year")
    elif year % 100:
        print("Leap year")
    elif year % 400:
        print("Common year")
    else:
        print("Leap year")