# Name: Jacob Steffen
# Decription: Imports book and patron data of a library and creates classes from them. Checks out books for each patron and then displays the books they checked out.

# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

import random # used to randomly generate numbers and randomly select things in lists

# You only need either pandas or openpyxl to import excel files. I used both just for demonstration purposes.
import pandas as pd
import openpyxl 


class Book:
    def __init__(self, title, author, genre, is_checked_out = False):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = is_checked_out # this isn't included in the excel file. By default a book should not be checked out.

    def display_info(self): # just a way to show all the relevant information about the book.
        print(f"{self.title} by {self.author} (Genre: {self.genre})")

class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.checked_out_books = [] # not included in the excel file. You can set it here, or in the parameters section, either works.

    def check_out_book(self, book):
        if len(self.checked_out_books) < 3 and not book.is_checked_out: # checks if the length of the list is less than 3 AND that the book isn't checked out
            self.checked_out_books.append(book) # adds book to their list
            book.is_checked_out = True # updates the value of the book to show it is now checked out
            print(f"{book.title} has been checked out by {self.name}.")
        else: # this will occur if either of the 2 conditions in the if statement is false. Thats because I used "and" instead of "or"
            print(f"Cannot check out {book.title}. Limit reached or book already checked out.")

    def display_checked_out_books(self):
        if self.checked_out_books: # this is shorthand for checking if there is something in the list. The same as len(self.checked_out_books) > 0
            print(f"\n{self.name} has checked out the following books:")
            for book in self.checked_out_books:
                book.display_info() # run the display_info on every book in the patron's checked out books list
        else:
            print(f"\n{self.name} has no books checked out.")

# Importing the book data
df_books = pd.read_excel(r"solution_final_practice_1_books\books_data.xlsx") # put excel data in a pandas dataframe
list_of_books = [] # will store objects in later

# iterrows() returns two variables each iteration. I don't use the index, but I need to list it to get at the row
# the other variable is a single row of the dataframe as a list/tuple.
for index, row in df_books.iterrows(): 
    title, author, genre = row # row is a list of of the column values. You can unpack a column into mulutiple variables like this.

    # the other way of doing it is like this:
    # title = row[0]
    # author = row[1]
    # genre = row[2]

    book = Book(title, author, genre) # creating a new Book, storing it in variable called book.
    list_of_books.append(book) # storing that book object in a list.


# Here I'll show doing it with openpyxl for the patrons. I'd recommend just choosing pandas or openpyxl and sticking with it.
wb_patrons = pd.read_excel(r"solution_final_practice_1_books\patrons_data.xlsx")
list_of_patrons = []

for row in wb_patrons.iterrows(): # note that with openpyxl you use iter_rows() with an underscore. With pandas you use iterrows() with no underscore.
    patron_id, name = row[1]
    patron = Patron(patron_id, name)
    list_of_patrons.append(patron)

# For each patron, choosing a number between 1 and 4 and trying to check out those books:

for patron in list_of_patrons:
    num_books_to_check_out = random.randint(1,4) # random number between 1&4
    print(f"{patron.name} will try and check out {num_books_to_check_out} book(s):")
    for _ in range(num_books_to_check_out): # I just need to do something between 1-4 times, but I don't need the index. So I just called the loop variable _. That is convention when you don't use the looping variable.
        random_book = random.choice(list_of_books) # choose a random book
        patron.check_out_book(random_book) # try to check out that book.
    print() # this just prints out a line return for some extra space

# display the checked out books for all patrons
for patron in list_of_patrons:
    patron.display_checked_out_books()
    

