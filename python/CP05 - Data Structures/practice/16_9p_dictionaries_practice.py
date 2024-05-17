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

'''
Practice Problem: Fruit Market Inventory
Objective: Create a dictionary to manage the inventory of a fruit market and perform various operations on it.
'''
# Tasks:
#     - Create a dictionary named fruit_inventory where the keys are the names of fruits and the values are the quantities available. Add at least five fruits with their quantities.
#     - Print the entire dictionary.
#     - Find the quantity available for "Apples" and print it. Use the method that handles the case where the key might not exist, providing a default message like "Fruit not found."
#     - Add a new fruit to the inventory with its quantity.
#     - Update the quantity of an existing fruit.
#     - Remove a fruit from the inventory using .pop() and print the name of the fruit along with the quantity removed.
#     - Use .get() to check the quantity of a fruit. If the fruit is not in the inventory, it should return "Fruit not in inventory."
#     - Use .setdefault() to add a new fruit with its quantity to the inventory only if it does not already exist, and print the updated inventory.
#     - Print only the names of the fruits available in the market using .keys().
#     - Print only the quantities of each fruit using .values().
#     - Check if "Oranges" are available in the market. If yes, print a message saying "Oranges are available!"

fruit_inventory = {"Apples": 21, "Banannas": 12, "Oranges": 18, "Strawberries": 54, "Grapes": 32}
print(fruit_inventory)
print(fruit_inventory.get("Apples", "Fruit not found"))

fruit_inventory["Coconut"] = 32
fruit_inventory["Apples"] = 40
poppedFruit = fruit_inventory.pop("Strawberries")
print(f"Value of Strawberries: {poppedFruit}")
print(fruit_inventory)
print(fruit_inventory.get("Banannas", "Fruit not in Inventory"))
fruit_inventory.setdefault("Kiwi", 10)
print(fruit_inventory)





