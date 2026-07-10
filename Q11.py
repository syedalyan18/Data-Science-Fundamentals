import pandas as pd

df = pd.DataFrame({
    "ID":[1,2,3,4],
    "Color":["Red","Blue","Green","Red"]
})

print("Original DataFrame:\n", df)

# One-hot encoding
df_encoded = pd.get_dummies(df, columns=["Color"])

print("\nAfter One-Hot Encoding:\n", df_encoded)
