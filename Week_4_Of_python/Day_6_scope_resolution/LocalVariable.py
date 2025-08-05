# variable Scope =Where a variable is visible and accessable
# scope resolution (LEGB) LOcal -> Enclosed -> Global -> Built-in


def a():
    a = 1 #Local variable
    print(a)

def s():
    b = 2#Local variable
    print(b)

def d():
    c = 3 #Local variable
    print(c)

a()
s()
d()

# We can write different version of local variable in 
# same function

def a():
    z = 1 #Local variable
    print(z)

def s():
    z = 2#Local variable
    print(z)

a()
s()

