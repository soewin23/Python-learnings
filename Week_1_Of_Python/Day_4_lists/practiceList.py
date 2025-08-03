# 1️⃣ Create a list named colors with values ["red", "blue", "green"].

# Print the second color.

colors =[ "red","blue", "green"]
newcolors =colors[1]
print(newcolors)#blue

# 2️⃣ You have a list numbers = [10, 20, 30, 40]

# Change the third item to 99.

# Print the updated list.

numbers = [10,20,30,40]
numbers[2]= 99
print(numbers)#[10, 20, 99, 40]

# 3️⃣ Start with this list: fruits = ["apple", "banana"]

# Add "orange" at the end.

# Add "grape" at index 1.

# Print the list.

fruits = ["apple", "banana"]
fruits.append("orange")
fruits.insert(1,"grape")#['apple', 'grape', 'banana', 'orange']
print(fruits)


# 4️⃣ You have: items = ["pen", "pencil", "eraser", "sharpener"]

# Remove "eraser" from the list.

# Print the list.

items = ["pen", "pencil", "eraser", "sharpener"]
items.pop(2)
print(items)#['pen', 'pencil', 'sharpener']


# 5️⃣ marks = [75, 60, 90]

# If the first mark is greater than 70, print "Passed" else "Failed"

# (Use list index and if-else

marks = [75, 60, 90]
if marks[0] > 70:
    print("pass")
else:
    print("Failed")

# 6️⃣ You have nums = [5, 8, 12]

# Multiply the first item with the second 
#     item and print the result.

nums = [5, 8, 12]
new = nums[0]* nums[1]
print(new)

# 7️⃣ Ask the user to input 3 favorite movies (one by one) and store them in a list.

# Print the second movie.

first_movie = input("Enter a movie name: ")
second_movie = input("Enter another name: ")
third_movie = input("Enter another name: ")

movieList = [first_movie, second_movie,third_movie]
a = movieList[1]
print(movieList)
print(a)