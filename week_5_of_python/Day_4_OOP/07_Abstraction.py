# Abstraction 
# Hiding the implementatioin details of a class and only the showing the essential features to the user 
 

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False

    def start(self):
        self.cluch = True # we hide the unnecessary information
        self.acc = True
        print("Car started....")        

car1= Car()
car1.start()