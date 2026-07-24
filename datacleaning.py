import pandas as pd
import numpy as np 

# we will create an custo dataset 
data = {
    "name" : ["ajay","babu","charan","Siri",None],
    "age" : [25,np.nan,30,25,35],
    "marks"  : [85,80,np.nan,95,95],
    "City"   : ["banglore","chennai","hyderabad","mumbai","delhi"]
}

# to convert raw data into dataframe where we can use pandas operation

df = pd.DataFrame(data)
print(df)

# handiling the missing valves 

# check for missing valves 

print(df.isnull().sum())


# fill the specific row or column (age ) with mean or median uding probabilty 

age_filler = df["age"].fillna(df["age"].median())
print(age_filler)

marks_filler = df['marks'].fillna(df["marks"].mean())
print(marks_filler)


# fill random name in the name section 


name_filler = df["name"].fillna("sanjana")
print(name_filler)




# i nned to find the duplicate valves 


print(df.duplicated())


# need to go and specific column 

print(df["age"].duplicated())



# i nned to go and check for "marks"

print(df["marks"].duplicated())

# deletimg the duplicate valves 

print(df["age"].drop_duplicates())

# delete the duplicates from the marks 

print(df["marks"].drop_duplicates())



