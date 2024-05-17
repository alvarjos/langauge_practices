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

# sometimes, You may want to store a list inside of a list! #inception


# Characters from Harry Potter
harry_potter_characters = [
    "Harry Potter", "Hermione Granger", "Ron Weasley",
    "Albus Dumbledore", "Severus Snape", "Voldemort",
    "Sirius Black", "Dobby", "Luna Lovegood", "Draco Malfoy"
]

# Characters from Lord of the Rings
lord_of_the_rings_characters = [
    "Frodo Baggins", "Samwise Gamgee", "Aragorn",
    "Legolas", "Gandalf", "Gimli", "Boromir",
    "Sauron", "Galadriel", "Saruman"
]

# Characters from Super Mario
super_mario_characters = [
    "Mario", "Luigi", "Princess Peach", "Bowser",
    "Yoshi", "Toad", "Donkey Kong", "Wario",
    "Waluigi", "Princess Daisy"
]

# create a list called list_of_character_lists, and put each of the 3 above lists inside it:
list_of_character_lists = [harry_potter_characters, lord_of_the_rings_characters, super_mario_characters]

# try printing out the 3rd Lord of the Rings character.
print(list_of_character_lists[1][2])



### basic sorting

print(harry_potter_characters)

# reverse the order of the characters using .reverse()
harry_potter_characters.reverse()
print(harry_potter_characters)

# you can sort any list using .sort()
# (but it should only be of comparable data types. No lists of ints and strings)

harry_potter_characters.sort()
print(harry_potter_characters)

#sort_them reversed using .sort(revers=True):
harry_potter_characters.sort(reverse=True)
print(harry_potter_characters)


# You can get much more complicated with sorting, even using custom functions to sort things on.
# Here's an example using len. We won't go into details on this or do complicated sorting in this class
# but you should be aware it is totally possible.

harry_potter_characters.sort(key = len, reverse=True)
print(harry_potter_characters)



