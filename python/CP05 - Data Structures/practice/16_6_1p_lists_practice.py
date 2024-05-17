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


