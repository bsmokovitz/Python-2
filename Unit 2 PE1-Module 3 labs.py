# solution - 3.1.1.4

n = int(input("Enter a number: "))
print(n >= 100)

# solution - 3.2.1.3

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
n = int(input("Enter a number: "))
while n != secret_number:
    print("Ha ha! You're stuck in my loop!")
    n = int(input("Enter a number: "))
print("Well done, muggle! You are free now.")

# solution - 3.2.1.6

import time


for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")


# solution - 3.2.1.14

blocks = int(input("Enter the number of blocks: "))

height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1

print("The height of the pyramid:", height)

# solution - 3.1.1.6

hat_list = [1, 2, 3, 4, 5]

hat_list[2] = int(input("Enter a number: "))
print(hat_list)

del hat_list[-1]
print(hat_list)

print(len(hat_list))

# solution - 3.6.1.9

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
my_list = new_list

print("The list with unique elements only:")
print(my_list)


