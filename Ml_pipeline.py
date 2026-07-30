import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler


# create an custom data using dict

data = {
    "name" : ["ajay","babu","charan","Siri",None],
    "age" : [25,np.nan,30,25,35],
    "marks"  : [85,80,np.nan,95,95],
    "City"   : ["banglore","chennai","hyderabad","mumbai","delhi"]
}

# convert this into daat frames 

df = pd.DataFrame(data)
print(df)

# check for missing valves 

print(df.isnull().sum)

# using the specific column like age with men aor median operations 


age_filling =df["age"].fillna(df["age"].mean)
print("\n",age_filling)


marks_filler =df["marks"].fillna(df["marks"].median)
print(marks_filler)



# find the dupicate valves 

print(df.duplicated())

# i nned to find the dupicate valves 

print(df["age"].duplicated())


# remove duplicate valves 

print(df["age"].drop_duplicates())


print(df["marks"].drop_duplicates())
