# Encapsulation
# Wrapping data and functions into a single unit (object) 

class me:
    @staticmethod
    def Greeding():
        print("hello Pythonic Guys!")


    def __init__(self,name, age, country):
        self.name = name
        self.age = age
        self.country = country
    def get_info(self):
        print(f"I'm {self.name}.\nI'm {self.age} years olds.\nand from{self.country}")
        
me.Greeding()
a1 = me("bimal",18, "Earth")
a1.get_info()
