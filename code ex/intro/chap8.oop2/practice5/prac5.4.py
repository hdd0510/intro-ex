class Rectangle():
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        
    def perimeter(self):
        return (self.width + self.height) * 2
    
    def area(self):
        return self.width * self.height
    def set_width(self, newid):
        self.width = newid
    def set_height(self, newhei):
        self.height = newhei

class Square(Rectangle):
    def __init__(self, a):
        self.width = a
        self.height = a
    def set_height(self, b):
        self.height = b 
    def set_width(self, b):
        self.width = b