import random
cards =["A",'2','3','4','5','6','7','8','9','K',"Q",'J']

# for random choice
choices = random.choice(cards)
print(choices)

# to shuffle the items in variable
random.shuffle(cards)
print(cards)