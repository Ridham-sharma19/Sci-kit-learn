from sklearn.linear_model import LinearRegression

model = LinearRegression()
x=[[1],[2],[3],[4],[5]]
y=[10,20,30,70,90]
model.fit(x,y)
hours = float(input("how many hour you studied"))
predicted_marks=model.predict([[hours]])

print(f"score prediction:-{predicted_marks}")