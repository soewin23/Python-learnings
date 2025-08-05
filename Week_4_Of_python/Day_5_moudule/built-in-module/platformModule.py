import platform
x = platform.system()# To know the system of the devivce
print(x)
y = platform.version()
print(y)

# Using the dir() Function

# There is a built-in function to list all the function names 
# (or variable names) in a module. The dir() function:

z = dir(platform)
print(z)