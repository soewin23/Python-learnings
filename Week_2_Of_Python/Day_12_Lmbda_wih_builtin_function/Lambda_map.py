# Use with Built-in Functions ✅

# map()<--Transform each item	

# 1. map() — Apply a function to every item in an iterable

"""Takes a function and an iterable (like a list).
Returns a new iterable where the function is applied to each element.
"""
lis = [1,2,3,4,5]
A =[]
# Using lamba to square each number
square = list(map(lambda x: x ** 2,lis))
print(square)
"""Using for loop"""
for i in lis:
    A.append(i **2)
print(A)
print("---")

b = [1,2,3,4,5,6,7,8,9]
squar = tuple(map(lambda i: i**2,b))
print(squar)