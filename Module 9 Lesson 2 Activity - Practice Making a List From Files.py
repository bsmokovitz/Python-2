# For this activity complete your code in the CodeHS Sandbox and share the share link for this assignment. Make sure that the show code and public boxes are both checked.

# Sandbox SolutionLinks to an external site.

# Making a List From a File

# Create a Sandbox Python 3 Program named FirstName-LastInitial Mod9 Les2 Practice
# Download this CSV fileLinks to an external site. of female Oscar winners and open it into a text editor on your computer
# Add a text file to your sandbox project named OscarWinnersFemales.txt 
# Copy and paste several lines from the original file into your sandbox file. Make sure that you include the header.
# Write a Python program that does the following:
# Open the file and store the file object in a variable
# Read the entire contents line by line into a list and strip away the newline character at the end of each line
# Using list slicing, print lines 4 through 7 of your file
# Write code that will ask the user for an actress name and then search the list to see if it is in there. If it is it will display the record and if it is not it will display Sorry not found.
# Close the file
# Submit the sandbox share link.

file = open("OscarWinnersFemales.txt", "r")
print(file)
list = file.readlines()
print(list[3:7])
file.close()
name = input("Enter an actress name: ")
if name in list:
    print(list)
else:
    print("Sorry not found.")
    