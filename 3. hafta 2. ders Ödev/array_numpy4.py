# 4- slicing

import numpy as np
array2 = np.array([[1,2,6,7], [4,3,9,5]])

array3 = np.array([[[7,5,14],[21,8,11]],
                    [[8,6,20],[14,3,9]]])

print(array2[0, 1:3])    
print(array2[1, 1:])

print(array3[0, 1, :]) 
print(array3[1, 0, 1:])