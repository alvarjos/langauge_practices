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
    1st step: Write a function that prints out
    "Welcome to class!" and then call the function
'''


'''    2nd step: Write a function that accepts a parameter with your name. Insert your name
        into the function and have it print "Welcome to class, yourName!"
        
'''

'''
3rd step: Write a function that accepts a parameter with your name. 
        keep the function printing "Welcomee to class, yourName!" but also return the first letter of your name.
        Hint: for any string you can do sVariable[0] to get the first letter.

        Then outside of your function, print out "This is the first letter of my name: x"
'''





