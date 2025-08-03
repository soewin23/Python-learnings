## Recursion

# means calls a function itself


# to work correctly function must have :

# Base Case      -- The condition where the recursion stops 
# Recursive Case --- the function call itself with smaller input

#Greed
def greet(n):
    if n== 0 :
        return "None" #base case
    print("hello")
    greet(n-1) #recursive case

greet(8)

#factorial
def factorial(n):
    if n == 0 or n == 1:# base case
        return 1
    return n* factorial(n -1)#recursive case
print(factorial(5))# output 120


# Sum of first N numbers
def sum(n):
    if n ==1: # base case
        return 1
    return n + sum(n-1)#recursive case
print(sum(100))# 5050



# The fibonacci Sequence

def fibonacci(n):
    if n == 0:# base case
        return 0
    elif n== 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)# recursive casw
print(fibonacci(10))

#debugging Recursion with Print
def countdown(n):
    print("Entering :",n)
    if n == 0: # base case
        print("Base Case reached")
        return
    countdown(n-1)#recursion case
    print("Exiiting",n)
countdown(3)
