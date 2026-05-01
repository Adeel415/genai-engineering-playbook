class Student:
    def __init__(self,name,age):
        self.name=name 
        self.age=age

    def display(self):
        print(f"My NAme is {self.name}\n My age is {self.age}")



s1=Student("Adeel",22)
s1.display()