#       Unpacking Tuple
#unpacking means extracting value in the tuple and assign then to a variable

a = ("apple","Tree","ball","cow","dog","ear")# This is called a packing of tuple

red, green, blue, white,yellow, *skin = a#unpacking of tuple & assigning tuple into the variable

"""Note---> the number of items in a tuple must be the same"""
print(red)
print(green)
print(blue)
print(white)
print(yellow)
print(skin)
print(type(skin))# using asterik will convert a tuple to list**

# use of Asterisk

# Used when the number of variables are less than the values of a tuple

a = ("apple","Tree","ball","cow","dog","ear")

hi,*Arno,b = a
print(hi)#apple
print(Arno)#['Tree', 'ball', 'cow', 'dog', 'ear']
print(b)
