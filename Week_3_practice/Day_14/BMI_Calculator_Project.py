# BMI calculator

height = float(input("Enter your height in metre :"))
weight = float(input("Enter your weight in kilograms: "))

BMI = weight / (height ** 2)
if BMI < 18.5:
    print(f"{BMI},--> This is underweight")
elif 18.5 <= BMI < 24.9:
    print(f"{BMI} ---> THis is in a healthy weight range")
elif 25 <= BMI < 29.9:
    print(f"{BMI} --> this is overweight")
else:
    print(f"{BMI} You are obese")
