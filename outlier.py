import pandas as pd 
import numpy as np 

data = {
    "name" : ["ajay","babu","charan","Siri","deeksitha"],
    "age" : [25,40,30,25,35],
    "marks"  : [85,80,90,95,300],
    "City"   : ["banglore","chennai","hyderabad","mumbai","delhi"]
}

df = pd.DataFrame(data)
print(df)


# using IQR (INTERQUARTILE Range ) method to indemntify the outlier 


Q1 = df["marks"].quantile(0.25) # thhis is my lower range 

Q3 = df["marks"].quantile(0.75) # this is my upper range 


IQR = Q3-Q1

outilers = df[(df["marks"]< Q1 - 1.5*IQR)| (df["marks"] > Q3 +1.5*IQR)]

print("outliers are : \n ",outilers)


# treating the outlears 

# using cap method we are solving 

df["marks"] = np.where(df["marks"] > Q3 + 1.5*IQR, Q3+1.5 * IQR,df["marks"])
print("after treatment:\n ",df)


