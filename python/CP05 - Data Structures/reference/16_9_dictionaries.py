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
grade_dict = {"A": 4.0, "A-": 3.7, "B+": 3.4,"B": 3.0}

# Find the value for the key of "A".
# in dictionaries, you use [] like with lists, but instead of providing an index, you provide a key
gpa_value = grade_dict['A']  # Returns 4.0
print(gpa_value)


# Add an entry with B- as the key and 2.7 as the value
grade_dict['B-'] = 2.7
print(grade_dict)

# modify the entry for the key "A" to be 4.01
grade_dict['A'] = 4.01
print(grade_dict)

# delete items using del, or pop(key)
# try deleting B-
#del grade_dict['B-']
# or use pop:
removed_gpa = grade_dict.pop('B-')
print(removed_gpa)
# delete everything with .clear():
#grade_dict.clear()

#######
# .get()
# looks for the value of the key given.If it can't find it returns the value after the comma
# safer than just grade_dict["A"] because it handles the case of the key not existing:
value = grade_dict.get("A")
print(value)

# try getting the value for the key of "F". if it isn't found, return "Grade not found"
value = grade_dict.get('F', 'Grade Not Found')
print(value)

# setdefault(key, value)
# You can grab a value if it is there, or insert it if it isn't there:
# try adding F , 0.0 using setdefault. setdefault() returns the value of the key, or the new value set.
print(grade_dict)
value = grade_dict.setdefault('F', 0.0)
print("F isn't in there, so it will add F and a value:", value)
print(grade_dict)

# try adding A, 5.0 with setdefault
value2 = grade_dict.setdefault('C', 0.0)
print(value2)


#sometimes, you only want the keys, values, or both in a list-type format:

# use .keys() to print only the keys
grades = grade_dict.keys()
print(grades)
# use .values() to print only the values
gpas = grade_dict.values()
print(gpas)

# use .items() to return keys and values in a tuple pair.
grade_gpa_pairs = grade_dict.items()
print(grade_gpa_pairs)



# also useful with if statements. It will check the key by default.
# check if B+ is a key in the grade dictionary:
if "B+" in grade_dict:
    print("that is a valid grade")



