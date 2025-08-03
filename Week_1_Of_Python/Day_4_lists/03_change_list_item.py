#           Python - Change List Items


# To change the value of a specific item, refer to the index number:

list = ["my", "name","is","Soe","Win"]
list[1]= "naam"
print(list)# ['my', 'naam', 'is', 'Soe', 'Win']
list[2] = "are"
print(list)# ['my', 'naam', 'are', 'Soe', 'Win']


        # Changing a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[0:4]= "The","list","of","fruits"
print(thislist)     #['The', 'list', 'of', 'fruits', 'kiwi', 'mango']

thislist[0:4]= "hi"
print(thislist)#['h', 'i', 'kiwi', 'mango']


#                    Insert Items

# To insert a new list item, without replacing any of the existing 
# values, we can use the insert() method.

list = ['this','is', 'me']
list.insert(3,"SoeWin")
print(list)#['this', 'is', 'me', 'SoeWin']

