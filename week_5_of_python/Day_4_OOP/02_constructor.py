# __init__ function  <---- Constructor

# All class havve a function called __init__(), which is always executed when the class is being initiated. 


class Student:

    School_name = "ABC School"# <--- attribute

   # parameterized construcerd
    def __init__(slef, name, marks):
        slef.name = name # object attribute
        slef.marks = marks
        print('adding new student in Database...')

s1 = Student("soe",97)
# obj attr > class attr 
print(s1.name, s1.marks)


s2 = Student("Arno",98)
print(s2.name, s2.marks)

print(s2.School_name)
