# Loop Through a List
# We can loop through the itlems by using fo loop:

list = ["apple", "banana", "cherry", "piapple"]
for i in list:
    print(i)
    # Output
""" apple
    banana
    cherry
    piapple"""

# Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.
list = ["apple", "banana", "cherry", "piapple", "mago"]
for i in range(len(list)):
    print(i) #01234



# Using while loops

# u can loop through the list items by using a while loop
# .
newlist = ["apple", "banana", "cherry", "piapple", "mago"]
i = 0
while i < len(newlist):
    print(newlist[i])
    i += 1
# apple
# banana
# cherry
# piapple
# mago


# Looping Using List Comprehension

# List Comprehension offers the shortest syntax for looping through lists:

new = ["apple", "banana", "cherry", "piapple", "mago"]
[print(i) for i in new]
