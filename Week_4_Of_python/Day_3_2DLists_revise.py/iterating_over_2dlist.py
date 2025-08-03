
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7,8,9]
]

for row in matrix: # outer loop -> rows
    for element in row: #inner loop -> colums (elemen)
        print(element, end=" ")
    print()

    #   Print all elements with their row and column index  
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}]= {matrix[i][j]}")


# 🧪 Practice Task 2: Replace all even numbers with 0, odd with 1
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7,8,9]
]
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column]%2 == 0:
            matrix[row][column] = 0
        else:
            matrix[row][column] = 1

print(matrix)

even_count = 0
odd_count = 0
for row in range(len(matrix)):
    for coulmn in range(len(matrix[row])):
        if matrix[row][coulmn] % 2 ==0:
            even_count += 1
        else:
            odd_count+=1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)