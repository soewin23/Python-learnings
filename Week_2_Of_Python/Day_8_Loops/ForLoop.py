# Python For Loops

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruite = ["apple","banana","cream","doll"]
for i in fruite:
    print(i)
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

# Looping Through a String


# Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
    print(x)
"""b
a
n
a
n
a"""
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")


# break statement in for

# With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i != "apple":
        break
    print(i)
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")



# continue Statement in for
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruit = ["apple", "banana", "mango"]
for i in fruit:
    if i == "banana":
        continue
    print(i)
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
# The range()   function 


# The Range function

# We use to loop through a set of code a specified number of times, we can use the range() function,
for i in range(4):
    print(i)
"""0
1
2"""
print("x---x----x----x-----x-----x----x----x----x-----x-----")

# We can use range to set the starting point and ending point

for i in range(12,15):
    print(i)
print("x---x----x----x-----x-----x----x----x----x-----x-----")


# and also we can add increment using the range function

for i in range(0,10,2):# start, end, incerment
    print(i)
"""0
2
4
6
8"""
print("x---x----x----x-----x-----x----x----x----x-----x-----")


# Else in For Loop

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for i in range(6):
    print(i)
else:
    print("Finally finished")
    print("x---x----x----x-----x-----x----x----x----x-----x-----")

for i in range(6):
    if i == 3:
        break
    print(i)
else:
    print("Loop over!")



"""Nested Loops"""
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for i in adj:
    for x in fruits:
        print(i,x)
        """red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry"""

# The pass Statement
# if we use for loop for soem reason and we don't want to store any value in it, we use pass statement to avoid getting errors
"""it will not print anythind"""
for i in [0,1,2,3,4,5,6,7,8,9]:
    pass
