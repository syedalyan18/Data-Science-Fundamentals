import pandas as pd

# Example datasets
df1 = pd.DataFrame({"ID":[1,2,3], "Name":["Alice","Bob","Charlie"]})
df2 = pd.DataFrame({"ID":[1,2,3], "Age":[25,30,35]})
df3 = pd.DataFrame({"ID":[1,2,3], "Score":[85,90,95]})

# Merge them on 'ID'
merged = df1.merge(df2, on="ID").merge(df3, on="ID")

print("Merged DataFrame:\n", merged)

# Analyze relationships (correlation between Age and Score)
print("\nCorrelation:\n", merged[["Age","Score"]].corr())
