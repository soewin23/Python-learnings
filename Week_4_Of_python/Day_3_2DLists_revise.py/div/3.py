

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10,11,12]
]

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] %3 ==0:
            matrix[row][column] = "Div/3"
        else:
            matrix[row][column] = "NotDiv/3"
for row in matrix:
    print(row)