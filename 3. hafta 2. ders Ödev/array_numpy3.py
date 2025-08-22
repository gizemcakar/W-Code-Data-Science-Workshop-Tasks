# 3 - indexing of arrays

import numpy as np
array2 = np.array([[1,2,6,7], [4,3,9,5]])

array3 = np.array([[[7,5,14],[21,8,11]],
                   [[8,6,20],[14,3,9]]])


print(array2[0, 1])

print(array2[0, 3])

print(array3[1, 1, 2])

print(array3[0, 0, 1])
