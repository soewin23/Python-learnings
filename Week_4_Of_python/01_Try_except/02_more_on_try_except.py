# Many Exceptions
# we can define as many exppection blocks as we want

try:
    print("x")
except NameError:
    print("Variable x is not defined ") 
except:
    print("Something else went wrong")
    

    # example

try:
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    print("Result", x +y)
except:
    print("Please enter only numbers!")

#Catching Specific Errors
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError: #if you try to divide with Zero it'll run this
    print("YOu can't divide with zero !")
except ValueError:# if I run other than integer it will run this block
    print("Thatls not a valid number")



    