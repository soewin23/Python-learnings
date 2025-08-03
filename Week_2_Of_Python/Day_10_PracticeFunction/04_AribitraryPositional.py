# Arbitrary Positional Arguments (*args)

# Use *args when you don’t know how many arguments will be passed
def add_all(*numbers):
    total = sum(numbers)
    print("Total", total)

add_all(1,2,3,4,5)

# Create a function sum_marks(*marks) that prints the total.
def sum_marks(*marks):
    total_marks = sum(marks)
    return total_marks
point = sum_marks(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,221)
print(point)
