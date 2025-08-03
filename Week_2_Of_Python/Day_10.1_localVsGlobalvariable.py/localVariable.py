# 🌍 Global vs Local Variables in Python

# Local Variables
# Defined inside a function.

# Only accessible within that function.

# Created when function starts, destroyed when function ends.
"""Example """
def greet():
    message = "hello"#<--- local variable
    print(message)
greet()
# print(message)# Error will occour