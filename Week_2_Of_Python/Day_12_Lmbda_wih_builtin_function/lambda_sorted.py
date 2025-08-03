# sorted()<--Custom sort logic	

# sorted() returns a new sorted list from the items in an iterable.
# You can use a lambda to customize how it sorts.


# sorted is use to sorted items in a list (or any iterable)
# it give new sorted list and doesn;t change the original one

number = [1,4,2,6,3,63,0,5,7,9]
print(sorted(number))


# sorted in reverse ( largest to smallest) 
print(sorted(number, reverse=True))


""" Sorting with lambda using the key= argument"""


students = [("Aung", 14), ("Mya", 13), ("Hla", 15)]
print(sorted(students,key=lambda i:i[1]))

# 🧪 Let’s try sorting by the first number instead
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_by_first_item_in_listOftuple = sorted(pairs,key= lambda i: i[0])
print(sorted_by_first_item_in_listOftuple)#[(1, 3), (2, 2), (4, 1)]


sorted_by_second_item_in_listOftuple = sorted(pairs, key=lambda i: i[1])
print(sorted_by_second_item_in_listOftuple)