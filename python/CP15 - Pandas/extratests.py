import numpy as np
import pandas as pd

#list of data
lstNames = { "Type" : [ np.nan, "Jazz", "Modern", "Tap", "Tango", "Square", "Hip-Hop"],
                "Dancer" : ["Jane", np.nan, "Lyla", "London", "Zoey", "Millie", "Beck"],
                "Age" : [18, 23, 19, 20, 21, 22, 21]
            }

#Calling DataFrame constructor on list
dfDance = pd.DataFrame(lstNames)

ex1 = dfDance.loc[(dfDance["Age"] > 20) & (dfDance["Dancer"] == "Millie"), "Age"]

print(ex1)

ex2 = dfDance.loc[5,2]

print(ex2)