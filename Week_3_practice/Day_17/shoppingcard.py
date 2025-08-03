# shopping cards program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        items = int(input("how many items you want? :"))
        price = float(input(f"Enter the prize of a {food} :$ "))
        foods.append(food)
        prices.append(price)

print("-------Your cart------")
print()
for food in foods:
    print(food, end="\t| ")# to list horizontally we use end = ""

for price in prices:
    total += (price* items)
print(f"\nyour total is $ {total}")