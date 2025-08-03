# Function

# A function is a block of code which only runs whenit is called
def Greeding():
    print(f"Hello from Function")

#       Calling a Function
# To call a function, use the function name followed by parenthesis
# Greeding()

"""ARGUMENTS"""

# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a 

def name(name):
    print(f"Your name is {name}")
# name("kyaw")
# name("Zin")
# name("Htet")



# Number of Arguments

def info(name, age):
    print(f'Your name is {name}. You are {age} years old.')

info("Mr.Beast",100)

# Arbitrary Arguments, *args
"""If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition."""

# If the number of arguments is unknown, add a * before the parameter name:

# This way the function will receive a tuple of arguments, and can access the items accordingly:

def I(*kids):
    print(f'kids are{kids}'+ kids[2])
I("soe","Win","Arno")

#           """Keyword argument"""
#  You can also send arguments with the key = value syntax.
def infor(name,age, gender):
     print(f"your name is {name}")  
     print(f"YOu are {age} years old")     
     print(f"You are {gender}")

infor(name="SoeWin", age=18, gender="Male")

print("-----")
# Arbitary keyword Argymnet **
"""If you do not know how many keyword arguments that will be passed into your function, add two asterisk:
** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:"""

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def n(**keys):
    print(keys)
n(hi = "hi",ad= 12)


"""Default Parameter Value"""
# f we call the function without argument, it uses the default value:
def country(country="America"):
    print(f"You want to go {country}")
country("England")
country("Swedan")
country()
country("Brazil")
print("____")

# Passing a List/dict/tuple as an Argument

def loop(item):
    for i in item:
        print(i)
fruit = ['apple','banana','cucumber','mango']
dict = {"greeding":"hi",}
tuple = ("hi",18)
list = [1,2,3,4,5]

loop(fruit)
loop (dict)
loop(tuple)
loop(list)
print("----")

# Return Values

"""To let a function return a value, use the return statement:"""
def function(a):
    return a +1
print(function(19))# here print is necessary

print("----")

# The pass Statement
# for some reason function can't be empty 
# for that we use pass statement

def a():
    pass


""" Positional-Only Arguments"""
# When a function uses positional-only arguments, it means:

# 👉 You must pass the values by position, not by using the name of the argument.
def positional(x , y, /):
    return x + y
print(positional(1,12))# we can only add positional argument not keyword argument
print("-------")


# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def keyonly(*, a):
    return a *3
print(keyonly(a= 12)) #we can only add argument argument not keyword positional
print("-------")



"""To combine Positional_ONly and Keyword_only argument"""

# Any argument before the / , are positional-only,
# and any argument after the *, are keyword-only.
  

# def Pos_Key(a,b,c,/,*,d,e,f):
#     return a,b,c,d,e,f
# print(Pos_Key(1,2,3,d=4,e=5,f=6))

def A(a,b,c,/,*,d,e,f):
    return (a+b+c)*(d+e+f)
print(A(20,69,90,d=56,e=79,f=50))
print("---------")

 # Recursion
"""Calling a function from itself"""
#for recursion limit
def recursion(i):
    if i > 0:
        result = i + recursion(i -1) #--> recursion(i-1)== recursion(2)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example of Result ")
recursion(12)
