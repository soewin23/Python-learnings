# Default Arguments
# If an argument is not passed, the default value is used.

def greet(name, Country ="Nepal"):
    print(f"Hello, I'm {name} form {Country}.")

greet("SoeWin") #uses Default Country name
greet("Sion", "Myanmer")

# Create intro(name, hobby="coding") that prints both.
def intro(name, hobby= "Coding"):
    print(f"I'm {name}, I love {hobby}.")

intro("Soe")
intro("Soe Win", "Gaming")

# 🧠 Q2. Define a function power that raises a number to a power. 
# Default power should be 2.
# Example: power(5) → 25, power(5, 3) → 125
def Power(number = 1, power = 2):
    print(f"The {power}th power of {number} is {number**power}")
Power(number= 5, power=3)

print("-------")

# 🧠 Q3. Create a function to calculate discounted price.
# By default, discount is 10%.

# # discounted_price(100) → 90.0
# # discounted_price(100, 20) → 80.0
def discount(price, discount =10):
    if discount == 10:
        discount_prize = price - (price *(discount/100))
        return discount_prize
    elif discount == discount:
        discount_prize = price - (price *(discount/100))
        return discount_prize
print(discount(100,20))
