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

# DATA TYPES

'''
string: for storing text

integer (or int): Whole numbers, no decimals

float: number w/ decimals

boolean: True or False. 


'''

# store you name in a variable
# you can use single or double quotes

Name = 'Angel' 


# store your age in a variable

Age = 21

# store how much money is in your pocket in a variable

cashOnHand = 4.5

# state whether you like bacon or not

bacon_liked = True

# if you want to see what the data type is:
# print(type(variableName))
# remember that python is dynamically typed! (instead of statically typed)

# PRACTICE #1
#   store an integer and a float in two separate variables. Print out their sum.
angels_Money = cashOnHand 
mekelis_Money = 100
totalmoney = angels_Money + mekelis_Money
message = "Our total money combined is: "


#snakecase: all lowercase, with an underscore
# variable_name = 2

# camel case: lowercase first, no spaces, then uppercase first letter 
# variableName = 2 

# pascal case: like camel, but start with capital letter 
# VariableName = 2

final_msg = message + "$" + str(totalmoney)
print(final_msg)
# print(totalmoney)



# Hungarian notation
iVariableName = 2
#i in iVariableName = integer 
fVariableName = 2.2
#f in fVariableName = float
# etc...


'''
Sometimes, people like to put the name of the datatype in the name of the variable
This is optional, but I recommend it if you want to keep track of what type it is
Just remember, don't name it something like iMoney if you are actually storing a Float
'''

