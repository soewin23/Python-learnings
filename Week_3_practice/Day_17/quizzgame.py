questions = ("1. how many elements are in the periodic table? : ",
             "2. Which animal lays the largest agges? : ",
             "3. What is the most abundant gas in the Earth's atmosphere? : ",
             "4. How many bones in the human body? : ",
             "5. Which planet in the solar system is the hottest? : ")
 
options = (("A. 116 ","B. 118 ","C. 117 ","D. 119" ),
           ("A. Whale","B. Crocodile","C.  Elephant","D. Ostrich " ),
           ("A. Nitrogen","B. Oxygen ","C. carbon_Dioide ","D. Hydrogem  " ),
           ("A.206","B.207 ","C.208 ","D.209 " ),
           ("A. Mercury ","B. VEnus","C. Earth ","D. Mars" ))

answers = ("C","D","A","A","B")

guesses =[] 

score = 0

question_num = 0

for question in questions:
    print("----------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D)").upper() 
    guesses.append(guess)
    if guess == answers[question_num]:
        score =score + 1
        print("correct")
        print(f"score ={score} " )

        
    else:
        print("incorrest")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("----------------------------------------------------")
print("                       RESULTS                      ")
print("----------------------------------------------------")


print("answers : ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses : ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
percentage = int((score / len(questions)*100))
print(f"Your score = {percentage} % ")