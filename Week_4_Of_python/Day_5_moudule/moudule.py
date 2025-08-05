# moudule = a file containing code you want to include in your program
#             use import to include a moudule (built-in or your own)
#             useful to break up a large program reusable separate file

"""print(help("modules"))"""#find out thee built in module

# import math
import math as me  #<--alius
# we can also give the nick name of modules we use " as  (name)"
print(me.pi)

# if you use from import (module )
from math import pi
print(pi)

import math 
a,b,c,d,e = 1,2,3,4,5

# e is an exponential constant
print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)
