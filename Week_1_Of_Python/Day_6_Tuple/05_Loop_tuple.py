# Loop Through a Tuple


thistuple = ("apple", "banana", "cherry")
print(thistuple)#('apple', 'banana', 'cherry')
# for i in thistuple:
#     print(i)
"""    apple
banana
cherry"""


        # Loop through index Number
# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

truple =("apple","bluebery","orange", "banana", "cherry")
for i in range(len(truple)):
    print(truple[i])


# Looping with "**while"

truple =("hiiiii","apple","bluebery","orange", "banana", "cherry")
i = 0
while i < len(truple):
    print(truple[i])
    i += 1
"""    apple
bluebery
orange
banana
cherry"""