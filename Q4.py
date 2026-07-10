import numpy as np

data = np.random.uniform(low=10, high=100, size=20)
print("Original data:\n", data)

normalized = (data - data.min()) / (data.max() - data.min())
print("\nNormalized data:\n", normalized)

threshold = 0.5

mask = (normalized > threshold).astype(int)
print("Binary mask:", mask)
