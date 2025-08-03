# Python - List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []
for i in fruits:
    if "a" in i:
        new_list.append(i)

print(new_list)# ["apple", "banana","mango"]


        # We can write this code in short
        # it is caleed list comprehension

# The Syntax
 # newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new =[i for i in fruits if 'e'in i]
print(new)#['apple', 'cherry']

another = [i for i in fruits if i != "apple"] #this will check aall the items and add only item that is not an apple because !=
print(another)#['banana', 'cherry', 'kiwi', 'mango']

a = [i for i in fruits]
print(a)#['apple', 'banana', 'cherry', 'kiwi', 'mango']




#           Iterable
# The iterable can be any iterable object, like a list, tuple, set etc

b = [i for i in range(12)]
print(b)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(type(b))


# for i in range(100):
#     print(i)# zero to 99 vertically
        
#         # Or
# [print(i) for i in range(100)]

# We can add cnodition in loopin a list

one = [i for i in range(100) if i <10]
print(one)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = [i for i in range(15) if i <= 10]
print(a)
print(type(a))

#       Expression
# Set the values in the new list to upper case:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
hi = [i.upper() for i in fruits]
print(hi)#['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


# To Set all values in the new list to 'hello':


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new =["Soe Win" for i in fruits]
print(new) #['Soe Win', 'Soe Win', 'Soe Win', 'Soe Win', 'Soe Win']


# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
fruits = ["apple","banana", "cherry", "kiwi", "mango"]
# "Return the item if it is not banana, if it is banana return orange".
nelists = [i if i != "bimal" else "piapple" for i in fruits]
print(nelists)

