import pandas as pd
from requests import head 

df= pd.read_csv("/Users/manjunathareddy/Downloads/genai_llm_usage_dataset_1000 2.csv")
# i nned to perform the indexing of the data
# select the cloumn from dataset 
col1=df["task_type"]
print(col1)
# multiple columns 
mul_col = df[["temperature","top_p"]]
print(mul_col)

# selct row from index 

print(df.iloc[14])



# filter the rows where prompt is greater than 1000
fil_rows = df[df["prompt_length"]> 1000]
print(fil_rows)

find = df[df["application_domain"] == "Healthcare"]
print(find)


# modify the valves from the dataset 
df.loc[1,"application_domain"] = "Education"
df.loc[2,"application_domain"] = "Finance"
print(df.loc[1,"application_domain"])
print(df.loc[2,"application_domain"])

print(df.head(10))


# group by the dataset uyisng the prompt_length cal the mean valve 

print(df.groupby("prompt_length")["total_tokens"].mean())