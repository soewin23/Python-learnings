# Python Loops

# The while Loop

""""With the while loop we can execute a set of statements as long as a condition is true."""
"""A = 1
while A < 13:
    print(A)
    A += 1"""


# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

"""b = 0
while b < 10:# if the conditiona is true
    print(b) #it will print b
    if b == 5: # this check the b is equal to 5 if not print(b) if yes loop break
        break
    b += 1# only works when that if condition is false
"""
"""0
1
2
3
4
5"""

# The continue statement


# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 5:
    i += 1
    if i == 3:# this check the i is equal to 3 if not print(i) if yes then skip 3 and countinue loop 
        continue # it will dkip 3 and countinue the loop
    print(i)

# The else Statement

# With the else statement we can run a block of code once when the condition no longer is true:
i = 0 
while i <=5 :
    print(i)
    i += 1
else:
    print(f"i is no longer less than 6")

