imput = input("Enter a message to encrypt: ")
shift = int(input("Enter a shift value: "))
output = ""

for char in imput:
    if not char.isalpha():
        output += char
    elif char.isupper():
        output += chr((ord(char) + shift - 65) % 26 + 65)
    else:
        output += chr((ord(char) + shift - 97) % 26 + 97)

print(output)