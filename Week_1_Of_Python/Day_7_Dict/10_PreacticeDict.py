# Create a dictionary of a student: name, age, grade

# Print the student's name and grade
student = {
    "name": "Alice",
    "age": 17,
    "grade": "A"
}
print("Name : ", student["name"])#Name :  Alice
print("Grade : ", student["grade"])#Grade :  A
print("--------------------------------------")

# Change the age to 18
# Add a new key 'school' with value 'Greenwood High'
student.update({"age": 18})
print(student)#{'name': 'Alice', 'age': 18, 'grade': 'A'}


# Add a new key 'school' with value 'Greenwood High'
student = {
    "name": "Alice",
    "age": 17,
    "grade": "A"
}

student.update({"School":"Greenwood High"})
print(student)

print("--------------------------------------")


# Remove 'grade' key using pop()
# Try to remove 'address' key using pop() with a default message

# Print all keys
# Print all values
# Print keys and values using .items()

# Make a copy of the student dictionary and modify the name to "Bob"
# Show that the original dictionary didn’t change


# Create a dictionary of 2 students
students = {
    "student1": {"name": "Alice", "age": 17},
    "student2": {"name": "Bob", "age": 18}
}
# Print Bob’s age


# Create a dictionary of 2 students
students = {
    "student1": {"name": "Alice", "age": 17},
    "student2": {"name": "Bob", "age": 18}
}
# Print Bob’s age





person = {
    "name": "Charlie",
    "age": 25,
    "skills": ["Python", "ML"]
}
# Use .get() to get age

# Use .update() to add a new key: "city": "Yangon"

# Use .setdefault() to add "gender": "Male"

# Use .values() to list all values

# Use .clear() and print it