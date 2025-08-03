# Intersection
# This will make a new set, in that set all same item in both set 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)#{'apple'}

# we can also use intersection() with list and set to get the same output
set5 = [1,2,3,"apple"]
set6 = set1.intersection(set5)
print(set6)#{'apple'}



# We can also use & operator to intersect both set

set4 = set1 & set2
print(set4)#{'apple'}


# The values True and 1 are considered the same value. The same goes for False and 0.


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)#{False, 1, 'apple'}


