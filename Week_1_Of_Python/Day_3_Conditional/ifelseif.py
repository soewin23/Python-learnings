# Python Conditions and If statements

# An "if statement" is written by using the if keyword.

# Example of if statement

"""a = 33
b = 200
if b > a:
  print("b is greater than a")
"""
            # Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# Example


#                   Else
# The else keyword catches anything which isn't
# caught by the preceding conditions.


print("Grading system")

m = int(input("Enter your makrs: "))
if m > 39 and m== 59:
    print("Your grade is C")
elif m > 59:
    print("your grade is B")
elif m >79:
    print("your grade is A")
elif m > 100:
    print("Error marks")
else:
    print("Fail")







age = int(input("Enter your age "))
if age >= 18:
    print("You can dive a car")
else:
    print("You can't drive a car")