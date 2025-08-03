# . Arbitrary Keyword Arguments (**kwargs)
#**kwargs allows you to pass any number of keyword arguments (key-value pairs) to a function. 
# It collects them into a dictionary.
def profile(**info):
    print(info)
profile(a = 12,v = 12)

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}=>{value}")

A = show_details(name ='soe',age= 18,country= "Earth")
print(A, end='')

def inf(**hi):
    for key, value in hi.items():
        return f'{key}=>{value}'

print(inf(name = "Thar", hobby='coding', age = 18))

# 🧠 Challenge:
# Create a function greet_user(**kwargs) that:

# Gets the user’s name from kwargs

# If the name is provided, print: "Hello, <name>!"

# If not, print: "Hello, Guest!"

def greet_user(**kwargs):
    name = kwargs.get("name") # to get the name key only
    if name:
        return f'Hello, {name}'
    else:
        return f"hello, Guest"
    
user = greet_user(age = 18)
print(user)


# 🧠 Task:
# Create a function called display_profile(**kwargs) that:

# Prints "Name: ..." only if "name" is provided

# Prints "Email: ..." only if "email" is provided

# If neither is provided, print: "No name or email provided"

def display_function(**kwargs):
    name = kwargs.get("name")
    email = kwargs.get("email")
    if name and email:
        print(f'name: {name}')
        print(f'Email : {email}')
    elif name:
        print(f"Name :{name}")
    elif name :
        print(f'Email : {email}')
    
    else:
        print(f"No name or email provided")
display_function(name = "Soe", email = "soofs@.gmali.com")
display_function(age=18)

# Write a function register_user(name, age, *skills, country="Nepal", **extra_info) that:

# Prints name and age

# Lists skills

# Prints other data like email="xyz@gmail.com"

def register_user(name, age, *skills, country="Nepal", **extra_info):
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)
    print("Country:", country)
    print("Extra Info:", extra_info)
register_user("Soe",18, "python","java",email = 'adfa@gmail')


# #✍️ Task:

# def calculate(a, b, op='+'):
#     # If op == '+', return a + b
#     # If op == '*', return a * b

def calculate(a, b, op='+'):
    if op== '+':
        return a+b
    else:
        return a * b
print(calculate(12,12,"*"))