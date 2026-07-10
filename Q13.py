import pandas as pd
 
data = {
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Year": [2021, 2021, 2021, 2021, 2022, 2022],
    "Sales": [100, 150, 200, 130, 180, 220]
}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

pivot = pd.pivot_table(df, values="Sales", index="Region", columns="Year", aggfunc="sum")

print("\nPivot Table:\n", pivot)

variance = df.groupby("Region")["Sales"].agg(lambda x: x.var())

print("\nVariance of Sales per Region:\n", variance)

