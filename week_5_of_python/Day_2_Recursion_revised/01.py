# recursive function 

def show(n):
    if n == 0:# base case for controlling the recursion
        return
    """Base case in important if base case is not there is can run infinaltely
    exceeding the memory and then crash the program"""
    print(n)
    show(n-1)
show(5)# n-1=4 n-1=3....

