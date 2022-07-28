class Student():
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id 
        self.grade = grade
    def __str__(self):
        return f"Name: {self.name} \nID: {self.id} \nGrade: {self.grade}"
    def __lt__(self, other):
        return self.grade < other.grade
    def __eq__(self, other):
        return self.id == other.id
    def GradeType(self):
        if self.grade >= 3.6:
            return "Excellent"
        if 3.2<= self.grade < 3.6:
            return "Good"
        if 2.5<= self.grade < 3.2:
            return "Fair"
        else:
            return "Poor"