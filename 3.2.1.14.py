blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
while blocks > 0:
    height += 1
    blocks -= height
    if blocks < 0:
        height -= 1
        break

print("The height of the pyramid:", height)