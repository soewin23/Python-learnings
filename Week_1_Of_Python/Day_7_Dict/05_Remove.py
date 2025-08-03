# Removing Items



    # Using the pop()
thisdict = {"brand": "Ford","model": "Mustang","year": 1962}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1962}
thisdict.pop("year")#**we need at least one argument in pop()
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang'}
print("........")



    #Using the popitem()
Me = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
print(Me)
# {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
Me.popitem()#**Removes the last item in Dict
print(Me)
# {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
print("........")



#  del (keyword)to delete items in Dict
Me = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
print(Me)
# {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
del Me["year"] #** it will delete the "year" key value pair
print(Me)
# {'name': 'xxxx', 'age': 1101, 'Gender': 'Male', 'Student': True}
print("........")

#   clear()method for clearing the entire dict items
Me = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
print(Me)
# {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
Me.clear()
# {}
print(Me)