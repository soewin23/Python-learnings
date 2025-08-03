# list methods


# append()	Adds an element at the end of the list
list = ["apple", "banana", "cherry", "piapple"]
list.append("bimalKtd")
print(list)

# copy()	Returns a copy of the list
new_lilst = list.copy()
print(new_lilst)
# count()	Returns the number of elements with the specified value
a = new_lilst.count("apple")
print(a)
# extend()	Add the elements of a list (or any iterable), to the end of the current list
b = [1,2,3,45,4,4,5]
list.extend(b)
print(list)
# index()	Returns the index of the first element with the specified value
listaa = ["apple", "banana", "cherry", "piapple"]

ass = listaa.index("piapple")
print(ass)
# insert()	Adds an element at the specified position
listz = ["apple", "banana", "cherry", "piapple"]
listz.insert(2,"soe")
print(listz)

# pop()	Removes the element at the specified position
listz.pop(0)
print(listz)
# remove()	Removes the item with the specified value
listz.remove("soe")
print(listz)
# reverse()	Reverses the order of the list
listz.reverse()
print(listz)
# sort()	Sorts the list
listz.sort()
print(listz)
listz.sort(reverse = True)
print(listz)
# clear()	Removes all the elements from the list
listz.clear()
print(listz)
