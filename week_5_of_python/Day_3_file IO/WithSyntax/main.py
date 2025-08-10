with open("me.txt","w") as files:
    files.write("hi this is me and I'm doing my work")





with open("me.txt","r") as file:
    data =file.read()
    print(data)


#** We don't need to close file when using with 
# Python automatically close the file

with open("me.txt", "w") as f: #"""this over the me.txt"""
    a = f.write("heheheh")



# to delete a file we need to use a module for that 
import os 
os.remove("me.txt")