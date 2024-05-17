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
    Lists just store other data types inside them
'''

# Make a list of strings
# Store "Harry", "Hermione", "Ronald", "Luna" in the list:

example_list = ["Harry", "Hermione", "Ronald", "Luna"]

# you can print the whole list, but its a little ugly.
# Note: we'll learn how to print a whole list prettier when we get to loops in the next section.
print(example_list)


# You can access specific points of the list using brackets [index]:
# note that index starts at 0. So 1st item = 0, 5th item = 4, etc.
# think of it like when you are born, you are 0 until you have moved 1 year through life.

print(example_list[0])
print(example_list[1])

# You'll get an error if you try to access a point in the list that doesnt exist:
#print(example_list[4])

# len gives you the length of the list
lengthExample = len(example_list)

print(lengthExample)

# you can add things to the end of the list with append.
example_list.append("Dumbledore")

print(example_list)


# you can add things anywere else with insert(where to add it, what to add):

example_list.insert(0, "Fred")
print(example_list)
example_list.insert(2, "George")
print(example_list)

# you can delete something from the list using .pop()
# by default it gets rid of the last thing on the list.
# BUT it also returns it if you want to use it.

poppedVariable = example_list.pop() # gets rid of the last thing from the list
print(example_list)

print(f"But when you pop something, it returns what you popped off, so you can store it somewhere else if you want: {poppedVariable}")

# you can also specify a specific thing to pop, not just the last one:
# try popping the 4th thing in the list (remember 4 thing means index 3)
example_list.pop(3)
print(example_list)


# useful in if statements:

# check if "Harry" is in your list. Print something if so.
if "Harry" in example_list:
    print("wow Harry is in the list")

# if Voldemort is not in the list, print "Yay"
if "Voldemort" not in example_list:
    print("Yay!")

# getting a range of things: [starting index: end index]
# print out the 3rd to the 5th things in the list
print("range of things:", example_list[2:4])

# You can get the last thing in a list using -1
print("last list element:", example_list[-1])









'''
Lots of cool functions to use with lists. We covered some, see the textbook for more:

append()	Add an element at the end of the list.	lstNames.append("Salsa")
clear()	    Removes all the elements from the list so that the length is now 0.	lstNames.clear()
copy()	    Return a copy of the list so you can store it to a new variable. This creates a true copy so that the variables are NOT pointing to the same memory location. You can change one variable and it will not affect the other.	lstNew = lstNames.copy()
count()	    Returns the number of times a specific value is found in a list.	print( lstNames.count("Tap"))
extend()	Add one or more items from another list to the end of the current list.	lstNames.extend(lstOtherNames)
index()	    Returns the numerical position for the first item that has a specific value.	print(lstNames.index("Tap"))
insert()	Increase the size of the list and add a new item at a specific position. This example would increase the length of the list by 1 and then add the new item at the beginning of the list.	lstNames.insert(0, "Irish Folk")
pop()	    Remove an item from the list based upon the numerical position (0 based). You could use the negative indexing to remove the last item in the list (-1).	lstNames.pop(0) #removes first item
remove()	Removes the first item in the list that has the specified value. It also decreased the size of the list by 1. This only removes the first one found. If there were two items with the same value only the first would be removed. You would want to use a loop if you needed to remove more than one.	lstNames.remove("Tap")
reverse()	Reverses the order of the list so that the last becomes the first and the first becomes the last.	lstNames.reverse()
sort()	    Sorts the list in ascending order based upon alphabetical or numerical order. If you want a descending list, you can sort the list and then issue a reverse(). NOTE: If you want to sort the list in descending order you can use the reverse parameter lstNames.sort(reverse=True).	lstNames.sort()

'''










