# The try let you to test a block of code for error.

# THe except let you to handle the error

# The else lets you excute code when there is no error

# the finally block lets you excute, regardless of the result of the try- and except blocks



# Exception Handling
 
# he try block will generate an exception, because x is not defined:



try:
    # risky code
    print("x")
except:
    # what to do if error happens
    print("An exception occoured")


try:
    print("a")# if this is an error 
    #without the try block program will crash and raises error

except:# only excute wheen try block occoured an error
    print("An exception occoured")

"""Example"""

# try:
#     number = int(input("Enter a number")) # if error occours
#     print("You entered", number)
# except:#it will come here without showing error in compilter
#     print("This is not a digit")



# More example

try:
    number = int(input("Enter a number : "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
except:
    print("Opps! That didn't work. ")


