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

import pandas as pd # pandas gets you dataframes

# read the excel file into a pandas dataframe with pd.read_excel
dfImportedFile = pd.read_excel(r'dummy_data.xlsx')
print(dfImportedFile)
########
# inserting columns
########

# use .insert on a dataframe to add a column
# .insert(index, "name of column", data)
# for the data, you can either supply a single variable to apply to all rows,
# a list with the exact number of elements as there are rows
# or just provide another column from an existing dataframe.

# try inserting a new column called  "test_column" with "test" as the value for each row
dfImportedFile.insert(0, "test_column", "x")
print()
print(dfImportedFile)

# now make a column called "half_age", at position 2 that is the original age column divided by 2
# put it right after the original age column

dfImportedFile.insert(5, "half_age", dfImportedFile["age"] / 2)
print(dfImportedFile)


#######
# deleting columns / rows
#######

# delete the original age column using del. del is standard python to delete anything
# try deleting the "age" column
del dfImportedFile["age"]

# you can also use the .drop method to delete columns or rows.
# axis = 1 means columns, axis = 0 means rows (the default).
# you can add inplace = True

dfImportedFile.drop("test_column", axis=1, inplace = True)
print(dfImportedFile)


# provide a list of indices for it to drop specific rows
# try to drop the 1st and 4th rows.
dfImportedFile.drop(index = [1,4], inplace = True)








