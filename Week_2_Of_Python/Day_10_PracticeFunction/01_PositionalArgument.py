# Positional argument
# Arguments passed in order. Python matches them by position.

def argument(Arrg):
    print(f"{Arrg}This is  an argument!")
argument("What ")

# postitional Arguments

def greet(name, age):
    print(f"Hello! {name}, you are {age} years old.")

greet("Sion",18)

"""Practice question"""

# 1️⃣ Create a function called introduce that takes two arguments: name and hobby
# Print: "My name is <name> and I love <hobby>"

def introduce(name, hobby):
    print(f"My name is {name},and I love {hobby}")

introduce("Soe", "coding")

print("-------")


# Write a function introduce(first, last) that prints:
# "My name is <first> <last>"
def introduce(first, last):
    print(f"My first name is {first} and the last name is {last}")

introduce("Soe", "Win")


# Create a function that takes user input for name and email, and uses
def regester_user():
    user_name = input("Enter your name :")
    user_email = input("Enter your Email")
    role = input("Do you want to change the role or use a default'student( yes/no)").lower()
    if role == "no":
        role = "student"
    elif role == "yes":
        role = input("Enter your role :")
    else:
        role = 'student'
    active = input("ARe you actve as student :").lower()
    if active == "yes":
        active ="active"
    elif active =="no":
        active = "Not active"
    else:
        active = "error"
    return{"name":user_name, "email": user_email,"role":role, "active":active}
user_info = regester_user()

print("\n✅ Register User Info:")
print(user_info)