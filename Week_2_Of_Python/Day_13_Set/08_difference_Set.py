"""**crucial very you run the code the outpit will be unordered that is the behavior"""


## different() method wiil return a new set that will contain
# only items from the first set tatare not present in other set
# 💡 It does NOT change the original set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google",1,2,3, "microsoft", "apple"}

set3 = set1.difference(set2)# it prints only the first set that are not in a second set
print(set3)#{'cherry', 'banana'}


list3 = [1,2,3,4,5,6,7,"google"]
set5 = set2.difference(list3)
print(set5)# this method work with different datatype




"other Operator to do the same thig"# this Operator doesn't work for different datatype

set1 = {"apple", "banana","ice_cream", "cherry"}
set2 = {"google", "microsoft", "apple"}

set4 = set1 - set2
print(set4)#{'banana', 'cherry', 'ice_cream'}



A = {1,2,3,4}
B = {3,1,4,5}
A.difference_update(B)
print(A)#{1, 2}


# key different between difference()& difference_update
#                     difference()             |   difference_update()
# Returns new set?	    ✅ Yes                |     	❌ No
# Modifies original?	❌ No                 |     	✅ Yes
# Use case	When you want to keep original | When you want to update in place

