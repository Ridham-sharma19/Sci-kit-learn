import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler

from sklearn.model_selection import train_test_split

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Scores": [50, 55, 60, 65, 70, 75, 80, 85]
}

df = pd.DataFrame(data)

#standard_scaler
# standard_scaler = StandardScaler()
# standard_scaled = standard_scaler.fit_transform(df)

# print("Standard Scaler output:")
# print(pd.DataFrame(standard_scaled,columns=["Study_Hours","Scores"]))

#Min Max SCaler

min_max_scaler = MinMaxScaler()
min_max_scaled = min_max_scaler.fit_transform(df)
#print(pd.DataFrame(min_max_scaled,columns=["Study_Hours","Scores"]))

x = df[["Study_Hours"]]
y = df[["Scores"]]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print("Train Data")
print(x_train)

print("Test Data")
print(x_test)

print("Train Data")
print(y_train)

print("Test Data")
print(y_test)