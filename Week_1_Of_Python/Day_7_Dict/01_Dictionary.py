# Python Dictionaries

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dict = {"name":"Soe Win", "Age":18,"year": 2007, "Male":True}
print(Dict)
print(type(Dict))


        # Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates**

Dict = {"name":"Soe Win",
         "Age":18,
         "year": 2007, 
         "Male":True
}
print(Dict["name"])


# Dictionary Length

# Using len() function
print(len(Dict))


# The dict() Constructor

soe = dict(name = "soe win", age = 17 , male = True, year = 2007)
print(soe)#{'name': 'soe win', 'age': 17, 'male': True, 'year': 2007}