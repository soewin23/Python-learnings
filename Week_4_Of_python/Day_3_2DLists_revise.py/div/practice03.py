

numbers = [
    [2, 3],
    [4, 5]
]
# Create a new matrix with each number squared.
square = [[num ** 2 for num in row]for row in numbers]
print(square)

matrix = [
    [3, 4],
    [7, 8]
]
# Expected: [[1, 0], [1, 0]]

new_matix = [[0 if num &2 ==0 else 1 for num in row]for row in matrix]
print(new_matix)
