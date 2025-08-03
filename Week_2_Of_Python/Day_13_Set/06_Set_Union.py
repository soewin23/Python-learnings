"""There are several ways to join two or more set in python"""

# union() or update === same to join


# Union

# The union() method returns a new set with all items from both sets

set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)#{'b', 'c', 1, 2, 3, 'a'}

# Or 
# the operator for  union set"|"

set4 = set1 |set2
print(set4)#{'b', 1, 2, 3, 'c', 'a'}


# Join multiple set using union()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
new  = set1.union(set2,set3,set4)
print(new)

# {1, 2, 'a', 'b',3, 'Elena', 'cherry', 'bananas', 'John', 'c', 'apple'}

# Or 
# the operator for  union set"|"

new1 = set1 | set2 | set3 | set4
print(new1)
# {1, 2, 'a', 'b',3, 'Elena', 'cherry', 'bananas', 'John', 'c', 'apple'}



# JOin  a set and tuple Using union()

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)#{1, 2, 3, 'a', 'c', 'b'}



######Note we can't use | to join dfferent type of  data set



# Update method is also like a union but it changes the original set 
# but union method doesn't, it made a new set 


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
