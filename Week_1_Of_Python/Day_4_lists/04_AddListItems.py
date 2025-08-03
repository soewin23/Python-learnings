#       Python - Add List Items

# To add an item to the end of the list, use the append() method:

thislist = ["cherry", "orange", "kiwi", "mango"]
thislist.append("strawbary")
print(thislist)#['cherry', 'orange', 'kiwi', 'mango', 'strawbary']



#            Insert Items

# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:
new_list = ['cherry', 'orange', 'kiwi', 'mango', 'strawbary']
new_list.insert(2,"banana")
print(new_list)#['cherry', 'orange', 'banana', 'kiwi', 'mango', 'strawbary']



#           Extend List

# To append elements from another list 
# to the current list, use the extend() method.

a_list = ["Soe","Win", "Sion", "Harry","bimal"]
c_list = ["Arno","Christ","William","David"]
a_list.extend(c_list)
print(a_list)#['Soe', 'Win', 'Sion', 'Harry', 'bimal', 'Arno', 'Christ', 'William', 'David']