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


# for loops

'''
Useful in two main situations:
    - You have an iterable variable (list, dictionary, range, string, etc. An iterable just means a variable with other variables inside it)
      and you want to repeat code for however many things are in that iterable variable

    - You want to repeat something x times. Like "do this 5 times". You usually would use a range variable to do that.

'''
# structure of for loops:
'''
    for looping_variable in iterable_variable:
        code that will repeat

    for:
        always there

    looping_variable:
        you make this variable name up on the spot. It will represent every individual element in the iterable_variable
        sometimes called the iterator variable

    iterable_variable:
        this is the range, list, etc that you want to loop through
'''

# Practice:
# given a list of names, for each name,
# print out "This is the character's name: " and then the character's name

example_list = ["Harry", "Hermione", "Ronald", "Luna"]

for name in example_list:
    print(f"This is the character's name: {name}")

# Practice:
# given a dictionary, do:
    # a for loop that prints out just the keys (default)
    # a for loop that prints out just the values (use .values(), or put the keys back in the dictionary)
    # a for loop that prints out the keys and values (use .items())

grade_dict = {"A": 4.0, "A-": 3.7, "B+": 3.4, "B": 3.0}

# just the keys:
for key in grade_dict:
    print(key)

# just the values:
for value in grade_dict.values():
    print(value)

# keys and values:
for key, value in grade_dict.items():
    print(f"This is the key: {key}. This is the value: {value}")


# strings are iterables too!
# not as common to loop through, but you can:

# practice: 
# print out each individual character in the word "Supercalifragilisticexpialidocious"
poppins_word = "Supercalifragilisticexpialidocious"

for character in poppins_word:
    print(character)

# for iCount in range(1, 5) :
#     print("First Example: ", "The count is", iCount)

# # before going forward, let's explain the range() function
# # range() creates a range object. For example:
# print(type(range(5)))

# in a range object you can specify the:
'''
    range(stopping point)
    range(starting point, stopping point)
    range(starting point, stopping point, step value)
'''

# # basically, the point is to create something that gives a range to loop through.
# # here are some example of each

# # range(stopping point). this starts at zero and goes to the stopping point,
# # but doesn't include the stopping point
# for iCount in range(5) :
#     print("Range(stopping point)", "The count is", iCount)

# # range(staring, stopping). starts wherever you tell it, stops before the stopping point
# for iCount in range(1,5) :
#     print("Range(starting point, stopping point)", "The count is", iCount)

# # same as above but moves in increments dictated by the step value
# for iCount in range(3,10,2) :
#     print("Range(starting point, stopping point, step)", "The count is", iCount)

# Example from textbook
# Note: you can highlight the text and use
# ctrl + / (windows) or cmd + / to comment or uncomment things in bulk
# iNumStudents = int(input("How many students? "))

# # notice that I am adding one to iNumStudents
# for iCounter in range(1, iNumStudents +1) :
#     sFullName = input("\n\t\t\tWhat is student " + str(iCounter) + "'s full name: ")
    
#     print("Welcome", sFullName, "\n")


# strings are iterables too!
iCount = 1
sFullName = input("enter a name: ")
for sChar in sFullName :
    print(iCount, sChar)
    iCount += 1


# Quick Practice:
'''
    Create a Python program that asks the user to enter an integer n. Then, use a for loop to print the first n square numbers starting from 1.

    Example
    If the user enters 5, your program should print:

    1
    4
    9
    16
    25
'''

# Get input from the user
n = int(input("Enter an integer: "))

# Use a for loop to print the first n square numbers starting from 1
for i in range(1, n + 1):
    print(i * i)

