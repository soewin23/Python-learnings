# method 
 
#  Methods are functions that belong to objects

class Student:
    def __init__(self, name, marks):#        <--
        self.name = name #                     |-- constructor
        self.marks = marks #                 <--

    def greed(self):
        print("WElcome Student", self.name)
    def get_marks(self):
        return self.marks


s1 = Student("bimal", 99)
s1.greed()
print(s1.get_marks())