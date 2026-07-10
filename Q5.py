import pandas as pd
s=pd.Series([2,3,4],["a","b","c"])
print(s)

print("\n")
data={"Name ": ["Alice","Bob"],"Age":[18,19]}
df=pd.DataFrame(data)
print(df)