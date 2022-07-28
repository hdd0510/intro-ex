class Rect():
    def __init__(self, wid, len):
        self.wid = wid
        self.len = len
    def __str__(self):
        return "<Width = " + str(self.wid) + ", Height = " + str(self.len) +">"
    def area(self):
        return self.wid * self.len
    def perimeter(self):
        return 2*(self.wid + self.len)
        
