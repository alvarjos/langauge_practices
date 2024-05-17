# if we have time, attempt this. We probably won't have for everyone to have a full go at it, but at least you can start thinking through it.

'''
Write a python program for a prize slot machine. 

Ask the user if they want to play, and if they say yes,
generate a random number between 0 and 100.
if the number is above 70 then display (you won!)
otherwise display "better luck next time".

But, on Fridays and Saturdays players have a better
chance of winning, since the random integer should be
between 50 and 100 instead of 0 and 100.

Remember to import the correct modules
'''

import random
from datetime import datetime

# get the player's decision:
sPlayDecision = input("would you like to try and win a prize? enter yes or no: ".lower())

# only run the program if they say yes
if sPlayDecision == 'yes':
    
    # get today's date and convert it to a text date, like "Monday", or "Saturday"
    sToday = datetime.now().strftime("%A")

    print(sToday) # unnecessary, but shows what the previous line of code is doing.

    # if it is friday or saturday, make the odds better.
    if sToday == "Friday" or sToday == "Saturday":
        iRandomNum = random.randint(50,100) # grab a number between 50 and 100
    else:
        iRandomNum = random.randint(0,100) # grab a number between 0 and 100

    print("this is the random number. This is just for testing: ")
    print(iRandomNum)
    
    if iRandomNum > 70:
        print("you won!")
    else:
        print("better luck next time")
else:
    print("You will not play the game :(")

