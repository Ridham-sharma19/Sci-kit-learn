from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score

#true value actually what happened
y_true=[1,0,1,1,0,1,0]
#what model guesses
y_pred=[1,0,1,0,0,1,1]

#evaluation
print(F"Accuracy score {accuracy_score(y_true,y_pred)}")
print(F"Precision score {precision_score(y_true,y_pred)}")
print(F"recall score {recall_score(y_true,y_pred)}")
print(F"f1 score {f1_score(y_true,y_pred)}")
