
# 📝 Basic Tuple Operations
# 1️⃣ Create a tuple colors = ("red", "green", "blue")

# Print the second color.

colors = ("red", "green", "blue")
print(colors[1])#green

# 2️⃣ Create a tuple of 3 numbers (10, 20, 30)

# Access and print the first and last item.
A =(10, 20, 30)
print(A[0])#10
print(A[-1])#30

# 📝 Tuple Unpacking
# 3️⃣ Unpack the tuple (5, 10, 15) into variables a, b, c

# Print the value of b.
f = (5, 10, 15)
a,b,c = f
print(b)#10

# 📝 Joining Tuples
# 4️⃣ You have:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# Join them into one tuple and print it
print(tuple1 + tuple2)#(1, 2, 3, 4, 5, 6)

# 📝 Looping through Tuples
# 5️⃣ Loop through this tuple:
animals = ("cat", "dog", "rabbit")
# Print each animal on a new line.
for i in range(len(animals)):
    print(animals[i])
# cat
# dog
# rabbit
"""Or"""
i =0 
while i < len(animals):
    print(animals[i])
    i+= 1


# 📝 Tuple Methods
# 6️⃣ You have:

numbers = (1, 2, 3, 2, 4, 2)
# Find how many times 2 appears in the tuple.

# Find the index of first occurrence of 4.
print(numbers.count(2))#3
print(numbers.index(4))#4


# 📝 Tuple with Single Item
# 7️⃣ Create a tuple with only one item "apple" and print its type.
one = ("hi",)
print(type(one))