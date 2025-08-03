
# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("apple")
print(thisset)


# To remove a random item we use pop() method

A= {"a","b","c",'d'}
A.pop()
print(A)

# The clear() method empties the set:

C = {"a","b","c",'d'}
C.clear()
print(C)#set()


# The del keyword will delete the set completely:

this= {"apple", "banana", "cherry"}

del this

print(this)# raises an error
