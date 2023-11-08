# Assignment: Add comments to the following code to make it easier to understand

# Importing the time and os modules
from time import sleep
import os

# Defining the clear function
def c():
    os.system('cls' if os.name == 'nt' else 'clear')

# Defining the main function
def main():
    while True:
        # Clears the screen and displays the start menu
        c()
        print("Welcome // The road trip")
        print("The goal of this game is to make it to your destination")
        print("1. Start")
        print("2. Exit")
        choice = input(">> ")
        # If the user chooses 1 then the game starts
        if choice == "1":
            # Clears the screen and displays the first part of the game
            c()
            print("buzzzzz")
            sleep(1)
            print("buzzzzz")
            sleep(1)
            print("You wake up to the sound of your alarm")
            print("You look at your phone and see that it is 6:00 AM")
            print("Do you wake up or go back to sleep?\n 1. Wake up\n 2. Go back to sleep")
            # Ask the user if they want to wake up or go back to sleep
            choice = input(">> ")
            if choice == "1":
                c()
                print("You wake up and... \n 1. Get ready \n 2. Pack your bags")
                # Ask the user if they want to get ready or pack their bags
                choice = input(">> ")
                if choice == "1":
                    print("Your are now ready to go. Do you pack your bags or leave? \n 1. Pack your bags \n 2. Leave")
                    # Ask the user if they want to pack their bags or leave
                    choice = input(">> ")
                    if choice == "1":
                        print("Your bags are now packed")
                        sleep(1)
                        leave()
                    elif choice == "2":
                        leave()
                elif choice == "2":
                    c()
                    print("You pack your bags and... \n 1. Get ready \n 2. Leave")
                    # Ask the user if they want to get ready or leave
                    choice = input(">> ")
                    if choice == "1":
                        print("Your are now ready to go.")
                        leave()
                    elif choice == "2":
                        leave()   
            elif cloice == "2":
                c()
                print("You wake up at 8:00 AM to your friends at the door")
                print("Do you get ready to go or leave? \n 1. Get ready \n 2. Leave")
                # Ask the user if they want to get ready or leave
        # If the user chooses 2 then the program exits
        elif choice == "2":
            break
        # If the user chooses anything else then the program tells them that it is an invalid option
        else:
            print("Invalid option")
            sleep(2)
            main()

# Defining the leave function
def leave():
    c()
    print("You are now on the road with your friends and you finily tell them where you are all going?")
    print("Where are you going?")
    # Ask the user where they are going
    destination = input(">> ")
    sleep(2)
    c()
    print("On your way to " + destination + " You are stopped at a red light for 10 minutes")
    print("Do you wait or continue? \n 1. Wait \n 2. Continue")
    # Ask the user if they want to wait or continue
    choice = input(">> ")   
    if choice == "1":
        print("You wait at the light for another 10 minutes and then a cop pulls up to direct traffic")
        print("You are now on your way to " + destination)
        sleep(2)
        c()
        print("after a bit more driving you make it to "+ destination)
        sleep(2)
        c()
        # The game ends
        # Asks the user if they want to play again
        print("Play again? \n 1. Yes \n 2. No")
        choice = input(">> ")
        if choice == "1":
            main()
        elif choice == "2":
            print("Goodbye")
            sleep(2)
            exit()
    elif choice == "2":
        print("As you continue you get hit by another car")
        print("You and your friends are all right but your car is totaled. You can no longer go to " + destination)
        sleep(2)
        c()
        # The game ends
        # Asks the user if they want to play again
        print("Play again? \n 1. Yes \n 2. No")
        choice = input(">> ")
        if choice == "1":
            main()
        elif choice == "2":
            print("Goodbye")
            # Waits 2 seconds
            sleep(2)
            # Exits the program
            exit()
# Calling the main function
main()