from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error

y_true=[90,80,70,10,60]

y_pred = [100,83,69,8,55]

mae = mean_absolute_error(y_true,y_pred)
mse = mean_squared_error(y_true,y_pred)
rmse = root_mean_squared_error(y_true,y_pred)

print("Mean_Absolute_Error",mae)
print("Mean_Square_Error",mse)
print("Root_Mean_Square_Error",rmse)