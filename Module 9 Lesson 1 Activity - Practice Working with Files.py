myPoem = open("poem.txt", "r")
print(myPoem)
completePoem = myPoem.read()
print(completePoem)
myPoem.close()

# Add a text file named cities.txt
# Add the following cities to your file:
# Beijing
# Cairo
# London
# Nairobi
# New York City
# Sydney
# Tokyo
# Open the cities file and store the file object in the cityFile variable.
# Read the first 20 characters into a variable named first20.
# Print the first20 variable.
# Close the cityFile

cityFile = open("cities.txt", "r")
print(cityFile)
first20 = cityFile.read(20)
print(first20)
cityFile.close()

# PART 3 - Cities Revisited

# Open the cities file and store the file object in the cityFile2 variable.
# Using a loop read and print the first 3 lines in the city file
# Close the cityFile2.

cityFile2 = open("cities.txt", "r")
print(cityFile2)
for i in range(3):
    print(cityFile2.readline())
cityFile2.close()
