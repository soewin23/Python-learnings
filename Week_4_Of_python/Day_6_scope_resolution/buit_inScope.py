#Buit-in Scope

from math import e

print(e)# built-in

def fun():
    print(e)

e = 3# Global 

fun()
# it eill print(3) because of
# LEGB order that how scope works

