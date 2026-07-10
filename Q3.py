import numpy as np

# Create a 3D random array (shape: 3x4x5)
arr_3d = np.random.rand(3, 4, 5)
print("3D Array:\n", arr_3d)

# Compute statistics along axes
mean_axis0 = np.mean(arr_3d, axis=0) 
mean_axis1 = np.mean(arr_3d, axis=1)  
mean_axis2 = np.mean(arr_3d, axis=2)  

print("\nMean along axis 0:\n", mean_axis0)
print("\nMean along axis 1:\n", mean_axis1)
print("\nMean along axis 2:\n", mean_axis2)
