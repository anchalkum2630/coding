import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\envy\Downloads\Titanic-Dataset.csv")
data=pd.DataFrame(df)
print(data.head())
print("=========================================================================")
print(data.describe())
print("=========================================================================")
x=data.shape
print(x)
print("=========================================================================")

rows,column=df.shape
print(rows)
print("=========================================================================")
print(df.head(2)) 
print("=========================================================================")
print(df.tail(2))
print("=========================================================================")
print(df[2:5])
print("=========================================================================")
print(df.columns)
print("=========================================================================")
print(type(df.Survived))
print("=========================================================================")
print(df.Age.max())
print("=========================================================================")
print(df.index)
print("=========================================================================")

a=data['PassengerId']
b=data['Age']
# fig = plt.figure(figsize=(8,8))

# a1=data['Age']
# b1=data["Pclass"]
# plt.bar(a1,b1,color="blue")

plt.scatter(a,b)
plt.xlabel("PassengerId")
plt.ylabel("Age")

# plt.bar(a,b,color="blue")
# plt.xlabel("PassengerId")
# plt.ylabel("Age")


# sex_counts = df.groupby('Sex')['Age'].count()
# sex_counts.plot(kind='bar', color=['blue', 'pink'])

# sns.histplot(b)

plt.show()
