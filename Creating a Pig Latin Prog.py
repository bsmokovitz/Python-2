def pig(imput):
    if imput[0] in "aeiou":
        return imput + "yay"
    else:
        return imput[1:] + imput[0] + "ay"
    
while True:
    imput = input("Enter a word or quit: ")
    if imput == "quit":
        break
    else:
        print(pig(imput))