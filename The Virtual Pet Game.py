import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Pet:
    def __init__(self, name, species, hunger, happiness, health):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.happiness = happiness
        self.health = health

    def __str__(self):
        return f"""
        Name: {self.name}
        Species: {self.species} 
        Hunger: {self.hunger}
        Happiness: {self.happiness}
        Health: {self.health}
        """
        # return f"{self.name} {self.species} {self.hunger} {self.happiness} {self.health}"

class User:
    def __init__(self, username):
        self.username = username
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def __str__(self):
        return f"{self.username} {self.pets}"
    
def main():
    user = User(input("Enter your username: "))
    while True:
        clear()
        print("1. Adopt a Pet")
        print("2. Interact with a Pet")
        print("3. Exit")
        choice = input("Enter your choice: ")
        clear()
        if choice == "1":
            name = input("Enter the pet's name: ")
            species = input("Enter the pet's species: ")
            user.add_pet(Pet(name, species, 10, 10, 10))
        elif choice == "2":
            if len(user.pets) == 0:
                clear()
                print("You have not adopted any pets yet.")
                time.sleep(2)
            else:
                clear()
                print("Select a pet:")
                for i in range(len(user.pets)):
                    print(f"{i + 1}. {user.pets[i].name}")
                while True:
                    pet_choice = input("Enter your choice: ")
                    if pet_choice.isdigit():
                        pet_choice = int(pet_choice)
                        if pet_choice >= 1 and pet_choice <= len(user.pets):
                            break
                    print("Invalid choice.")
                clear()
                print("1. Feed")
                print("2. Play")
                action_choice = input("Enter your choice: ")
                pet_choice = int(pet_choice)
                if action_choice == "1":
                    user.pets[pet_choice - 1].hunger -= 1
                elif action_choice == "2":
                    user.pets[pet_choice - 1].happiness += 1
                print(user.pets[pet_choice - 1])
                time.sleep(2)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            clear()
            print("Invalid choice.")
            time.sleep(2)

main()

    
