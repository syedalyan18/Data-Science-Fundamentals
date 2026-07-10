import pandas as pd
import numpy as np

data = {
    "A": [1, 2, np.nan, 4, np.nan],
    "B": [np.nan, np.nan, np.nan, np.nan, 5],
    "C": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

# Drop columns with more than 50% missing values
threshold = 0.5 * len(df)
df_clean = df.dropna(thresh=threshold, axis=1)

print("\nAfter dropping columns:\n", df_clean)
