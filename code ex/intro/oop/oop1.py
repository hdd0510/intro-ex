class Fraction():
    def __init__(self, num, deno):
        self.num = num
        self.deno = deno
    def __str__(self):
        return str(self.num) + "/" + str(self.deno)
    def __add__(self, other):
        res_num = self.num * other.deno + self.deno * other.num
        res_deno = self.deno * other.deno
        return Fraction(res_num, res_deno)  
    def __subtract__(self, other):
        res_num = res_num = self.num * other.deno - self.deno * other.num
        res_deno = self.deno * other.deno
        return Fraction(res_num, res_deno)
    def __float__(self):
        return self.num / self.deno
    def inverse(self):
        return Fraction(self.deno, self.num)