"""Tuple Methods"""
# There are two methods in python --- count(), index()


"""Count()"""

# Returns the number of times a specified value occurs in a tuple

truple =("apple","bluebery","orange", "banana", "cherry")
count =truple.count("apple")
print(count)#1 'cuz there is only one apple in tuple

# index()	
# Searches the tuple for a specified value and returns the position of where it was found
print(truple.index("banana"))#3 'cuz there is a banana in third position.Count  like 0123
