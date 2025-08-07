
# closure is a function having access to the scope
# of its parent after the parent function has return

#nested function

def parent_function(person):
    coin =3
    
    def play_game():
        nonlocal coin
        coin -= 1

        if coin > 1:
            print("\n"+ person + "has"+str(coin)+ " coins left.")
        elif coin == 1:
            print("\n"+ person + "has"+str(coin)+ "coins left.")
        else:
            print("\n"+ person + "is out of the coins")


    return play_game

tommy = parent_function("tommy")
Arno = parent_function("Arno")

tommy()
tommy()
Arno()

