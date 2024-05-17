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

# print(f"This is the character's name: {example_list[0]}")
# print(f"This is the character's name: {example_list[1]}")
# print(f"This is the character's name: {example_list[2]}")
# print(f"This is the character's name: {example_list[3]}")

for name in example_list:
    print(f"This is the character's name: {name}")

# Practice:
# given a dictionary, do:
    # a for loop that prints out just the keys (default)
    # a for loop that prints out just the values (use .values(), or put the keys back in the dictionary)
    # a for loop that prints out the keys and values (use .items())

grade_dict = {"A": 4.0, "A-": 3.7, "B+": 3.4, "B": 3.0}

# just the keys:
for letter_grade in grade_dict:
    print(letter_grade)

# just the values:
for value_numerical_grade in grade_dict.values():
    print(value_numerical_grade)

print(grade_dict.items)
# var1, var2 = ["string 1", "string 2"]

# keys and values (remember unpacking):
for key, value in grade_dict.items():
    print(f"This is the key: {key}, this is the value: {value}")

# strings are iterables too!
# not as common to loop through, but you can:

# practice: 
# print out each individual character in the word "Supercalifragilisticexpialidocious"
poppins_word = "Supercalifragilisticexpialidocious"

for character in poppins_word:
    print(character)




