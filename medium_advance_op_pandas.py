import pandas as pd
from requests import head 

df= pd.read_csv("/Users/manjunathareddy/Downloads/genai_llm_usage_dataset_1000 2.csv")

print(df)

# using groupby method to group the dataset by application_domain and calculate the mean, median, and min of total_tokens
print(df.groupby("application_domain")["total_tokens"].mean())

print(df.groupby("application_domain")["total_tokens"].median())

print(df.groupby("application_domain")["total_tokens"].min())


# filterring on the dataset to spefic condition 

filter = df[df["user_satisfaction"] > 3]
print(filter)


filter1 = df[df["prompt_length"]>1000]
print(filter1)


# using filter by selcting and filterning an specific row 
print(df[df["application_domain"] == "Healthcare"])


# using filter by selcting and filterning an specific row
print(df[df["task_type"] == "Classification"])



