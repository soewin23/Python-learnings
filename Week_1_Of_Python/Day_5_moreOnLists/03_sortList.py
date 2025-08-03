# Python - Sort Lists

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:


thislist = ["orange", "Apple","bin","mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #it will print alphabitically

Numeric = [100, 1,12,233,222,464,50, 65, 82, 23]
Numeric.sort()
print(Numeric)

# Sort Descending aka backwards
# To sort descending, use the keyword argument reverse = True:

Num = [100, 1,12,233,222,464,50, 65, 82, 23]
Num.sort(reverse= True)
print(Num)#[464, 233, 222, 100, 82, 65, 50, 23, 12, 1]

# Case Insensitive Sort

thislist = ["banana", "O]orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)#['Kiwi', 'Orange', 'banana', 'cherry']

t = ["banana", "orange", "kiwi", "cherry"]
t.reverse()
print(t)#['cherry', 'kiwi', 'orange', 'banana']

