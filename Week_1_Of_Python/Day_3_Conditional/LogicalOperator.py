#           There are 3 logical main logical OPerator

# and Ooperator

a = True
b = False 
if a == True and b == False: # Returns True if both statements are true
    print("the condition are true")
else:
    print("false")


# Or Operator
soe = True
win = False
if soe == True or win == False:  #	Returns True if one of the statements is true
    print("True")
else:
    print("False")



# not operator
A = True

if A is not False:
    print("True")
else:
    print("False")


# Python Identity Operators

        # is , is not
# is 
A = "my name is Sion"
if A is str:
    print(f"'{A}' is a String ")
else:
    print(f"{A} is not a string")


# is not

A = 3.14285
if A is float:
    print(f"'{A}' is a flaoting number ")
else:
    print(f"{A} is not a flaoting number")



# Python Membership Operators

# in , not in

me = "this is Soe win I'm 17 yrs old"

A = "17" in me   #Returns True if a sequence with the specified value is present in the object
print(A)

A = "Sion"in me  #Returns True if a sequence with the specified value is not present in the object
print(A)
    
