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
conn = engine.connect()

# use the text function to make your query work with sqlalchemy
# try getting everything from the students table
sql_query = text("select * from students;")

# use conn.execute("put your query here") to run a query.
result = conn.execute(sql_query)

'''
to access the query you ran, you can use
    cur.fetchone() to get a single row
    cur.fetchmany(amount to get) to get a specific number of rows
    ur.fetchall() to get everything
'''

# use .fetchone and print it out
print(result.fetchone())

# do it a couple more times
print(result.fetchone())
print(result.fetchone())

# put the result of fetcheone() in a variable, and loop through each column and display the data:
single_row_result = result.fetchone()

input("This is a breakpoint, press enter")

for column in single_row_result:
    print(column)


# now use fetchmany to get 5 rows, print it out
print(result.fetchmany(5))

# now use fetchall, print it out
print(result.fetchall())

# if you want to get everything from start again, just re-execute the query
# do select * from students again
result = conn.execute(sql_query)

# store the result of fetch all in a variable, then loop throught the rows, then loop through the columns. print out the row, then print out the column
fetch_all_result = result.fetchall()

for row in fetch_all_result:
    print(row)
    for column in row:
        print(column)

# insert statement: INSERT INTO students (first_name, last_name, age, email) VALUES (21, 'New', 'Student', 99, 'fake_email@fake.com')
# remember to use the text function first
# execute the insert statement

input("This is a breakpoint, press enter")

sql_query = text("INSERT INTO students (id, first_name, last_name, age, email) VALUES (21, 'New', 'Student', 99, 'fake_email@fake.com')")

conn.execute(sql_query)

# find that student you just inserted (remember WHERE from class)

sql_query = text("SELECT * FROM students WHERE first_name = 'New' AND last_name = 'Student'")
result = conn.execute(sql_query)

print(result.fetchall())

'''
now look for that student in pgAdmin4.
You can't see them, right?

for things to show up in the actual database, they need to be committed
'''

# for commit, note I use conn, not cur
conn.commit()

# Close the cursor and connection to so the computer can allocate
# bandwidth to other requests
conn.close()




