# Python-Remove Specified Item


# The remove() method removes the specified item.

list = ["apple", "banana", "cherry"]
list.remove("banana")
print(list)#['apple', 'cherry']

# Remove Specified Index


# The pop() method removes the specified index.

lists = ["apple", "banana", "cherry"]
lists.pop(0)
print(lists)#['banana', 'cherry']

listss = ["apple", "banana", "cherry"]
listss.pop()# thsi will remove the last item
print(listss)#['apple', 'banana']



# The DEL keyword also removes the specified index:

thislist = ["cherry", "orange", "kiwi", "mango"]
del thislist[-1]# delete last item
print(thislist)#['cherry', 'orange', 'kiwi']


thislists = ["apple", "banana", "cherry"]
del thislists #it delete entire list

# #       clear the List

# The clear() method empties the list.

# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)# []

