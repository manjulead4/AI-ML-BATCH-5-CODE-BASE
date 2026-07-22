import pandas as pd 
# dict
data = {
    "Name" : ["Ajay","Babu","charan"],
    "Age" : [25,30,35],
    "city":["Banglore","Hyderabad","Chennai"]
}
df = pd.DataFrame(data)
print(df)

