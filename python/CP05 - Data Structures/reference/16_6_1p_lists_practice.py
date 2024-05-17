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
Practice Problem: Favorite Foods List
Objective: Create a list of your favorite foods and manipulate it using list methods.
'''
# Tasks:
#     - Create a list named favorite_foods and fill it with at least five of your favorite foods.
#     - Print out the entire list.
#     - Use indexing to print out your top 2 favorite foods individually.
#     - Add a new favorite food to the end of your list using .append().
#     - Insert a new food at the beginning of your list using .insert().
#     - Print the length of your list using len().
#     - Use .pop() to remove the last food in your list and print the name of the food that was removed.
#     - Check if "Pizza" is in your list. If it is, print "Pizza is one of my favorites too!"
#     - Print out a range of foods from your list, for example, the 2nd to the 4th foods.


# Create a list of favorite foods
favorite_foods = ["Pizza", "Ice Cream", "Chocolate", "Pasta", "Sushi"]

# Print the entire list
print("My favorite foods are:", favorite_foods)

# Print the top 2 favorite foods using indexing
print("My top favorite food is:", favorite_foods[0])
print("My second favorite food is:", favorite_foods[1])

# Add a new favorite food to the end of the list
favorite_foods.append("Tacos")
print("Added a new favorite food:", favorite_foods)

# Insert a new food at the beginning of the list
favorite_foods.insert(0, "Burgers")
print("Added a new food at the beginning:", favorite_foods)

# Print the length of the list
print("I have", len(favorite_foods), "favorite foods.")

# Remove the last food in the list and print the name of the food that was removed
removed_food = favorite_foods.pop()
print("I removed", removed_food, "from my list.")

# Check if "Pizza" is in the list
if "Pizza" in favorite_foods:
    print("Pizza is one of my favorites too!")

# Print out a range of foods from the list
print("Some of my favorite foods are:", favorite_foods[1:4])  # This will print the 2nd to the 4th foods
