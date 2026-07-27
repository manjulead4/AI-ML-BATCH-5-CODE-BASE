import matplotlib.pyplot as plt
import pandas as pd 

# creating an sample data of studnets and marks in each subject


data ={
    "student":["sanjay","manoj","priya","sai","latha"],
    "maths":[85,90,95,78,95],
    "physics" :[90,95,89,98,74],
    "python":[80,90,65,87,98],
    "dsa":[98,97,65,71,93]
}

# convert raw data into dataframes 

df = pd.DataFrame(data)

print(df)



# for my custom data i will perrrom the analysis and matploatlib graphs 


# 1) BAR GRAPH : average Marks per subject


avg_marks = df[["maths","physics","python","dsa"]].mean()

plt.bar(avg_marks.index, avg_marks.values, color="skyblue")
plt.title("avg marks per subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()


# LINE CHART : marks of one student across subjects 


# we will perfrom on sanjay we willp loata n line chart


student = df.loc[0,["maths","physics","python","dsa"]] 

plt.plot(student.index, student.values, marker="o", color="green")

plt.title("Marks of student sanjay across all subjects")
plt.xlabel("subjects")
plt.ylabel("Marks")
plt.show()



# scatter plot 

# this scctter plot reveals relationship between the variables 
# grapth math vs physics


plt.scatter(df["maths"], df["physics"], color = "red")
plt.title("maths vs physics Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Physics Marks")
plt.show()


# Histogram 

# this will shows the Distrubution of all Marks 
# diing graph for all marks distribution of all marks 

all_marks = df[["maths","physics","python","dsa"]].values.flatten()

plt.hist(all_marks,bins=8, color="pink",edgecolor="black")
plt.title("Distribution of marks")
plt.xlabel("Marks range")
plt.ylabel("Frequency")
plt.show()