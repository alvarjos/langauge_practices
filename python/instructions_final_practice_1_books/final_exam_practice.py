# Angel Alvarado

# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# import pandas as pd

# class Book:
#     def __init__(self, book_title, book_author, book_genre, is_checked_out = False):
#         self.book_title = book_title
#         self.book_author = book_author
#         self.book_genre = book_genre
#         self.is_checked_out = is_checked_out

#     def check_out(self): 
#         if self.is_checked_out is True:
#             print(f"{self.book_title} is already checked out") 
#         else:
#             self.is_checked_out = True
#             print(f"You have checked out {self.book_title}")

#     def return_book(self):
#         if self.is_checked_out is True:
#             print(f"Thanks for returning {self.book_title}")
#             self.is_checked_out = False
#         else:
#             print(f"{book_title} is not checked out, cannot return")
    
#     def display_status(self):
#         if self.is_checked_out is True:
#             print(f"{self.book_title}, {self.book_author}, {self.book_genre}: Checked out")    
#         else:
#             print(f"{self.book_title}, {self.book_author}, {self.book_genre}: Available")


# df_books = pd.read_excel(r"instructions_final_practice_1_books\books_data.xlsx")
# print(df_books)


# book_list = []
# for index, row in df_books.iterrows():
#     # print(row.iloc[0]) # same thing as the line below
#     book_title = row["title"]
#     book_author = row["author"]
#     book_genre = row["genre"]

#     book = Book(book_title, book_author, book_genre)
#     book_list.append(book)

# print(book_list)
# for index, row in df_books.iterrows():
#     book_title, book_author, book_genre = row
#     book = Book(book_title, book_author, book_genre)
#     book_list.append(book)

# book_list[2].check_out()
# book_list[5].check_out()
# book_list[6].check_out()
# book_list[2].check_out()
# book_list[3].return_book()
# book_list[6].return_book()



import random
import pandas as pd
import openpyxl


class Book():
    def __init__(self, title, author, genre, is_checked_out = False):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_checked_out = is_checked_out

    def display_info(self):
        print(f"{self.title} by {self.author} (Genre: {self.genre})")

class Patron():
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):
        if len(self.checked_out_books) < 3 and not book.is_checked_out: # checks if the length of the list is less than 3 AND that the book isn't checked out
            self.checked_out_books.append(book) # adds book to their list
            book.is_checked_out = True # updates the value of the book to show it is now checked out
            print(f"{book.title} has been checked out by {self.name}.")
        else: # this will occur if either of the 2 conditions in the if statement is false. Thats because I used "and" instead of "or"
            print(f"Cannot check out {book.title}. Limit reached or book already checked out.")      

    def display_checked_out_books(self):
        if self.checked_out_books:
            print(f"\n{self.name} has checked out the following books:")
            for book in self.checked_out_books:
                book.display_info() # run the display_info on every book in the patron's checked out books list
        else:
            print(f"\n{self.name} has no books checked out.")

df_books = pd.read_excel(r"instructions_final_practice_1_books\books_data.xlsx")
list_of_books = []   

for index, row in df_books.iterrows():
    title, author, genre = row

    book = Book(title, author, genre)
    list_of_books.append(book)


wb_patrons = pd.read_excel(r"instructions_final_practice_1_books\patrons_data.xlsx")
list_of_patrons = []
    
for row in wb_patrons.iterrows():
    patron_id, name = row[1]
    patron = Patron(patron_id, name)
    list_of_patrons.append(patron)

for patron in list_of_patrons:
    num_books_to_check_out = random.randint(1,4)
    print(f"{patron.name} will try and check out {num_books_to_check_out} book(s):")
    for _ in range(num_books_to_check_out):
        random_book = random.choice(list_of_books)
        patron.check_out_book(random_book)
        
    print()

for patron in list_of_patrons:
    patron.display_checked_out_books()