# mention the __.dict__ of classes for printing out everything a class has


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
    Each element in a dictionary stores 2 things:
        a key (unique value, can't be repeated)
        a value (associated with the key. Can be repeated)

    So the first element is a key/value, the 2nd element is another key/value, etc.

'''

# create a dictionary using {:} that stores key/values for:
# "A": 4.0, "A-": 3.7, "B+": 3.4, "B": 3.0
example_dictionary = {"A": 4.0, "A-": 3.7, "B+":3.4, "B":3.0}
print(example_dictionary)

# Find the value for the key of "A".
# in dictionaries, you use [] like with lists, but instead of providing an index, you provide a key

value_of_A = example_dictionary["A"]
print(value_of_A)
print(example_dictionary["B"])

# Add an entry with B- as the key and 2.7 as the value

example_dictionary["B-"] = 2.7
print(example_dictionary)

# modify the entry for the key "A" to be 4.01

example_dictionary["A"] = 4.01
print(example_dictionary)

# delete items using del, or pop(key)
# try deleting B-
#
# or use pop:

example_dictionary.pop("B-")

# delete everything with .clear():
# example_dictionary.clear()

print(example_dictionary.get("A"))

#######
# .get()
# looks for the value of the key given.If it can't find it returns the value after the comma
# safer than just grade_dict["A"] because it handles the case of the key not existing:
print(example_dictionary.get("F", "Grade not found"))


# try getting the value for the key of "F". if it isn't found, return "Grade not found"


# setdefault(key, value)
# You can grab a value if it is there, or insert it if it isn't there:
# try adding F, 0.0 using setdefault. setdefault() returns the value of the key, or the new value set.

example_dictionary.setdefault("F", 0.0) # F isn't there
example_dictionary.setdefault("A", 0.0) # A is there
print(example_dictionary)

# try adding A, 5.0 with setdefault



#sometimes, you only want the keys, values, or both in a list-type format:

# use .keys() to print only the keys
print(example_dictionary.keys())
# use .values() to print only the values
print(example_dictionary.values())
# use .items() to return keys and values in a tuple pair.
print(example_dictionary.items())

# also useful with if statements. It will check the key by default.
# check if B+ is a key in the grade dictionary:

if "B+" in example_dictionary:
    print("It is there!")


