input1 = input("Enter first word: ")
input2 = input("Enter second word: ")

input1 = input1.lower()
input2 = input2.lower()

input1 = input1.replace(" ", "")
input2 = input2.replace(" ", "")

input1 = sorted(input1)
input2 = sorted(input2)

if input1 == input2:
    print("Anagrams")
else:
    print("Not anagrams")