# implementation of knn algorithm using the iris datset 

from sklearn.datasets import load_iris
from  sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# describing the data

iris = load_iris()
x,y = iris.data, iris.target


# use trian and split we will trian and test the data 

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=42)


# model selction where we are selcting algorthm of model

knn =KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train,y_train)


# predict the the output and diaplay 


y_pred = knn.predict(x_test)

print("prediction is ",y_pred)

# i nned to find the accuracy of this knn using accuracy as an metric 

accuracy = accuracy_score(y_test,y_pred)


print("KNN Accuracy :",accuracy)














