# we can't access the set ny referring to an index or key.


# But we can uloop through the set items using a for loop


thisset = {"apple", "banana", "cherry"}
for i in thisset:
    print(i)
"""banana
cherry
apple"""

# And we can ask if a specified 
# value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
print("banana"in thisset)# True

# Check if "banana" is NOT present in the set:
print("banana" not in thisset)#False