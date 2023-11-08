#1 Create a program called checkGuess() with one parameter for the guess. You will need a variable for a secret number inside the function. If the guess is greater than the secretNumber then you need to return a string saying it’s too high. If the guess is less than the secretNumber return too low. If the guess is the same as the secretNumber, return a string congratulating the user.

#In your main area you should get a guess using the input function. Call the checkGuess() function and output the hint/win message in a print statement.
secretNumber = 17
def checkGuess(guess):
    if guess > secretNumber:
        return "Too high"
    elif guess < secretNumber:
        return "Too low"
    else:
        return  "Congradulations"
    
while True:
    guess = int(input("Enter a number: "))
    if guess == secretNumber:
        print(checkGuess(guess))
        break
    else:
        print(checkGuess(guess))
        continue

#2 Create a program called iceCream() with two parameters for flavor and number of scoops. The program should use if, elif and else to display the following output.
#Print the following given the input
#Chocolate
#“Chocolate is my favorite too. You are getting [number] scoops.”
#Strawberry
#“You are getting [number] scoops of Strawberry. Sweet!”
#Vanilla
#“Vanilla is awesome! You are getting [number] scoops.”
#Else
#“You would like [number] scoops of [flavor].”

def iceCream(flavor, scoops):
    if flavor == "Chocolate":
        print("Chocolate is my favorite too. You are getting {scoops} scoops.")
    elif flavor == "Strawberry":
        print("You are getting {scoops} scoops of Strawberry. Sweet!")
    elif flavor == "Vanilla":
        print("Vanilla is awesome! You are getting {scoops} scoops.")
    else:
        print(f"You would like {scoops} scoops of {flavor}.")

flavor = input("What flavor would you like? ")
scoops = int(input("How many scoops would you like? "))
iceCream(flavor, scoops)
