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
    you can give functions arguments. To do this,
    define a parameter after the function name when defining the function

'''

# Write a function that allows you to pass text to it as an argument.
# Then print out that text with "This is your message: " before the text passed as an argument




# What happens if you don't provide an argument?



# Make a new function that does the same thing, but add a default value of "this is the default" for the parameter .


