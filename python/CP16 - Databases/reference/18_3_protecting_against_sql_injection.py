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
What I'll briefly show you crosses into more of a data security topic,
which we don't cover much in this class at all.

BUT, it isn't too complicated and should always be considered when building apps, 
so I think a brief demonstration is warranted.

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



'''
Let's say you wanted a write a program that lets you insert in a new student
and it asks the user for a name
for simplicity's sake we will just enter the last name.
'''
user_input_last_name = input("Please enter in the last name of the student to enroll in the school: ")

sql_query = text(f"INSERT INTO students (last_name) VALUES ('{user_input_last_name}')")

conn.execute(sql_query)
conn.commit()
conn.close()

'''
The above code works, and seems innocuous.
But there are people who for malicious reasons or just for fun
will try and see if they can break your system.

Rerun this python file, and when it asks for the letter of the last name, copy this code in:

MALICIOUS USER'); DROP TABLE students; --

'''

####
# Sanitizing / Parameterizing your SQL inputs!
####

'''
To fix your SQL insert statement, you need to add parameters
that are checked before you run the query

instead of the f-string word it like:
    :parameter_name
        get rid of any quotes

    and when you call .execute() add an argument with a dictionary
    that has the parameter name as the key, and the variable as the value.
    conn.execute(sql_query, {"last_name" : user_input_last_name})
'''

# Connect to the PostgreSQL database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')

# Create a connection object with engine.connect()
conn = engine.connect()

user_input_last_name = input("Please enter in the last name of the student to enroll in the school: ")

sql_query = text(f"INSERT INTO students (last_name) VALUES (:last_name)")

conn.execute(sql_query, parameters={"last_name" : user_input_last_name})
conn.commit()
conn.close()

