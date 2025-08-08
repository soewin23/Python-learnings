def cal():
    while True:
        try:
            x = float(input("Enter the first number: "))
            y = input("Enter an Operator : (+,-,*,/,%,**) : ")
            z = float(input("Enter the second Number : "))
            
            if y == "+":
                return f"Your Answer is : {x + z}"
            if y == "-":
                return f"Your Answer is : {x - z}"
            if y == "*":
                return f"Your Answer is : {x * z}"
            if y == "/":
                return f"Your Answer is : {x / z}"
            if y == "**":
                return f"Your Answer is : {x ** z}"
        except:
            return "invalid input"

print(cal())
