import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df.info())
print(df.describe())

df["Age"]=df["Age"].fillna(df["Age"].median())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])

df=df.drop_duplicates()

first_class=df[df["Pclass"]==1]
print("FIRST CLASS PASSENGERS :\n",first_class.head())

# survived_by_class= df.groupby("Pclass")["Survived"].mean()
# survived_by_class.plot(kind="bar",color="skyblue")
# plt.title("Survival rate by class")
# plt.ylabel("Survival rate")

# sns.histplot(df["Age"],kde=True,bins=20,color="purple")
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

plt.scatter(df["Age"] , df["Fare"], alpha=0.5, color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()