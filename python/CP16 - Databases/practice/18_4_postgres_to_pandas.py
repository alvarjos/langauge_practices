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

import pandas as pd
import sqlalchemy

# define the connection parameters:
database_name = "is303"
db_user = "is303user"
db_password = "12345classpassword"
db_host = "localhost" #this just means the database is stored on your own computer
db_port = "5432" # default setting

# because we eventually want to write back to the postgres database, we are connecting using sqlalchemy
# Connect to the PostgreSQL database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')
# query to eventually run:
query = "select * from students;"

# use pandas' read_sql_query() function. give it the query you want to send,
# and the engine object that has your connection
# to the postgres database. It will return a dataframe.


# now you could do anything you want with a pandas dataframe
# e.g. print out the first_name column:


# if you want to sanitize any inputs, just add a params = (variable,)
# and make the query have %s for every variable substitution you want to perform.
# to the read_sql_query
# pd.read_sql_query(query, engine, params = (variable, ))

