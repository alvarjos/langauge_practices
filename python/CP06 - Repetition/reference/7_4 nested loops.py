# Just like with nested ifs, you can also do nested loops:

# this is asking how many students there are, and looping throug them,
# then asks how many tests each student has taken

# iStudentCount = int( input( "How many students? "))

# # outer loop: looping through number of students
# for iCount in range(0, iStudentCount) :
#     # remember that \t adds a tab. I just added it to physically show where we are in the loop.
#     print("\tthis is the outer loop : ", iCount +1)
#     # remember \n adds a line break
#     sFullName = input("\n\tEnter the student " + str( iCount + 1) + "'s full name: ")
    
#     iNumTests = int( input("\n\tHow many tests for " + sFullName + "? "))
#     # this resets the value of iSumTest
#     iSumTest = 0
#     #this adds an extra line break (paragraph break)
#     print("\n")
#     for iTestCount in range(0, iNumTests) :
#         print("]\t\tthis is the inner loop # ", iTestCount + 1)
#         iSumTest = iSumTest + float( input("\t\tEnter test score for test " + str( iTestCount + 1) + ": "))
        
#     fTestAve = iSumTest / iNumTests
    
#     print("\n\t", sFullName, "has a test average of", fTestAve, "\n")


# Practice:
'''
Write a program to print a right-angled triangle using asterisks (*).
The user should input the height of the triangle,
and your program should print rows of * where the number of * in each row equals the row number.

Example:
If the user inputs 4, the output should be:

*
**
***
****

So there are 4 rows, the first row has 1 *, the 2nd row has 2 *s, 3rd row has 3 *s, etc.
Hint: to get python to print something without adding a line break, add end="" to print, like this: print('*', end="")
'''

# iHeight = int(input("enter how many rows high you want the triangle to be: "))

# for row in range(1, iHeight +1):
#     sAsterisksToPrint = ''
#     for column in range(0, row):
#         sAsterisksToPrint = sAsterisksToPrint + "*"
    
#     print(sAsterisksToPrint)
    
'''
num_students = int(input("How many students do you want to enter?"))

for current_student_num in range(1, num_students + 1):
    print(f"Enter information for student {current_student_num}")
    name = input("Enter a name: ")
    num_test = int(input(f"How many tests to enter for {name}: "))

    for current_test_num in range(1, num_test + 1 ):
        test_score = input(f"Enter in test score #{current_test_num}: ")
        print(f"Student {name} scored {test_score} on Test {current_test_num}")
'''

# How to make a schedule
#How to make a tab in a string
print("\t")


schedule = {
    "Monday": ["Science", "Math"],
    "Tuesday": ["English", "History", "Art"],
    "Wednesday": ["Science", "Math"],
    "Thursday": ["English", "History", "Art"],
    "Friday": ["PE", "Science", "Math"]
}
for key_day, value_list_of_subject in schedule.items():
    print(key_day)
    for subject in value_list_of_subject:
        print(f"\t{subject}")
    "\n"