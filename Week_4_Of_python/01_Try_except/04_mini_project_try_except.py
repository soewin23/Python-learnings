try:
    num1 = int(input("Enter a number :"))
    operator = input("Choose an Operator(=,-,*,/,**) :")
    num2 = int(input("Enter a number :"))

    if operator == "+":
        print(f"{num1}+ {num2}= ",num1 + num2)
    elif operator == "-":
        print(f"{num1}- {num2}= ",num1 - num2)
    elif operator == "*":
        print(f"{num1}* {num2}= ",num1 * num2)
    elif operator == "/":
        print(f"{num1}/ {num2}= ",num1 / num2)
    elif operator == "**":
        print(f"{num1}** {num2}= ",num1 ** num2)
    else:
        print("invalid operator.")

except ValueError:
    print("Please enter valid number")
except ZeroDivisionError:
    print("Can't divide by Zero.")
finally:
    print("Calculator finidhed")
