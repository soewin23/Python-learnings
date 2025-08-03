# Copy Lists

# Use the copy() method

a_list = ["Soe","Win", "Sion", "Harry","bimal"]
b_list = a_list.copy()
if a_list == b_list:
    print("both are the same list")# this is true
else:
    print("they are not")

# Or 
A_list = ["Soe","Win", "Sion", "Harry","bimal"]
llist = list(A_list)
if A_list == llist:
    print("both are the same list")# this is true
else:
    print("they are not")

# slice Operator

# You can also make a copy of a list by using the : (slice) operator.
A_list = ["Soe","Win", "Sion", "Harry","bimal"]
my_list = A_list[:]
print(my_list)


A_list = ["Soe","Win", "Sion", "Harry","bimal" ]
my_list = A_list[1:4]
print(my_list)

