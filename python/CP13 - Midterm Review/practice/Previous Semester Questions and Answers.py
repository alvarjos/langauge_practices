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

# these are just questions and answers that some people had from previous semesters.
# you might find some of it useful.


############
# modulus
############
'''
Think of modulus as doing division, and then giving you what is left over.

For example lets think of 5 divided by 2.  2 goes into 5 twice (getting to 4) with 1 left over.

So if we do 5 % 2, the result would be 1
'''
result = 5 % 2
print("modulus:", result)

'''
if divides evenly, that means there are no remainders, so the modulus will be zero.

For example 9 can be divided by 3 with no remainders, so the modulus here is zero.

'''
result = 9 % 3
print("modulus:", result)

'''
one more example: 17 / 5.  The closest 5 gets to going into 17 is 15. Then there are 2 left over to get to 17, 
so the remainder is 2
'''
result = 17 % 5
print("modulus:", result)

#################
# shortcuts += -=
##################

'''
There are shortcuts for adding or subtracting (also multiplying, dividing, etc.) anything to an existing  variable

Let's say you have a variable holding the value 15. You want to add 3 to it, so that the variable is now holding 15
You could do this:
'''
exampleVariable = 15

exampleVariable = exampleVariable + 3

print("no shortcut:", exampleVariable)
'''
The shortcut is just a way  to do this without retyping exampleVariable
'''

exampleVariable = 15

exampleVariable += 3

print("with shortcut (its the exact same:", exampleVariable)


#####################
# when to use while, for, or if
######################

'''
if is NOT a loop. Only use it if you want to check a condition once.

Wording for using an if would be like "only print out "you did it!" if the numbers add to 10.
'''
num1 = 6
num2 = 4

if num1 + num2 == 10:
    print("you did it!")

'''
a while loop is something you'd do if you want something to occur over and over again until the condition
is no longer true.

For example, keep adding 1 to num 1 until it equals 10:
'''
num1 = 6

while num1 < 10:
    num1 = num1 + 1
    print("this is the value of num1:", num1)


''' 
a for loop will run for as many times as you tell it to with range() or if you give it a list of things
it will step 1 by 1 through the list (or if not a list, any other kind of data type it can iterate through, like a dictionary or string)
'''

# range
for callThisWhateverYouWant in range(5):
    print("this is the current value of the step in range(5): ", callThisWhateverYouWant)

# this is just a list of random things
forLoopListExample = [20, 34, 56, "another thing", "hello", 6]

for thing in forLoopListExample:
    print("this is the current thing in the list:", thing)

'''
often, you can have a for loop or while loop and have it work the same. Generally, I'd say use a for loop if you have a 
list you need to go through or you ask the user for a specific number of times to do something. Otherwise, just use a while.
'''

###################
# len()
###################
'''
len() just tells you how long things are, like strings, dictionaries and lists
'''
exampleString = "example"
exampleList = [1, 2, 3, 4 ,5 ,6]
exampleDictionary = {"first" : 1, "second" : 2, "third" : 3, "fourth" : 4}

print("length of string:", len(exampleString))
print("length of a list:", len(exampleList))
print("length of a dictionary:", len(exampleDictionary))

###################
# randint(1,3) # can give 1, 2, or 3 
# randrange(1,3) can give 1, or 2
###################


'''
when you use randint it is inclusive on both sides

so randint(1,3) can give you 1, 2, or 3 randomly

when you use randrange it in inclusive on the bottom range, but exclusive on the top range

so randrange(1,2) can give you 1 or 2 randomly.

Use either one, it doesn't matter, just know how the function behaves so you use it correctly

'''
#############
# try and except, difference between
###############

'''
If you have a try, you must have an except.

try is just a place to put code. The code runs like normal, except if it runs into an error.

If code in a try hits an error, it stops IMMEDIATELY and goes to the except, and then the code in except runs
'''

try:
    print("this code will work")
    #this line won't run because I haven't made the variable z yet, but I'm trying to print it:
    print(z)
    print(" this is another line of code")
    #this line won't be run because when the line above is found to have an error, it will skip to the except
except:
    print("this will print if there is an error")