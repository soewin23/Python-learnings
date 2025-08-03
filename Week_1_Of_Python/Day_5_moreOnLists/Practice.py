# 1️⃣ Create a list of 5 integers.

# Sort the list in ascending order.

# Print the sorted list.

list = [1,2,4,6,75,0,5]
list.sort()
print(list)

# 2️⃣ Given colors = ["red", "green", "blue"]

# Add "yellow" to the list using append().

# Insert "black" at index 1.

# Print the final list.

colors = ["red", "green", "blue"]
colors.append("yellow")
colors.insert(1,"black")
print(colors)

# 3️⃣ Loop through the list names = ["Alice", "Bob", "Charlie"]

# Print each name with a greeting: "Hello, <name>!"
names = ["Alice", "Bob", "Charlie"]
for i in names:
    print("hello,",i)

i = 0
while i < len(names):
    print("hello, ",names[i])
    i += 1

#     4️⃣ Use list comprehension to create a list of squares of numbers from 1 to 10.

# Example: [1, 4, 9, 16, 25, ...]

suquare = [i**2 for i in range(1,10)]
print(suquare)

# 5️⃣ You have a list animals = ["cat", "dog", "rabbit", "cat"]

# Count how many times "cat" appears.

# Remove "dog" from the list.

# Make a copy of the list.

# Clear the original list and print both lists.

animals = ["cat", "dog", "rabbit", "cat"]
a=animals.count("cat")
print(a)
animals.remove("dog")
print(animals)
a= animals.copy()
print(a)
animals.clear()
print(animals)


# 6️⃣ You have two lists:

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Join them into one list using +.

# Join them using a loop (by appending each element).


list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2
print(new_list)
for i in list1:
    list1.append(list2)

print(list1)

#.. Given marks = [75, 60, 89, 45, 92]

# Sort in descending order.

# Find the highest and lowest mark using list methods.

marks = [75, 60, 89, 45, 92]
marks.sort(reverse=True)
print("Sesending order",marks)
hightest = max(marks)
lowest = min(marks)
print(hightest)
print(lowest)

