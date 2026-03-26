import pandas as py

data ={
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"],
    "Age": [25, 30, None, 40, 45, 50, 55, None],
    "City": ["New York", "Los Angeles", "Chicago", None, "Phoenix", "Philadelphia", None, "San Diego"]

}
df = py.DataFrame(data);
# print(df.isnull().sum());
# df_drop = df.dropna()
# print(df_drop)

# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["City"] = df["City"].fillna(df["City"].mode()[0])
print(df.isnull().mean()*100)
