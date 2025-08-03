        #Loopin dict

# Using for loop to return keys
About_Me = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
for a in About_Me:
    print(a )#**ONly return the keys of Dict
print(".....")
"""Or"""

# Using ,keys() methods to return the keys of Dict
for i in About_Me.keys():
    print(i)
print(".....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxx")


#Using for loop to return valus
About_Me = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
for i in About_Me:
    print(About_Me[i]) #** it will return only valuse of Dicts
print(".....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxx")

"""Or"""
#using .values()  method to return vaule of Dict
for i in About_Me.values():
    print(i)
print(".....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxx")
# We learn about looping the keys and values separately
# Now we will learn about looping together


#Using .items() method to loop both value of Dict
About_Me = {'name': 'xxxx', 'age': 1101, 'year': 21007, 'Gender': 'Male', 'Student': True}
for i in About_Me.items():
    print(i)
print(".....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxxx.....xxx")