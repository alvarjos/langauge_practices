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

# Stuff to know:

    # Data structures are data types that let you store many variables inside of them.
    # Immutable: can't be changed. Once you create it, you have to destroy it and recreate it if you want to change it
    # Mutable: can be changed. You can update it whenever you want.


# Note: there are NO PRACTICE PROBLEMS in this file. This is meant to give a brief overview.
# the following files will let you practice using them.
# 4 data structures to know about:

# LISTS (care about this):
############
'''
    use square brackets []
    When in doubt, just use a list.
    Mutable, so you can add to them, delete things from them, update stuff from them, etc.
'''
# making a list using []
listExample = ['first thing', 'second thing', 'third thing']

# you can print the whole thing.
print(listExample)

# You can access individual items in the list:
print(listExample[0])

# You can change items in lists:
listExample[0] = "altered first thing"
print(listExample)

# you can add items to lists:
listExample.append('fourth thing')
print(listExample)

# TUPLES (only sorta care about this.
#          Know what they are, but I don't think you'll ever
#          create a tuple datatype on purpose in this class):
##############
'''
    use parentheses ()
    don't worry too much about these
    Immutable. They're like lists you can't change. Quicker in memory to work with, but we don't care too much about that in this stage of our learning
'''
# making a tuple
tupleExample = ('first thing', 'second thing', 'third thing')

print(tupleExample)
print(tupleExample[0])
# can't append :(
# only way to edit is to make a whole new variable and add to it:
newTupleExample = tupleExample + ("fourth thing",)
print(newTupleExample)


# DICTIONARIES (care about this)
#############

'''
    use curly braces and colons { : }
    in each position, you store a key (something unique) and a value (any value associated with the key)
    Mutable. Great for storing things and getting access to them later
'''
# key is name, value is age
dictionaryExample = {"Heidi" : 43, "Howard" : 15, "Helga" : 27}

print(dictionaryExample)
# get list of just the keys:
print("\nkeys:", dictionaryExample.keys())
# get list of just the values
print("\nvalues:", dictionaryExample.values())

# get a list with each key and value in a tuple:
print("\nkeys and values:", dictionaryExample.items())

# usually used when you know a key, but want the value:
print(dictionaryExample['Heidi'])


# More on the uses of dictionaries later.


# SETS (just be aware of it)
########################
'''
    use curly braces with no colons {}
    mutable
    you can think of this as a dictionary that only has keys, no values
    the point is to store only unique, non repeating data
'''

setExample1 = {"Heidi", "Howard", "Helga"}
setExample2 = {"Homer", "Heidi", "Happy"}

# useful for set logic/algebra (think venn diagrams)

#union (combine with no duplicates):
print("\nunion:", setExample1 | setExample2)

# intersection (common elements):
print("\nintersection:", setExample1 & setExample2)

# difference (elements in one set not in the second) 
print("\ndifference:", setExample1 - setExample2)

# symmetric difference (elements in one or the other but not both)
print("\nsymmetric:", setExample1 ^ setExample2)