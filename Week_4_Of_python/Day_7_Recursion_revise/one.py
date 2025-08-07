#  Recursion happens in python when a function called itself

def add_one(num):
    if (num>=9):
        return num +1
    
    total = num+ 1
    print(total)
# one through nice is printed from here

    return add_one(total)# this is called the function itself# 
#    ^--> remember to return this recursive call if not it won't print 10 but None
my_total = add_one(0)
print(my_total)# and ten is printed here



def rescur(a):
    
    while a <= 10:
        print(a)
        a+= 1

rescur(1)