import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error
import numpy as np

#loading of dataset

data = pd.read_csv("project-2\clean.csv")

#defining input and output
X = data[["Study_Hours_per_Week"]]
Y = data["Final_Score"]

model = LinearRegression()
model.fit(X,Y)

predicted_score = model.predict(X)

mae = mean_absolute_error(Y, predicted_score)
mse = mean_squared_error(Y, predicted_score)
rmse = np.sqrt(mse)

# print("MAE:", mae)
# print("MSE:", mse)
# print("RMSE:", rmse)


check = float(input("Enter hours: "))
outcome = model.predict(pd.DataFrame([[check]], columns=["Study_Hours_per_Week"]))

print("Predicted score:", outcome[0])
