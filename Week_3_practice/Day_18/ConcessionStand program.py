
# Concession Stand Program

# dictionary (key: value)

menu = {
    "pizza":4.58,
    "popcorn": 6.00,
    "chips": 1.22,
    "pret zel": 3.58,
    "lemonade": 3.00,
    'fries': 2.50,
}

cart =[]
total = 0

print("-----------MENU----------------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}$")# format speceficior for 2 decimial place
    # :10 for ten spaces
print("---------------------------")
A = True
while A:
    food = input("Selete an items (q to quit : )").lower()
    if food == 'q':
        A = False
    elif food  in menu:
            cart.append(food)
    else:
         print("item is not avavilable")
print(cart)

print("-----------YOUR ORDER----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" " )

print()
print(f"\nTotal is : ${total:.2f}")
