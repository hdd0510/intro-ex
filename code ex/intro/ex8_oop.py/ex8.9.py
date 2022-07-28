# Let an instance M of the Matrix class is a square matrix that defines a system of linear algebraic equations: Mx = b
# Your task is to add a solve method to the previous class Matrix that accepts a row vector b of free members and returns a string consisting of float numbers that represent the solution of the system of linear equations. The float numbers are separated by spaces and each number is displayed using two digits after the decimal points.
# It is guaranteed that the system has always a unique solution.
# For example:

# Test	
#   m = Matrix([[1, 1, 1], [0, 2, 0], [0, 0, 4]])
#   print(m.solve([1,1,1]))
# Result
#   0.25 0.50 0.25


from copy import deepcopy

def A(m, i, j):
    a = deepcopy(m)
    a.pop(i)
    for y in a:
        y.pop(j)
    return a
def det(mat):
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    return sum((-1)**(1+(j+1)) * mat[0][j] * det(A(mat, 0, j)) for j in range(len(mat))) 
def inverse(mat):
    res = [[] for i in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            res[i].append((-1)**(i+j) * det(A(mat, j, i)) / det(mat))
    return res
class Matrix:
    def __init__(self, mat):
        self.mat = mat
    def solve(self, B):
        A = inverse(self.mat)
        res = []
        for x in A:
            res.append("%.2f" % float(sum([x[i] * B[i] for i in range(len(B))])))
        return " ".join(str(i) for i in res)
