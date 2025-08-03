# 2d list is a  list that is made up of many list

fruits = [ "apple","oranges","banan","coconut"]
veg = ["celery","carrot","paotaoes","tomato"]#!D list
meats = ["chicken","fish","turkey"]

groceries = [fruits, veg, meats]

# to access the 2d list individually
print(groceries[0])# entire fruits row list
print(groceries[0][0])#only apple like row is zero and coulmn is o
print(groceries[1][0])#only celery like row is one and coulmn is o

##using loop to iterelate
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

