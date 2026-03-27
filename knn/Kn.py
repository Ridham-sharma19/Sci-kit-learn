from sklearn.neighbors import KNeighborsClassifier

#x=>wt,size
#y=>fruit

x=[[180,7],[200,7.5],[170,6],[160,6.5],[150,5.5],[140,3],[200,8],[190,7.8],[210,8.5]]
y=["apple","apple","orange","orange","grape","grape","apple","apple","apple"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)
wt = float(input("Enter the weight of the fruit: "))
size = float(input("Enter the size of the fruit: "))    
predicted_fruit = model.predict([[wt, size]])[0]
print(f"The predicted fruit is: {predicted_fruit}")