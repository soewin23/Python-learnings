# Access Tuple Items

# We can access tuple items by referring to the index number, inside square brackets:

this = ("apple","banana", "cherry")
print(this[0])#apple

# Negative indexing
print(this[-1])#cherry
this = ("apple","banana", "cherry")
print(this[-2])#banana



#    WE can also specify the range of a tuple.
#By specifying the starting & end of a tuple

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
new = thistuple[1:5]
print(new)#('banana', 'cherry', 'orange', 'kiwi')

# if we do not add a beginning index it'll start from 0
another = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(another[:4])#('apple', 'banana', 'cherry', 'orange')

# same way for endings
print(another[3:])#('orange', 'kiwi', 'melon', 'mango')


# Range of Negative Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-3:-1])#('kiwi', 'melon')



# Check if Item Exists in tuple
A = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "banana" in A:
    print("Yes, banana exists in this Tuple")

