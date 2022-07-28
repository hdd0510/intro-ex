# Solve the system of linear equation Ax = b, knowing the augmented matrix [A|b]. It is guaranteed that the system of the linear equation has n equations, n variables, and a single solution


# Example: 

# a + 3b - 2c = 5
# 3a + 5b + 6c = 7
# 2a + 4b + 3c = 8
# Input:
# a = np.array([[1, 3, -2, 5],                                           Output:[[-15.]
#               [3, 5, 6, 7],                                                    [  8.]
#               [2, 4, 3, 8]])                                                   [  2.]]
# 	             
# 	            
# print(system_solver(a))
import numpy as np

def system_solver(a):
    m, n = a.shape
    A, B = a[0:, ([i for i in range(n-1)])], a[0:, -1].reshape(m, 1)
    return np.linalg.inv(A).dot(B)    #or np.linalg.solve(A,B)
