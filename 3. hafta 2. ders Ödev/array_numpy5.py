# 5 - two arrays to be combined into one

import numpy as np

arr1 = np.random.randint(0, 2, size=(5, 3))
print(arr1)

arr2 = np.random.randint(0, 2, size=(5, 3))
print(arr2)

# Combine arr1 and arr2 into a single array in case of rows
combined_rows = np.concatenate((arr1, arr2), axis=0)
print("Combined Rows:\n", combined_rows)

# Combine arr1 and arr2 into a single array in case of columns
combined_columns = np.concatenate((arr1, arr2), axis=1)
print("Combined Columns:\n", combined_columns)

