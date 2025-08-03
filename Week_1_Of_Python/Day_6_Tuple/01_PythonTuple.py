# Tuples are used to store multiple items in a single variable.

example = ("a","b","c","d","e","f")
print(type(example))
print(example)

#Lenght of tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thisnottuple = ("apple")
print(type(thisnottuple))

# The tuple() Constructor
thisistuple = tuple(("apple","banan","cherry"))# note the double round-brackets
print(thisistuple)
print(type(thisistuple))


        # we can add different data type in tuple 
Datas = ("Strings",12, True, 12j)
Datas[1]
print(type(Datas[3]))
print(Datas)
