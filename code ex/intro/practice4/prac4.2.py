# Write a function to convert the numpy matrix into a percentage matrix: each element in a line is converted into its percentage of the sum of elements in that line (no need for rounding)
# Input:
# print(convert(np.arange(0, 9).reshape(3, 3)))
# Output:
# [[0.         0.33333333 0.66666667]
#  [0.25       0.33333333 0.41666667]
#  [0.28571429 0.33333333 0.38095238]]
import numpy as np
def convert(a):
    b = []
    m, n = a.shape
    for i in a:
        b.append([i[j]/sum(i) for j in range(n)])
    return np.array(b)  
print(convert(np.arange(0, 9).reshape(3, 3)))