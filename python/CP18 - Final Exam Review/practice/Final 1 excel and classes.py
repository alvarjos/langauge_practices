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


# practice question:

'''
import the "books_data.xlsx" file. Each row should become a "Book" object. Store each book object in a list.

In the Book class, instance variables should be book_title, book_author, and year_of_publication. 
Also include an instance varaible is_checked_out that defaults to a value of False. 

The book class should include a constructor

Create a method called "check_out".
    - normally, should change is_checked_out to True and print "You checked out book_title"
    - But, if the book is already checked out, then print "book_title already checked out, cannot check it out currently."

Create a method called "return_book"
    - It changes the is_checked_out variable to False and prints out "Thanks for returning book_title"
    - But, If is_checked_out is already False, print ("book_title is not checked out, cannot return")

Create a method called "display status"
    - it prints out the title, author, year of publication and "Checked out" or "Available"


Check out the 3rd, 6th, and 7th books in your list.
Try to check out the 3rd again.
Try and return the 4th
Return the 6th.
Run Display status on all the books.

'''

# import the excel file and make objects


#checking out the 3rd, 6th, and 7th books in the list

# try to check out the 3rd:


# try and return the 4th:


# try and return the 6th:


# run display status on all the books:

