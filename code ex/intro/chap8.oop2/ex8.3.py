class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def __str__(self):
        return f"Vehicle: name = {self.name}, mileage = {self.mileage}, cap = {self.capacity}"
    def fare(self):
        return self.capacity*100
class Bus(Vehicle):
    def __init__(self, name, mileage, capacity = 50):
        Vehicle.__init__(self, name, mileage, capacity)
    def fare(self):
        return float(self.capacity*110)
    def __str__(self):
        return f"Bus: name = {self.name}, mileage = {self.mileage}, cap = {self.capacity}"