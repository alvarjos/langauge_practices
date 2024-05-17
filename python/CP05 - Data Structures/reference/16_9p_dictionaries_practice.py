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

# Create a dictionary for fruit inventory
fruit_inventory = {"Apples": 20, "Bananas": 50, "Cherries": 30, "Dates": 15, "Elderberries": 40}

# Print the entire dictionary
print("Current inventory:", fruit_inventory)

# Find the quantity of "Apples"
print("Quantity of Apples:", fruit_inventory.get("Apples", "Fruit not found"))

# Add a new fruit to the inventory
fruit_inventory["Figs"] = 25
print("Added Figs:", fruit_inventory)

# Update the quantity of an existing fruit
fruit_inventory["Bananas"] = 60
print("Updated Bananas quantity:", fruit_inventory)

# Remove a fruit from the inventory
removed_fruit_quantity = fruit_inventory.pop("Dates", "Fruit not in inventory")
print("Removed Dates:", removed_fruit_quantity)

# Check the quantity of a fruit
print("Quantity of Cherries:", fruit_inventory.get("Cherries", "Fruit not in inventory"))

# Add a new fruit with its quantity if it does not exist
fruit_inventory.setdefault("Grapes", 50)
print("Added Grapes (if not present):", fruit_inventory)

# Print only the names of the fruits
print("Fruits available:", list(fruit_inventory.keys()))

# Print only the quantities of each fruit
print("Quantities available:", list(fruit_inventory.values()))

# Check if "Oranges" are available
if "Oranges" in fruit_inventory:
    print("Oranges are available!")
else:
    print("Oranges are not available!")
