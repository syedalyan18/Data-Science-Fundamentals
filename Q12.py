import pandas as pd

data={
    "Class":["A","B","A","A","C","B"],
    "Score":[76,68,87,65,80,91],
    "Age" :[17,17,18,19,18,17]
}
df=pd.DataFrame(data)
print("ORIGINAL DATASET :\n",df)

result=df.groupby("Class").agg( {"Score":
    ["mean", "max","min"],"Age":["mean", "max", "min"]})
print("\nGROUPED DATASET :\n",result)