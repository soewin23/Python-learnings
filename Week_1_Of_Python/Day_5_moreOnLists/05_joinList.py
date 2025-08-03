# Python - Join Lists

# using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
l3 = list1 + list2
print(l3)



# using for loop

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for i in list1:
    list2.append(i)

print(list2)
# using extend()
# can use the extend() method, where the purpose is to add elements from one list to another list

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
