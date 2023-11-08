input_string = input("Enter a string: ")
input_string = input_string.replace(" ", "")
input_string = input_string.lower()
reverse_string = input_string[::-1]
if input_string == reverse_string:
    print("It's a palindrome")
else:
    print("It's not a palindrome")