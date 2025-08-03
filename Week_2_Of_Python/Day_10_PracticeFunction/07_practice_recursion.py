# Sum of Natural Numbers (Recursive Addition)

def sum_to_n(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    return n + sum_to_n(n-1)
print(sum_to_n(5))#15
print(sum_to_n(100))#5050

# fibonacci value
def fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+ fib(n-2)
print(fib(8))#21


# Factorial 
def factorial(n):
    if n == 0 or n ==1:
        return 1
    return n * factorial(n-1)
print(factorial(5))# 120

# String revrse using recursion

def reverse_string(s):
    if len(s)== 0:
        return s
    return s[-1]+ reverse_string(s[:-1])
print(reverse_string("SoeWin"))
  

# checker if name is palindrome or not

def is_palindrone(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return "it's not a plaindrone"
    return is_palindrone(s[1:-1])
print(is_palindrone("naran"))


# Print Fibonacci Series up to n terms using recursionand loop 

def fib(n):
    if n==0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fibonaacci_series(n):
    for i in range(n):
        print(fib(i), end="    ")

fibonaacci_series(12)
