import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Animal:
    def __init__(self, name, species, location, food_status, water_status, return_time, notes=""):
        self.name = name
        self.species = species
        self.location = location
        self.food_status = food_status
        self.water_status = water_status
        self.return_time = return_time
        self.notes = notes

    def update_location(self, new_location):
        self.location = new_location

    def update_food_status(self, status):
        self.food_status = status

    def update_water_status(self, status):
        self.water_status = status

    def update_return_time(self, new_time):
        self.return_time = new_time

    def update_notes(self, new_notes):
        self.notes = new_notes

    def display_info(self):
        return f"""
        Name: {self.name}
        Species: {self.species}
        Location: {self.location}
        Food Status: {self.food_status}
        Water Status: {self.water_status}
        Return Time: {self.return_time}
        Notes: {self.notes}
        """

class AnimalManager:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        for index, animal in enumerate(self.animals):
            print(f"{index + 1}. {animal.name} - {animal.species}")

    def get_animal_info(self, index):
        if 1 <= index <= len(self.animals):
            return self.animals[index - 1].display_info()
        else:
            return "Invalid animal choice."

    def update_animal(self, index, attribute, new_value):
        if 1 <= index <= len(self.animals):
            animal = self.animals[index - 1]
            if attribute == 1:
                animal.update_location(new_value)
            elif attribute == 2:
                animal.update_food_status(new_value)
            elif attribute == 3:
                animal.update_water_status(new_value)
            elif attribute == 4:
                animal.update_return_time(new_value)
            elif attribute == 5:
                animal.update_notes(new_value)
            else:
                return "Invalid attribute choice."
            return "Animal information updated!"
        else:
            return "Invalid animal choice."

def main():
    animal_manager = AnimalManager()

    while True:
        clear()
        print("1. Add Animal")
        print("2. Update Animal Information")
        print("3. View Animals")
        print("4. Exit")
        choice = input("Enter your choice: ")
        clear()

        if choice == "1":
            name = input("Enter the animal's name: ")
            species = input("Enter the animal's species: ")
            location = input("Enter the animal's location: ")
            food_status = input("Enter the food status: ")
            water_status = input("Enter the water status: ")
            return_time = input("Enter the return time: ")
            notes = input("Enter additional notes (if any): ")
            animal_manager.add_animal(Animal(name, species, location, food_status, water_status, return_time, notes))
            print("Animal added successfully!")
            time.sleep(2)

        elif choice == "2":
            if len(animal_manager.animals) == 0:
                clear()
                print("No animals added yet.")
                time.sleep(2)
            else:
                clear()
                animal_manager.display_animals()
                animal_choice = input("Select an animal to update: ")
                if animal_choice.isdigit():
                    animal_choice = int(animal_choice)
                    clear()
                    print(animal_manager.get_animal_info(animal_choice))
                    print("\n1. Update Location")
                    print("2. Update Food Status")
                    print("3. Update Water Status")
                    print("4. Update Return Time")
                    print("5. Update Notes")
                    attribute_choice = input("Choose the attribute to update: ")
                    new_value = input("Enter the new value: ")
                    if attribute_choice.isdigit():
                        attribute_choice = int(attribute_choice)
                        print(animal_manager.update_animal(animal_choice, attribute_choice, new_value))
                        time.sleep(2)
                    else:
                        print("Invalid attribute choice.")
                        time.sleep(2)
                else:
                    print("Invalid input.")
                    time.sleep(2)

        elif choice == "3":
            if len(animal_manager.animals) == 0:
                clear()
                print("No animals added yet.")
                time.sleep(2)
            else:
                clear()
                animal_manager.display_animals()
                animal_choice = input("Select an animal to view details: ")
                if animal_choice.isdigit():
                    animal_choice = int(animal_choice)
                    clear()
                    print(animal_manager.get_animal_info(animal_choice))
                    input("Press Enter to continue...")
                else:
                    print("Invalid input.")
                    time.sleep(2)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            clear()
            print("Invalid choice.")
            time.sleep(2)

main()
