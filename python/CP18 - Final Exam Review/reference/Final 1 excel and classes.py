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
import pandas as pd
import openpyxl

class Book:

    def __init__(self, book_title, book_author, year_of_publication, is_checked_out = False):
        self.book_title = book_title
        self.book_author = book_author
        self.year_of_publication = year_of_publication
        self.is_checked_out = is_checked_out

    def check_out(self):
        if self.is_checked_out == True:
            print(f"{self.book_title} already checked out, cannot check it out currently.")
        else:
            self.is_checked_out = True
            print(f"You checked out {self.book_title}")

    def return_book(self):
        if self.is_checked_out == False:
            print(f"{self.book_title} is not checked out, cannot return")
        else:
            self.is_checked_out = False
            print(f"Thanks for returning {self.book_title}")

    def display_status(self):
        if self.is_checked_out == True:
            extra_message = "Checked out"
        else:
            extra_message = "Available"
        print(f"{self.book_title}, {self.book_author}, {self.year_of_publication}, {extra_message}")

# # using pandas
# dfBooks = pd.read_excel("reference/books_data.xlsx")
# list_of_books = []
# for index, row in dfBooks.iterrows():
#     book_title, book_author, year_of_publication = row
#     book = Book(book_title, book_author, year_of_publication)
#     list_of_books.append(book)

# using openpyxl:
wbBooks = openpyxl.open("reference/books_data.xlsx")
list_of_books = []
for row in wbBooks.active.iter_rows(min_row = 2, values_only=True):
    book_title, book_author, year_of_publication = row
    book = Book(book_title, book_author, year_of_publication)
    list_of_books.append(book)


#checking out the 3rd, 6th, and 7th books in the list
list_of_books[2].check_out()
list_of_books[5].check_out()
list_of_books[6].check_out()

# try to check out the 3rd:
list_of_books[2].check_out()

# try and return the 4th:
list_of_books[3].return_book()

# try and return the 6th:
list_of_books[5].return_book()

# run display status on all the books:
for book in list_of_books:
    book.display_status()
