class Person:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"NAme is {self.name}")    
        


class Student(Person):
    def __init__(self, name,course):
        super().__init__(name) 
        self.course=course


s=Student("Adeel Abid","Python OOP")

print(s.show())