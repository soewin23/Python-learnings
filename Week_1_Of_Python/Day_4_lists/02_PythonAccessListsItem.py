#               Access list items

# neagative indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # to acces the last items of a list

print(thislist[-2]) # to access the second last items in a list


# Range of indexing

list =["the", "name", "of", "the","company", "is", "Sion"]
newlist = list[2:5]  #of the company 5 is not included "is"
print(newlist)


this = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
l = this[:4]# it will start from zero to 3
print(l)# apple banana cherry oringe

m = this[2:]#it will start from two to end
print(m)# "cherry", "orange", "kiwi", "melon", "mango"


#        Range of nagative indexing 
comp =["the", "name", "of", "orange", "kiwi",  "the","company", "is", "Sion","melon", "mango"]
new = comp[-4:-1] #is sion meoln
print(new)




#       to check litem exit or not

comp =["the", "name", "of", "orange", "kiwi",  "the","company", "is", "Sion","melon", "mango"]
if "Sion"in comp:
    print("Yes, Sion is in the list")