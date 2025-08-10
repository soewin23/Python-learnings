# Create a new file "practice.txt" using python. And the follwing data in it:

'''
HI wvwryone 
we are learning file I/O
using Java.
I kike programming in Java.'''


# with open("practice.txt", "w")as file:
#     file.write("hi everyone\nWe are learning file I\O \nusing Java\nI like programming in Java.")


"""The folder was created with above code."""

# WAf the replace all occourance of java with "python" in ablove file.

with open("practice.txt", "r") as file:
    data = file.read()
#we store info of file in variable and if becomes a string
#And string can be manupliated

new_data = data.replace("Java", "Python")
print(new_data)


"""##Now let's override that old data from java to python."""

with open("practice.txt", "w")as file:
    file.write(new_data)
# this change will occour in the old file of line no.10

# look at the output of the line no.18 it changed👌👌👌




