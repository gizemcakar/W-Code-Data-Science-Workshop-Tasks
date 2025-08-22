# 2 - dimension, size and row and column vectors
import numpy as np

array2 = np.array([[1,2,6,7], [4,3,9,5]])

array3 = np.array([[[7,5,14],[21,8,11]],
                    [[8,6,20],[14,3,9]]])

# dimension of the arrays
print(array2.ndim)
print(array3.ndim)

# size of the arrays
print(array2.size)
print(array3.size)

# shape of the arrays
print(array2.shape)
print(array3.shape)

# rows of the array2
print(array2[0]) # first row
print(array2[1]) # second row
print(array2[0, :]) # first row
print(array2[1, :]) # second row

# columns of the array2
print(array2[:, 0]) # first column
print(array2[:, 1]) # second column
print(array2[:, 2]) # third column
print(array2[:, 3]) # fourth column

