#PYython_Number Guessing Game


import random

lowest_number =1 
highest_number = 100
answer = random.randint(lowest_number, highest_number)


guesses = 0
is_running = True
print("-------------------------------------------------------------")
print("Python_Number_Guessing Games")
print("------------------------------")
print(f"Select a number between {lowest_number} and {highest_number} ")

while is_running:
    guess = input("Enter your guess: ").strip()
    
    if guess.isdigit():
        guess= int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("-----------------")
            print("That number is out of range")
            print("----------------------")
            print(f"Please Select a number again, between {lowest_number} and {highest_number} ")
        elif guess < answer:
            print("too low try again")
        elif guess > answer:
            print("Too high,Try again")
        else:
            print("---------------------------")
            print(f"You've guessed the correct number!! {guess}")
            print("---------")
            print(f"Number of guesses : {guesses}")
            print('-------------------------------------------------------')
            is_running = False # break  to quit the while toop
    else:
        print("invalid guess")
        print("-----------------")
        print(f"Please Select a number again, between {lowest_number} and {highest_number} ")
        print("---------------------------")
        
