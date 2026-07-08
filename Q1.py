import numpy as np

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("ORIGINAL MATRIX : \n",matrix)
transpose=matrix.T
# print("TRANSPOSE MATRIX : \n",transpose)

matrix2=np.array([[9,8,7],[6,5,4],[3,2,1]])
# print("ADDITION : \n", matrix + matrix2)
# print("MULTIPLICATION : \n", matrix * matrix2)

arr=np.array([1,3,5,6,7,8,9,2,4])
print(arr[2:5])

# reshaped=arr.reshape(3,3)
# print(reshaped)

nums=np.arange(0,6,3)
print(nums)

nums2=np.linspace(0,1,4)
print(nums2)