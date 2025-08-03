# Copy a dict

# Using a copy()method
About_Me = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
new = About_Me.copy()
print(new)


# using a built-in function dict()
About_Me = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
my = dict(About_Me)
print(my)