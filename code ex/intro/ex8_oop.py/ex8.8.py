from functools import reduce
from copy import deepcopy

class Matrix:
    def __init__(self, mat):
        self.mat = mat
    
    def __str__(self):
        lines = []
        for i in range(len(self.mat)):
            lines.append("\t".join(str(i) for i in self.mat[i]))
        res = reduce(lambda x, y: x + "\n" + y, lines)
        return res
    
    def __add__(self, another):
        res = deepcopy(self.mat)
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                res[i][j] += another.mat[i][j]
        return Matrix(res)
    
    def __mul__(self, m):
        fake_mat = deepcopy(self.mat)
        for x in fake_mat:
            for y in range(len(x)):
                x[y] *= m
        return Matrix(fake_mat)
    
    def __rmul__(self, m):
        fake_mat = deepcopy(self.mat)
        for x in fake_mat:
            for y in range(len(x)):
                x[y] *= m
        return Matrix(fake_mat)
    


        


