import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# dataset creation 

# we are creatimg this data set for house  price prediction 

data = {
    "size" : [1000,1500,2000,2500,3000],
    "price" : [200000,250000,300000,350000,400000]   
}

# above data called raw data 

# i nned to convert raw data into dataframes 


df = pd.DataFrame(data)

x = df[["size"]]   # x is my input feature 
y = df[["price"]]  # y is output y 


# train the model 

model = LinearRegression()
model.fit(x,y)


# calculate the cofficient w valve 

print("slope (W) : ", model.coef_)

# step : 1 caluculate the intercept b valve 

print("intercept (b) :",model.intercept_)



#  step 2 : prediction 

new_size = np.array([[2200]])
predicted_price = model.predict(new_size)

print("predicted_price : ",predicted_price)


# evaluating the model using metrics 

y_pred = model.predict(x)

# we will use the metrics to fimd the difrrence between the predicted valve (y) & actual valve 

print("MSE : ",mean_squared_error(y,y_pred))

print("R2 score ; ",r2_score(y, y_pred))


# visualization using matplotlib ( scatterplot)

plt.scatter(x,y, color="blue",label="Actual Data")
plt.plot(x,y_pred, color="red",label="Regression Line")
plt.xlabel("House Size (SQ FT)")
plt.ylabel("Price")
plt.title("Linear Regression Model")
plt.legend()
plt.show()



























