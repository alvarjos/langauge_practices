# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################


# given this Person class and 3 person objects:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 35)

# 1: Create a dictionary to store the person objects.
#       Use the persons name as the key, and the entire object as the value

person_dict = {
    person1.name: person1,
    person2.name: person2,
    person3.name: person3
}
# 2: Using the dictionary, individually access each of the objects and run their print_info method

person_dict["Alice"].print_info()
person_dict["Bob"].print_info()
person_dict["Charlie"].print_info()

# 3: Make another person and add them to the dictionary
person_dict["Thomas"] = Person("Thomas", 50)

# 4: Loop through the dictionary of people and run the print_info method for each

for key in person_dict:
    person_dict[key].print_info()
