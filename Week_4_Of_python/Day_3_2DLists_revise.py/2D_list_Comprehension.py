# A 2D list comprehension is a nested list comprehension

# 📌 Basic Syntax:

# mew_matrix = [[expression for item in row]for row in matix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

doubled = [[num *2 for num in row] for row in matrix]
print(doubled)


new_matrix = []
for row in matrix:
    new_row = []
    for x in row:
        new_row.append(x * 2)
    new_matrix.append(new_row)

new_matrix = [[num*2 for num in row]for row in matrix]
print(new_matrix)