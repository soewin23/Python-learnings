# Modifying Global Variables Inside Functions

# By default, if you assign a value to a variable inside a function, Python treats it as local.

greeting = "hello" #<--- Global variable
def greet():
    print(greeting)
greet()#<--Works fine
print(greeting)#<-- also works fine

"""BUT"""
# To modify a global variable inside a function, use the global keyword.
count = [] #<--- Global variable
def incerase():
    global count
    for i in range( 1,10):
       count.append(i)

incerase()
print(count)

even_numbers = []

def fill_even():
    # Add only even numbers from 1 to 20 to even_numbers using global keyword
    global even_numbers
    for i in range(1,21):
        if i%2== 0:
            even_numbers.append(i)
fill_even()   
print(even_numbers)


limit =[]
def even_num(A):
    global limit
    for i in range (1, A +1):
        if i % 2 ==0:
            limit.append(i)
even_num(12)
print(limit)