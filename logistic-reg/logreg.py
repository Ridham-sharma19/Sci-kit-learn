from sklearn.linear_model import LogisticRegression


model = LogisticRegression()
x=[[1],[2],[3],[4],[5]]
y=[False,False,True,True,True]
model.fit(x,y)
hours = float(input("how many hour you studied"))
predicted_marks=model.predict([[hours]])[0]

print(f"FALI OR PASS:-{predicted_marks}")