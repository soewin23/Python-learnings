# 🐍 Python Lambda Functions

# A lambda is a small, anonymous function (function without a name).

# It's used when you need a quick function for a short task.

# Instead of using def, you use the lambda keyword

add = lambda a, b: a+b
print(add(3,5))#8

# ✅ 3. Same with def:
def add( a,b):
    return a +b
# add = lambda a, b: a+b 
"""These are like the same"""
print(add(3,5))#8
"""Or use in one line"""
print((lambda a,b:a*b)(2,3))#6