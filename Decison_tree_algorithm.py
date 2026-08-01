from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# loading the model inputs 
cancer =load_breast_cancer()
x,y=cancer.data,cancer.target

# classing the test data and trian data 
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=42)


# loadin the deciosn tree algorthmi model  and giving the condtions 

tree=DecisionTreeClassifier(criterion='entropy',max_depth=3)
tree.fit(x_train,y_train)

# predicting the output 

y_pred= tree.predict(x_test)
print(y_pred)

# find the accuracy as metric 

accuracy=accuracy_score(y_test,y_pred)
print("Decison tree accuracy: ",accuracy)