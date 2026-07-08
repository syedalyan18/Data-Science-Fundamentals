# import numpy as np

# # Create a 4x4 matrix
# matrix = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]])

# print("Matrix:\n", matrix)

# # Sum of rows
# row_sum = np.sum(matrix, axis=1)
# print("Row sums:", row_sum)

# # Sum of columns
# col_sum = np.sum(matrix, axis=0)
# print("Column sums:", col_sum)



# import numpy as np

# # Example array
# arr = np.array([10, 20, 30, 40, 50])

# # Normalize (min-max scaling)
# normalized = (arr - arr.min()) / (arr.max() - arr.min())

# print("Original array:", arr)
# print("Normalized array:", normalized)

import numpy as np

# Generate random array of size 10
random_arr = np.random.randint(1, 100, size=10)

print("Random array:", random_arr)
print("Minimum value:", random_arr.min())
print("Maximum value:", random_arr.max())


