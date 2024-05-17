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


import math
# math is part of the "standard library" of
# python functions. It isn't automatically loaded, but it was downloaded when you downloaded the python interpreter.
# usually, you import everything you need at the top of the python file,
# but it just needs to come before the code that references it.

'''
BUILT-IN FUNCTIONS.

Tons of them. You'll become familiar with many,
but some you'll forget the exact syntax for. Just google when you forget
That's what people in the real world do.

'''


# absolute value (abs)
# Find the absolution value of -5


# max()
# return the largest number in example_list:
example_list = [10, 4, 50, 10]
print(max(example_list))

# min()
# return smalles number in example_list:
example_list = [10, 4, 50, 10]
print(min(example_list))

# sum()
# adds up a list
example_list = [10, 4, 50, 10]
print(sum(example_list))

# round()
# round 5.6789 to the 2nd decimal
print(round(5.6789,2))

########
# Math library
########

# uses the "import math" from the top of the file.
# useful for some more complex functions, I'll just show a few here.

# math.ceil()
# give the next highest integer value of 11.3:
print(math.ceil(11.3))

# math.floor()
# give the next lower integer value of 11.3:
print(math.floor(11.3))

# math.factorial()
# give the factorial (4! or 4x3x2x1)
print(math.factorial(4))

# math.sqrt()
# find the square root of 16:
print(math.sqrt(16))

# math.trunc()
# truncates anything past the decimal: 36.7
print(math.trunc(36.7))



