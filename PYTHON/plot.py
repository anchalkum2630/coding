import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\envy\Downloads\Titanic-Dataset.csv")
data=pd.DataFrame(df)
data=pd.DataFrame(df)
print(df.head())
print(data.head())
print(data.describe())
x=data.shape
print(x)
a=data['PassengerId']
b=data['Age']
fig = plt.figure(figsize=(20, 8))
plt.scatter(a,b)
plt.xlabel("PassengerId")
plt.ylabel("Age")
plt.bar(a,b)
plt.xlabel("PassengerId")
plt.ylabel("Age")
plt.show()

print(df.shape)
rows,column=df.shape
print(rows)
print(df.head(2)) 
print(df.tail(2))
print(df[2:5])
print(df.columns)
print(type(df.Survived))
print(df.Age.max())
print(df.index)