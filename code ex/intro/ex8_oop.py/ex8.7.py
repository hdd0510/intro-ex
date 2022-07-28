from copy import deepcopy
from functools import reduce
class Matrix:
    def __init__(self, lst):
        self.lst = lst
    def __str__(self):
        lines = []
        for i in range(len(self.lst)):
            lines.append("\t".join(str(i) for i in self.lst[i]))
        res = reduce(lambda x, y: x + "\n" + y, lines)
        return res
    def Constructor(self):
        lst_fake = self.lst.deepcopy()
        return lst_fake
    def size(self):
        num_of_row = len(self.lst)
        num_of_col = len(self.lst[0])
        return (num_of_row, num_of_col)
