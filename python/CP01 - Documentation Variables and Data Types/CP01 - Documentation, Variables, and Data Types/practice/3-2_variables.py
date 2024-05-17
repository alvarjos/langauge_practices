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

# variables

'''
When programming you will need to store data and manipulate it.
You store data in variables

Think of variables as buckets that hold whatever you put into them.

You give the bucket (the variable) a name, and then an = and then the value to store into it.

'''

# create a varaible called age, and put a number into it:

age = 21
Age = 25
'''
rules for variable names:

    - variable names are case sensitive. Age and age will be two different variables
    - the starting character must be a letter or an underscore. You can use a number, just not at the start
    - some characters, like "!" also can't be used in the variable name
'''

# create a variable for your grandfather's age and store a number in it.

grandfathers_age = 80


'''
This is getting into chapter 4, but if you want to display the variable you typed out, you can use
print(variable_name)

'''

# print out the first age variable name you made, then print out the grandfather one

message = 'Hello World!'
print(message) 
print('my grandfathers age is') print(grandfathers_age)

