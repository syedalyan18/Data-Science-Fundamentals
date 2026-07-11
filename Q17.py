import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
del df['species']
corr_matrix=df.select_dtypes(include="number").corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("CORRELATION HEATMAP")
plt.show()