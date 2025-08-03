        # we can also add else and finally to control what runs when there's no error and always, respcitively

try:
    age = int(input("Enter your age :"))
except ValueError:
    print("Invalid input, Age must be a numbe.")
else:
    print("Your age is : ", age)
finally:
    print("thank you for using the program")