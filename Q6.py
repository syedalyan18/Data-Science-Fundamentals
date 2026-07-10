import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
# print(df[["species","sepal_length"]])

filtered_rows=df[(df["sepal_length"] > 5.0) & (df["species"]== "setosa")]
print(filtered_rows)