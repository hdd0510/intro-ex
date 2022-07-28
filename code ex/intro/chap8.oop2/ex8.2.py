from Polygon import *
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, no_of_sides= 3)
    def findArea(self):
        p = sum(self.sides)/2
        area = "%.2f" % (p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2]))**(1/2)
        print(f"The area of the triangle is {area}")
t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()