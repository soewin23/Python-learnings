import mymodule


# The module can contain functions, as already described, but also variables of all types 
# (arrays, dictionaries, objects etc):


a = mymodule.person1["name"]
print(a)
b = mymodule.person1["age"]
print(b)
c = mymodule.person1["country"]

"""Renaming the module"""
# y using the as keyword:


import mymodule as B
a = B.person1["active"]
print(a)
