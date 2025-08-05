
# Enclosed Scope 


# ehen we have a function inside the function 


def fun1():
    z = 1 #enclosed
    def fun2():
        z = 2  #
        print(z)
    fun2()
fun1()