# Private(like) attributes & methods

# Conceptional Implementations in python

# Private attributes & methods are ment to be used only within
# the class and are not accessible from outside the class 

class Account:
    def __init__(self, acc_num, acc_pass ):
        self.acc_num = acc_num
        # private __
        # we can't access this outside of the class
        self.__acc_pass = acc_pass
#if we try to print it will shows an error


# it will work inside the class 
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcd")

"""print(acc1.acc_num)
print(acc1.reset_pass())
print(acc1.__acc_pass)"""

class hi:
    def __init__(self, greed):
        self.__greed = greed

    def greed(self):
        print(self.__greed)

a = hi("Hello World!")
print(a.greed())
    
