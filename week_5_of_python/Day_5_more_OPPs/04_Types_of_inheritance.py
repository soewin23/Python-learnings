# Single inheritance
"""parent class 
    |
    |
   ...
child class
"""
class Car():
    color = "black"
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("Car stopped")
    
class fordCar(Car):
    def __init__(self, name):
        self.name  = name

car1 = fordCar("ford-MOdel-S")
print(car1.name)
print(car1.color)
print(car1.start())
print(car1.stop())

# Multi_level inheritance
"""base class
    |#parent
    |
   ... child
Derive class
    |#parent
    |
   ...#child
derived class"""



#Multiple inheritance