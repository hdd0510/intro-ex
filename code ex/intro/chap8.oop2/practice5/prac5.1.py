
import math

class Figure:
    def perimeter(self):
        pass
    
    def area(self):
        pass
class LengthException(Exception):
    pass
class InvalidTriangleException(Exception):
    pass
class Rectangle(Figure):
    def __init__(self, width, height):
        try:
            self.width = width
            self.height = height
            if width <= 0 or height <= 0:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) +  " was raised")
    def perimeter(self):
        res = 2*(self.height + self.width)
        return res
    def area(self):
        res = self.height * self.width
        return res
class Circle(Figure):
    def __init__(self, rad):
        try:
            self.rad = rad
            if rad <= 0:
                raise LengthException
        except LengthException as e:
                print(str(type(e)) +  " was raised")
    def perimeter(self):
        return 2*math.pi*self.rad
    def area(self):
        return (self.rad)**2 * math.pi
class Triangle(Figure):
    def __init__(self, a, b, c) -> None:
        try:
            self.a = a
            self.b = b
            self.c = c
            if a <= 0 or b <= 0 or c <=0:
                raise LengthException
            if c >= a+b or b >= a+c or a >= b+c:
                raise InvalidTriangleException
        except LengthException as e:
            print(str(type(e)) + " was raised")
        except InvalidTriangleException as e:
            print(str(type(e)) + " was raised")
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p = (self.a + self.b + self.c)/2
        res = (p*(p-self.a)*(p-self.b)*(p-self.c))**(1/2)
        return res
    
