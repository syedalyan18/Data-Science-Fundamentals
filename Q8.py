import pandas as pd
import numpy as np

d1=pd.DataFrame({
    "Name":["Alice","Bob","Charlie"],
    "Age":[24,25,27],
    "Score":[85,87,88],
})
d2=pd.DataFrame({
    "Name":["Alice","Bob","Charlie"],
    "Section":["A","B","C"]
})
merged=pd.merge(d1,d2,how="inner",on="Name")
print("MERGED DATASET :\n\n",merged)

merged["PERCENTAGE "]=(merged["Score"]/100)*100
print("\nUPDATED MERGED DATASET :\n\n",merged)
