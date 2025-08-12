        #   Inheritance

# When one class(child/derived) derives the properties & methods of another 
# class (parent/base )
"""Example"""
class Car:
    pass
# means we are taking info from the parent Class

class ToyotaCar(Car):
    pass



## practice
class Car():
    color = "black"
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("Car stopped")
    
class TeslaCar(Car):
    def __init__(self, name):
        self.name  = name

car1 = TeslaCar("Tesla-MOdel-S")
print(car1.name)
print(car1.color)
print(car1.start())
print(car1.stop())
print("---------------")
print()

car2 = TeslaCar("Tesla-Model-E")
print(car2.name)
print(car2.color)
print(car2.start())
print(car2.stop())
print("---------------")
print()

car3 = TeslaCar("Tesla-Model-A")
print(car3.name)
print(car3.color)
print(car3.start())
print(car3.stop())
print("---------------")
print()

car4 = TeslaCar("Model-X")
print(car4.name)
print(car4.color)
print(car4.start())
print(car4.stop())
print("---------------")
print()

car5 = TeslaCar("Tesla-Model-Y")
print(car5.name)
print(car5.color)
print(car5.start())
print(car5.stop())
print("---------------")
print()





