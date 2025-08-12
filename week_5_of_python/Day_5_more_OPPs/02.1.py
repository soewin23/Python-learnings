class Person:
    __name = "Unknown"

# definding a private functiion in class
    def __hello(self, ):
        print(" hello world!")
    
    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())
# print(p1.__name)
