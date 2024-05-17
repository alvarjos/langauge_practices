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

# Break and continue
'''
Break and continue are two control statements. They apply to while and for loops the same.
They will almost always be used in conjunction with an if statement.

Two types:

    - break: instantly exit the loop

    - continue: stop the current iteration of the loop, but then continue on with the next iteration of the loop.

'''


# break
# this will make you exit the loop immediately, continue on with anything after the loop


# Practice:
# do the same thing from 7_2_1 (Ask if you want to enter a student name, etc.)
# but inside the while loop, if they enter "QUIT", immediately exit the loop

sAnswer = input("Do you want to enter a student name?").upper()

while (sAnswer == "Y") :
    sFullName = input("Enter the student name: ")
    if (sFullName.upper() == "QUIT") :
        # HERE IS THE BREAK
        break
        
    fGPA = float(input("Enter the " + sFullName + "'s GPA: "))
    
    print(sFullName, "has a GPA of", fGPA)
    
    sAnswer = input("Do you want to enter a student name?").upper()

print("Thank you")


# continue
# Do the same as the above, but if the user enters 0 for the GPA, 
# then use a continue statement to start the iteration of the loop over.

sAnswer = input("Do you want to enter a student name?").upper()
while (sAnswer == "Y") :
    sFullName = input("Enter the student name: ")
    fGPA = float(input("Enter the " + sFullName + "'s GPA: "))
    
    if (fGPA == 0) :
        # HERE IS THE CONTINUE
        continue
        
    print(sFullName, "has a GPA of", fGPA)
    sAnswer = input("Do you want to enter a student name?").upper()
    
print("Thank you")





