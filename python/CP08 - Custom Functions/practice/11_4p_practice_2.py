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

# write a function that accepts 2 numbers, then divides
# the first by the second and multiplies it by 100
# don't worry about cases where you'd divide zero.
# just ignore that possibility. this is just simple practice.
