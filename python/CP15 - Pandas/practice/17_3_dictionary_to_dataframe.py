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

import pandas as pd
    
# dictionary with two lists
lstNames =  {"Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
             "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"]}

# create a dataframe using the dictionary, then print it out. Notice the column names!


'''
To remember:
    - The lists in the dictionary have to have the same number of values (like Type can't have 10 types, and then Dancer only has 8 dancers)
    - Easiest way to get around this for now is to just insert blank strings or None for empty values.
'''