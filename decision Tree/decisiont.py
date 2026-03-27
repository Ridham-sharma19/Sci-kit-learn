from sklearn.tree  import DecisionTreeClassifier

#x->size,color shade
#y->fruit
x=[[7,2],[8,3],[9,8],[10,9]]
y=[0,0,1,1]#0->apple,1->orange

model = DecisionTreeClassifier()

model.fit(x,y)
color_shade = float(input("Enter the weight of the fruit: "))
size = float(input("Enter the size of the fruit: "))    
predicted_fruit = model.predict([[color_shade, size]])[0]
print(f"The predicted fruit is: {predicted_fruit}")

