# Set
# Sets are used to store multiple items in a single variable


# Sets are written with curly brackets.
myset = {"apple"," banana", "ice cream", "cheese"}# unordered unchangeable and not allow to duplicate
print(myset)
print(type(myset))

# Set are one of four built in data tupe in python used to store collectioins of DeprecationWarning
# theother 3 are list, Tuple, and Dictionary

"""Duplicate not allowed"""

# Sets cannot have two items with the same value.
S = {"a","b","c","a","a","a"}
print(S)

#***** the value of Ture and 1 are consider same in Set
Set= { 1, True}
print(Set)#{1}
#***** the value of False and 0 are consider same in Set
q = {0, False}
print(q)#{0}
w = {True,True}
print(w)#{True}

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print(len(thisset))



"""The Set constructor """
theset = set(("a","b","c")) ## note the double round-brackets
print(theset)
print(type(theset))


