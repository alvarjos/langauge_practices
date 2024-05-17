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
Generate a Random Number: Generate a random number between 1 and 100. This is your "number of the day".

Choose a Random Color: pick a color from a predefined list of colors (e.g., ["Red", "Blue", "Green", "Yellow", "Purple"]).

Determine Lucky Day:
If the number is above 50 and the color is either Blue, Green, or Yellow, it's a "lucky day."
Otherwise, it's a "normal day."

Output: Print a message to inform the user whether it's a lucky day or a normal day based on the number and color.
Include the number and color they generated

'''
import random

# Generate a random number between 1 and 100
number = random.randrange(1, 101)

# Choose a random color from the list
color = random.choice(["Red", "Blue", "Green", "Yellow", "Purple"])

# Determine if it's a lucky day or a normal day
if number > 50 and color in ["Blue", "Green", "Yellow"]:
    message = "It's a lucky day!"
else:
    message = "It's a normal day."

# Output the result
print(f"Your number for today is {number}, and your color is {color}. {message}")
