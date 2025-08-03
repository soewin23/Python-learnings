#  # Grade analyzer

def grade_calculator(score):
    if score > 100:
        return "Invalid score"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
students ={}

while True:
    name = input("\n Enter a name ( or Enter 'quit' to exit)")
    if name.lower() == "quit":
        break
    score = input(f"\nEnter {name}'s score :")
    if not score.isdigit() or (0 <= int(score) >= 100):
        print(f"{score}'s is invalid synthx, Please Enter a number between (0 to 100): ")
        continue
    students[name] = int(score)

print("\nStudent grade : ")
for name , score in students.items():
    grade = grade_calculator(score)
    print(f"Student name = {name} : score = {score} : Grade = {grade}")

if students:
    print("Average score of the Calss")
    avg = sum(students.values()) / len(students)
    print(f'\n Calss average score = {avg}')
else:
    print("\nNO student entered ")

while True:
    lookup = input("\nEnter a student name to check thier grade (or Enter 'exit' to quit) : ")
    if lookup.lower() == "exit":
        break
    if lookup in students:
        print(f"{lookup}'s grade : {grade_calculator(students[lookup])}")
    else:
        print("Student is not found ")
