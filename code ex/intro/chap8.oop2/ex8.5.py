# Define a new class called SquareMatrix, which is a descendant of the class Matrix in the previous homework. Add the __pow__ exponentiation operation that takes a natural power (including zero) to which you want to raise the matrix.

# For example:

# Test	
    # m = SquareMatrix([[1, 0], [0, 1]])
    # print(isinstance(m, Matrix))
    # m = SquareMatrix([[1, 1], [0, 1]])
    # print(m ** 0)
    # print(m ** 2)
# Result
    # True
    # 1	0
    # 0	1
    # 1	2
    # 0	1



from functools import reduce
class Matrix:
    def __init__(self, mat):
        self.mat = mat
def mul(matA, matB):
    m = len(matA)
    n = len(matA[0])
    p = len(matB[0])
    res = [[] for i in range(m)]
    for i in range(m):
        for j in range(p):
            factor = sum(matA[i][k] * matB[k][j] for k in range(n))
            res[i].append(factor)
    return res 
    
class SquareMatrix(Matrix):
    def __init__(self, mat):
        super().__init__(mat)
    def __pow__(self, n):
        if n == 0:
            return [[1,0], [0,1]]
        if n == 1:
            res = [" ".join(str(i) for i in x) for x in self.mat]
            return reduce(lambda x, y: x + "\n" + y, res)
        if n == 2:
            a = mul(self.mat, self.mat)
            res = [" ".join(str(i) for i in x) for x in a]
            return reduce(lambda x, y: x + "\n" + y, res)
        else:
            a = mul(self ** (n-1), self.mat) 
            res = [" ".join(str(i) for i in x) for x in a]
            return reduce(lambda x, y: x + "\n" + y, res)

m = SquareMatrix([[1, 0], [0, 1]])
print(isinstance(m, Matrix))
m = SquareMatrix([[1, 1], [0, 1]])
print(m ** 1)
print(m ** 2)