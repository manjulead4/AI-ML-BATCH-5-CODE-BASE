import pandas as pd
from requests import head

df= pd.read_csv("/Users/manjunathareddy/Downloads/genai_llm_usage_dataset_1000 2.csv")

print(df)


# inspecting an data 
print(df.head(10)) # printing the first 10 rows of the dataset
# info of data set 
print(df.info())

# using describe method to get the statistical summary of the dataset
print(df.describe())
# using the describe method to get the statistical summary of specific columns
print(df[["prompt_length","temperature"]].describe())
# i nned to get only min and max valves of the dataset
print(df[["prompt_length","temperature"]].agg(["min","max"]))

#average of these columns
print(df[["prompt_length","temperature"]].agg(["mean"]))


# indexing and selecting the data from the dataset 


# i know my column name i nned to slect and print that cloumn from the datset
column = df["application_domain"]
print(column)

column1 = df["user_satisfaction"]
print(column1)

# specific number from the datset when iam sselcting the rows using iloc selctimg specific columns from the dataset
print(df.iloc[10,3])

# specifi row and range of columns from the dataset using iloc
print(df.iloc[10,3:6])



# i nned to selec tthe specific rows 
print(df.loc[10])



# i nned to modify the valve
modify = df.loc[0,"total_tokens"] = 3000
print(modify)
# i nned to printthe modifed total tokens column from the dataset
print(df.loc[0,"total_tokens"])


# i nned to modification of the dataset using loc 
modify = df.loc[20,"application_domain"] = "coding"
print(modify)

print(df.loc[20,"application_domain"])



#missimg values in the dataset
df["application_domain"].fillna(df["application_domain"].mode(),inplace=True)
print(df)
