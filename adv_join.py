
# merging to datsets using the join method in pandas 

import pandas as pd 

df1 = {
        "ID":[1,2,3],
        "Name":["suresh","Sai","charan"],
        "Age":[25, 30 ,35]
         }

df2 = {
        "ID":[1,2,4],
        "Marks":[85,90,95]
        }
# to convert raw data into dataframe so we can perform using pandas 
df1 = pd.DataFrame(df1)
df2 = pd.DataFrame(df2)


# merged based on ids 
merged = pd.merge(df1,df2,on="ID",how = "inner")
print(merged)


# merge the different  columns based on marks and age 

marks_df= pd.DataFrame({
       
        "ID":[1,2,3],
        "Name":["suresh","Sai","charan"],
        "Age":[25, 30 ,35]
         })

age_df = pd.DataFrame({
        "ID":[1,2,4],
        "Marks":[85,90,95]
        })

merged_df = pd.merge(marks_df,age_df,on = "ID",how = "inner")
print(merged_df)

