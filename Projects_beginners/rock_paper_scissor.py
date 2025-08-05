import random


print('--------------------Rock-Paper-Scissors------------------------')
options = ("rock", "paper", "scissors")
running = True


while running:


    player = None
    Computer = random.choice(options)

    while True:
        player = input("Enter a choices (rock, paper, scissors): ").strip()
        print("--------------")

        if player not in options:
            print("ENter again from optins :")
            print("--------------")
        else:
            break


    print(f"Player : {player}")
    print(f"Computer : {Computer}")
    print("------------------------------------------")


    if player == Computer:
        print("It's a tie!")
        print("--------------")
    elif player == "rock" and Computer == "scissors":
        print("You win! ")
        print("--------------")
    elif player == "paper" and Computer == "rock":
        print("You win! ")
        print("--------------")
    elif player == "scissors" and Computer == "paper":
        print("You win !")
        print("--------------")
    else:
        print("YOu lose")
        print("--------------")


    if not input("play again  (y/n) :").islower()!= 'y':
        running = False
    
print("Thank for playing !!!")








