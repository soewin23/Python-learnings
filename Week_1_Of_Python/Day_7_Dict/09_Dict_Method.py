            # Dictionary Methods

# Python has a set of built-in methods that you can use on dictionaries.

# Clear()  method
"""Removes all the elements from the dictionary"""
Clear = {"name":"aaaa", "age ": 14}
Clear.clear()
print(Clear)#{}
print("-------")


# copy() method
"""Returns a copy of the dictionary"""
About_Me = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
A = About_Me.copy()
print(A)
# {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
print("-------")


# fromkeys()
"""	Returns a dictionary with the specified keys and value"""

e = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
E= e.fromkeys("names",'Sion')#*** we need to store in separrate variable 'cuz dict can't change the original ualues
print(E)#{'n': 'Sion', 'a': 'Sion', 'm': 'Sion', 'e': 'Sion', 's': 'Sion'}

print('-------')

# get()	
"""Returns the value of the specified key"""
e = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
A = e.get("name")
print(A)#xxxx
print('-------')

# items()
"""Returns a list containing a tuple for each key value pair"""

e = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
V = e.items()
print(V)#dict_items([('name', 'xxxx'), ('age', 1101), ('year', 21007), ('Gender', 'Male'), ('Student', True)])
print("-------")

# keys()
"""Returns a list containing the dictionary's keys"""
e = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
B= e.keys()
print(B)#dict_keys(['name', 'age', 'year', 'Gender', 'Student'])
print("------")

# pop()
"""Removes the element with the specified key and returns its value."""
e = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
Q = e.pop("name")
print(Q)#xxxx
print("-------")

# popitem()
"""Removes the last inserted key-value pair and returns its value. And become typle"""
e = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
F = e.popitem()
print(F)#('Student', True)
print(type(F))#<class 'tuple'>
print("-------")


# setdefault()
"""Returns the value of the specified key.
If the key does not exist: insert the key, with the specified value"""
e = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
r= e.setdefault("A", "alpha") # A doesn;t exitst so this method add into dict
print(r)#alpha
print('------')


# update()	
"""Updates the dictionary with the specified key-value pairs"""
e = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
e.update({"Hi":"Greeding"})
print(e)#{'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True, 'Hi': 'Greeding'}
print('------')


# values()
"''Returns a list of all the values in the dictionary"""
e = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
k = e.values()
print(k)#dict_values(['xxxx', 1101, 21007, 'Male', True])
print('---xxxxxx-------xxxxxx-------xxxxxx-------xxxxxx-------xxxxxx-------xxxxxx-------xxxxxx---')