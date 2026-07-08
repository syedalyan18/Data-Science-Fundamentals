import numpy as np

# Create a 4x4 matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

print("Matrix:\n", matrix)

# Sum of rows
row_sum = np.sum(matrix, axis=1)
print("Row sums:", row_sum)

# Sum of columns
col_sum = np.sum(matrix, axis=0)
print("Column sums:", col_sum)
