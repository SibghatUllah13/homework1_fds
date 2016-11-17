# Importing all the Important Packages that we might need 
import os
import csv
import numpy as np
import pandas as pd


# Here the Code Starts

# Getting the Current Working Directory and adding the Name of the File 
cwd=os.getcwd()
file=cwd+"\\Nile.csv"

#### At this Moment, the Name of the File should be ready. The underlying assumption here, is that you
# already have the Nile.csv in your working directory. Please note that the "/" or "\" in Paths could be different, Since in Windows the Path is
# Like This, "C:\\Users\\conne" So thats why two backslashs "\\" are added before adding the File Name...However, if you are testing it on MAc or Linux,
# the Path might involve one backslash or forward slash..So while it is tested on Windows and double checked...Please beware that it could differ on other Platforms.


# Start is the variable that stores the Starting Year 
start = input("Give me the starting year: ")
# End is the variable that stores the Ending Year 
end = input("Give me the ending year: ")
# Read the CSV File , using two columns..which contain year and water flow 
nile=pd.read_csv(file,usecols=[1,2],index_col=0)
# Save the Values of the Nile data frame which only have our specific interval, for example 1880-1900 etc...
vector=nile.loc[start:end]
# Now only get the Column Nile out of this New Data Frame called Vector
n=vector['Nile']
# Print the Mean calculated using Numpy
print (np.mean(n))
# End 
