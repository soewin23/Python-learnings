# key word Arguments
# WE can pass arguments using the names of the parameters.
def descirbe_pet(animal, name):
    print(f"I have a/an {animal}, named {name}")

descirbe_pet(animal= "Husky",name="Jhony")
print("_______________________-")

# 1️⃣ Create a function called introduce that takes two arguments: name and hobby
# Print: "My name is <name> and I love <hobby>"
def introduce(name, hobby):
    print(f"My name is {name}, and Hobby is {hobby}")

introduce(name ="Bimal",hobby="coding")#<--- keywords are here
print("_______________________-")

# Create a function student(name, grade)
# and call it using keyword arguments in any order.
def student(name, grade):
    print(f"Name is {name}, grade is {grade}")

student(name="Sion", grade="A+")
print("_______________________-")

