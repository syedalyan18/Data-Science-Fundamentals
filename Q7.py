import pandas as pd
import numpy as np

data={
    "Name":["Alice",np.nan,"Charlie"],
    "Age":[24,25,np.nan],
    "Score":[85,np.nan,88],
}
df=pd.DataFrame(data)
print("DATASET : \n",df)

df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()
print("UPDATED DATASET : \n",df)

df=df.rename(columns={"Name":"STUDENT_NAME", "Age":"STUDENT_AGE"})
print("UPDATED COLUMNS : \n",df)