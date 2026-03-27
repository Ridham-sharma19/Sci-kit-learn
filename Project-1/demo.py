import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

data = pd.read_csv("Project-1/student.csv")

X = data[["Hours"]]
Y = data["Score"]   # 1D

model = LinearRegression()
model.fit(X, Y)

predicted_score = model.predict(X)

# Evaluation
mae = mean_absolute_error(Y, predicted_score)
mse = mean_squared_error(Y, predicted_score)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

# Prediction
check = float(input("Enter hours: "))
outcome = model.predict(pd.DataFrame([[check]], columns=["Hours"]))

print("Predicted score:", outcome[0])

