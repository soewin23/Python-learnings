# Static Methods 

# Methods that don't use slef parameter ( work at class leval)

"""class Student:
    @staticmethod # decorator
    def college():
        print("ABC college")"""

class Greed:
    @staticmethod
    def hello():
        print("hello world")
Greed.hello()

class Student_info:

    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
# using static method
    @staticmethod
    def greed():
        print(f"hello Dear student")


    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"{self.name}'s marks is {sum/len(self.marks)}")

s1 = Student_info("bimal",[12,23,23,45])
Student_info.greed()
s1.get_average()
