# 🧠 Concepts for  Reinforce:

# Conditional logic
# Loops (while, break)
# Functions
# Type conversion & error handling
# String formatting
# Input/output

def add(x,y):
    return x +y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "You can't divide by Zero"
    return x/y

def Remainder(x,y):
    return x%y

def Exponent(x,y):
    return x**y

def display_menu():
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Finding remainder")
    print("6.Exponent")
    print("7. Quit")

while True:
    display_menu()
    choice = input("Choose operation (1-7): ")

    if choice == "7":
        print("Extisting calculator. Goodbye!. ")
        break

    if choice not in ("1","2","3","4","5","6","7" ):
        print("Invalid choice. Try again")
        continue

    try:
        num1 = float(input("Enter first Number :"))
        num2 = float(input("Enter second number : "))
    except ValueError:
        print("Invalid input. Please enter numbers. ")
    if choice == "1":
        result = add(num1 + num2)
    if choice == "2":
        result = substract(num1 - num2)
    if choice == "3":
        result = multiply(num1 * num2)
    if choice == "4":
        result = divide(num1 / num2)
    if choice == "5":
        result = Remainder(num1 % num2)
    if choice == "5":
        result = Exponent(num1 ** num2)
    print(f"Result --> {result}")
