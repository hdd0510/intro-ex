import math

class Figure:
    def perimeter(self):
        pass
    
    def area(self):
        pass
    
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def get_height_a(self):
        return self.area()/self.a * 2 
    def get_height_b(self):
        return self.area()/self.b * 2
    def get_height_c(self):
        return self.area()/self.c * 2
    