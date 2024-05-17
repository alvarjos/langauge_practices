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
before running this code you should:

    1. Have postgreSQL installed (which should come with PGAdmin4)
    2. install psycopg2 and sqlalchemy
    3. created a database in pgAdmin4. Call the database is303 (no capitals)
    3. created a user in pgAdmin4.
        call your user is303user (no capitals)
        on the "Definition" tab, give a password of 12345classpassword (again no capitals)
        on the "Privileges" tab, select "can login" and "superuser"
    4. Copied the "students table creation script" into pgAdmin4, ran it, and created the students table in pgAdmin4
'''

import sqlalchemy
from sqlalchemy.sql import text

# define the connection parameters:
database_name = "is303"
db_user = "is303user"
db_password = "12345classpassword"
db_host = "localhost" #this just means the database is stored on your own computer
db_port = "5432" # default setting

# Connect to the PostgreSQL database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')

# Create a connection object with engine.connect()


# use the text function to make your query work with sqlalchemy
# try getting everything from the students table


# use conn.execute("put your query here") to run a query.
# store the result in a variable


'''
to access the query you ran, you can use
    fetchone() to get a single row
    fetchmany(amount to get) to get a specific number of rows
    fetchall() to get everything
'''

# use .fetchone and print it out


# do it a couple more times


# put the result of fetcheone() in a variable, and loop through each column and display the data:


# now use fetchmany to get 5 rows, print it out

# now use fetchall, print it out


# if you want to get everything from start again, just re-execute the query
# do select * from students again


# store the result of fetch all in a variable, then loop throught the rows, then loop through the columns. print out the row, then print out the column


# insert statement: INSERT INTO students (first_name, last_name, age, email) VALUES ('New', 'Student', 99, 'fake_email@fake.com')
# remember to use the text function first
# execute the insert statement


# find that student you just inserted (you can use WHERE id = 21)


'''
now look for that student in pgAdmin4.
You can't see them, right?

for things to show up in the actual database, they need to be committed
'''

# use .commit with the connection object you made at the beginning.


# Close the cursor and connection to so the computer can allocate
# bandwidth to other requests
# .close()





