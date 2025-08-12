# Create a student class that takes name & marks of 3 subkects as argument in constructure
# then create a method to print the average


class Student:
    def __init__(self, name , marks):
        self.name = name #class atributes
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name}, YOur marks are : {sum/len(self.marks)}")


s1 = Student("Soe wim", [12,11,13]) #object attribute
print(s1.name, s1.marks)


s1.get_avg()


# mainplating the attributes in Classes
s1.name = "bimal"
s1.marks= [90,91,92,93]
print(s1.name, s1.marks)

s1.get_avg()