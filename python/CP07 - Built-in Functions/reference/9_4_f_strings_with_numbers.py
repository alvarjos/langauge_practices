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
When using f-strings, and you have an int or float inserted into the string,
You can use a colon : and then anything after the colon is instructions for
formatting the int/float. You can even round doing this.
'''

# Adding commas
# print "This is my formatted number {example_number}
# but make it have commas by adding :,
example_number = 100456.3257
print(f"This is my formatted number: {example_number:,}")

# rounding
example_number = 100456.3257
print(f"This is my formatted number: {example_number:,.2f}")

#or it can add decimals to an int
example_number_2 = 12345
print(f"This is my formatted number: {example_number_2:,.2f}")

#percents
testNumber = .87
testString = "{:%}".format(testNumber)
print(".87 as a percent:", testString, "\n")

# more percents
testNumber = .87465
testString = "{:.2%}".format(testNumber)
print(".87465 as a percent with 2 decimals:", testString, "\n")

# you can also use it to help with spacing
testNumber = 12345
testString = "{:10d}".format(testNumber)
print("10d with 5 digit number means 5 extra spaces", "\n")
print(testString)

# align it in different ways with < for left > for right and ^ for center
testNumber = 12345
testStringLeft = "{:<10d}".format(testNumber)
testStringRight = "{:>10d}".format(testNumber)
testStringCenter = "{:^10d}".format(testNumber)
print("10d with different alignments:", "\n")
print(testStringRight)
print(testStringLeft)
print(testStringCenter)