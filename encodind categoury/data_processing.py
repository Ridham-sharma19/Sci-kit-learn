from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("sample_data.csv")

df_label = df.copy()

le_gender = LabelEncoder()
le_passed = LabelEncoder()

df_label["Gender_Encoded"] = le_gender.fit_transform(df_label['Gender'])
df_label["Passed_Encoded"] = le_passed.fit_transform(df_label['Passed'])

# print('\nLabel encoded data')
# print(df_label[["Name","Gender","Gender_Encoded","Passed","Passed_Encoded"]].head(5))


df_encoded = pd.get_dummies(df_label,columns=["City"],dtype=int)

print(df_encoded)
