# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# If we want to change the value of tuple,
# we have to change it into list**
x = ("apple", "banana", "cherry")
x = list(x)
print(type(x))

#   And then We can chnge and add the value of Tuple

A = ("apple", "banana", "cherry")
B = list(A)
B.remove("apple")
print(B)#['banana', 'cherry']


 # to replace items in a tuple

A = ("apple", "banana", "cherry")
C = list(A) # change it into a list first
C[0] = "peach" # apple changes into peach
A = tuple(C) # After changine the ilems in list , and then we change it back to Tuple
print(A)#['peach', 'banana', 'cherry']
print(type(A))#<class 'tuple'>


# # To delete the tuple Completely
# # We use del keyword
# a = ("apple", "banana", "cherry")
# del A
# print(A)# #this will raise an error because the tuple no longer exists

# Add tuple to  a tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange","pinapple")
thistuple += y

print(thistuple)



