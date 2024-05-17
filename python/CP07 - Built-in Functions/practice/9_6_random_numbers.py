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


import random 

'''
    we'll use this to:
    randomly select from a list
    randomly generate numbers

'''
# random.choice()
# randomly choose from a selection:
example_list = [1,2,3,4,5]


# random.randint()
# give random integer. Is inclusive on both sides
# get a random number between 0 and 10


# random.randrange()
# Like randint(), but EXCLUSIVE on the ENDING SIDE.
# Useful because you can also add a step amount
# get a random number between 0 and 10


# Do the same thing, but make it only 0, 2, 4, 6, 8, or 10


# random.uniform()
# if you want floats, use 



# if you don't want it to return something random, then use a seed 
# useful if you're trying to debug something and don't want it to change
# every time it runs while you're trying to find the problem.
fRandom = random.random() #Uses 3.14 as seed and returns 0.7754488379965433
print("should NOT always be the same:", fRandom)
random.seed(3.14)
fRandom = random.random() #Uses 3.14 as seed and returns 0.7754488379965433
print("should always be the same:", fRandom)