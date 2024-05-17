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
Note: I'm not going to go over this in class.

This is closer to what the textbook teaches, but I'm going to use the 
SQLAlchemy method, because it aligns better with Pandas and using SQLAlchemy
lets you use the same syntax for creating connections no matter which DBMS you use.


before running this code you should:

    1. Have postrgreSQL installed (which should come with PGAdmin4)
    2. install psycopg2
        one of these should work:
            pip install psycopg2
            pip3 install psycopg2

        if pip/pip3 install looks like it almost worked, but says it couldn't finish compiling, try this instead:
            pip install psycopg2-binary
            pip3 install psycopg2-binary
    3. created a database in pgAdmin4. Call the database is303 (no capitals)
    3. created a user in pgAdmin4.
        call your user is303user (no capitals)
        on the "Definition" tab, give a password of 12345classpassword (again no capitals)
        on the "Privileges" tab, select "can login" and "superuser"
    4. Copied the "students table creation script" into pgAdmin4, ran it, and created the students table in pgAdmin4

'''
import psycopg2

# define the connection parameters:
database_name = "is303"
db_user = "is303user"
db_password = "12345classpassword"
db_host = "localhost" #this just means the database is stored on your own computer
db_port = "5432" # default setting

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname = database_name, user = db_user, password = db_password, host = db_host, port = db_port)

# Create a cursor object with conn.cursor(). Can call it anything, but typically people call it cur.
cur = conn.cursor()

# use cur.execute("put your query here") to run a query.
# try getting everything from the students table
cur.execute("select * from students;")

'''
to access the query you ran, you can use
cur.fetchone() to get a single row
cur.fetchmany(amount to get) to get a specific number of rows
cur.fetchall() to get everything
'''

# use .fetchone and print it out
print(cur.fetchone())

# do it a couple more times
print(cur.fetchone())
print(cur.fetchone())

# put the result of fetcheone() in a variable, and loop through each column and display the data:
single_row_result = cur.fetchone()

for column in single_row_result:
    print(column)


# now use fetchmany to get 5 rows, print it out
print(cur.fetchmany(5))

# now use fetchall, print it out
print(cur.fetchall())

# if you want to get everything from start again, just re-execute the query
# do select * from students again
cur.execute("select * from students;")

# store the result of fetch all in a variable, then loop throught the rows, then loop through the columns. print out the row, then print out the column
fetch_all_result = cur.fetchall()

for row in fetch_all_result:
    print(row)
    for column in row:
        print(column)

# insert statement: INSERT INTO students (first_name, last_name, age, email) VALUES ('New', 'Student', 99, 'fake_email@fake.com')
# execute the insert statement
cur.execute("INSERT INTO students (first_name, last_name, age, email) VALUES ('New', 'Student', 99, 'fake_email@fake.com')")

# find that student you just inserted (remember WHERE from class)
cur.execute("SELECT * FROM students WHERE first_name = 'New' AND last_name = 'Student'")
print(cur.fetchall())

'''
now look for that student in pgAdmin4.
You can't see them, right?

for things to show up in the actual database, they need to be committed
'''
# for commit, note I use conn, not cur
conn.commit()

# Close the cursor and connection to so the computer can allocate
# bandwidth to other requests
cur.close()
conn.close()




