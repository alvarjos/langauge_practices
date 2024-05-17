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


dict_dancers =  {   "Type" : ["Ballet", "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
                "Dancer" : ["Jane", "Hadley", "Lyla", "London", "Zoey", "Millie", "Beck"],
                "Age" : [18, 23, 19, 20, 21, 22, 21]
            }

# create a dataframe from the dancers dictionary

# exporting a dataframe to a database is relatively simple
# just use .to_sql('table_name', engine, if_exists='replace', index= False) 

# try changing the if_exists parameter to have the argument of 'append'.
# check pgadmin4 to see what happened:



# Practice:
# Make a dicitonary, dict_dancers_2, and create 2 new dancers. Make that
# dictionary into a dataframe, and then append that to the dancers table in your
# postgres database

