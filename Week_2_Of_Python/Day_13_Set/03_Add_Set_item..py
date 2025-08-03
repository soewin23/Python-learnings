# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)#{'cherry', 'apple', 'orange', 'banana'}

"""To add items from another set into the current set, use the update() method."""
fruit = {"apple", "banana", "cherry"}
fruit_2= {"pineapple", "mango", "papaya"}
fruit.update(fruit_2)
print(fruit)#{'papaya', 'banana', 'cherry', 'apple', 'mango', 'pineapple'}


# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.)


fruit = {"apple", "banana", "cherry"}
fruit_2= ["pineapple", "mango", "papaya"]
fruit.update(fruit_2)
print(fruit)