#Recursion in Python
# when a function calls itself
def show(n):
    if n == 0:#base case
        return
    print(n)
    show(n-1)
show(5)

# Both are same

def loop(n):
    while True:
        if n == 0:
            return 
        print(n)
        n-=1
loop(5)