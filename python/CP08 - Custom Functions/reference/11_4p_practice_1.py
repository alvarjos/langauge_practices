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




## VERSION 1:
def functionName1():
    print("Welcome to class")

# calling the first function. No parameters required
functionName1()

## VERSION 2:
# now we have a variable we are passing in:
def functionName2(sName):
    print("Welcome to class, " + sName + "!")

sExampleName = "Jacob"
functionName2(sExampleName)

## VERSION 2.1
# I didn't originally ask about this, but someone asked about default values:
# this will work with or without passing a variable now.
def functionName2_1(sName = "Jacob"):
    print("Welcome to class, " + sName + "!")

sExampleName = "James"
functionName2_1(sExampleName) # we can pass a variable
functionName2_1()

## VERSION 3:
# This function recieves a name as the input and returns the very first letter of the name as an ouput
def functionName3(sName = "jacob"):
    print("Welcome to class, " + sName + "!")
    firstNameLetter = sName[0]
    return(firstNameLetter)

sExampleName = "James"
print("This is the first letter of my name:" +  functionName3(sExampleName)) 



