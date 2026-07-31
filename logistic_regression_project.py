import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

# daatset of an student wheather based on the marks they will pass/fail


data = {
    "marks" : [30,45,50,60,70,80,90],
    "pass" :  [0,0,1,1,1,1,1]
}

# i nned to convert raw data into data frames 

df =pd.DataFrame(data)
print(df)


# describe the inputs to pass the model

x = df[["marks"]] # feauture
y = df["pass"] # target


# step ; 3

# train - test split on input features 

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


#step 4 : train the logistic regression model 

model = LogisticRegression()
model.fit(x_train,y_train)

# step 5 : predictions

y_pred=model.predict(x_test)


# step 6 : Evaluation  & metric score 

print("Accuracy :",accuracy_score(y_test,y_pred))

# above strp it will compare my actual test score with preduicted one 

print("confusion matrix:\n",confusion_matrix(y_test,y_pred))


print("classification report :\n",classification_report(y_test,y_pred))



# step : 7 : visualization or (sigmod curve)


marks_range = np.linspace(30,90,100).reshape(-1,1)
probabilities =model.predict_proba(marks_range)[:,1]

# step : 8 : matplotlib

plt.scatter(x,y,color="blue",label="Actual Data")

plt.plot(marks_range,probabilities,color="red",label="Sigmoid Curve")
plt.xlabel("marks")
plt.ylabel("Probabilty of passing")
plt.title("Logistic Regression : Marks vs Pass/Fail")
plt.legend()
plt.show()
