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

    Define a function with def
    Then call it afterwards by writing the function name with parentheses

    A function is just stored code that you can reuse!

'''


# Practice:
# write a function called simpleFunction
# it should just print out "Wow this is a simple function" on one line
# and "Wow this is another line" after that.
# then call the function 3 times


