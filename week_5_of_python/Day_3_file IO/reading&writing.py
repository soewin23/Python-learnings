# r+ mode for ---> rading and writig

"""r+ mode overrides at the starting of the text."""

f = open("write.txt","r+")
f.write("abcd")
print(f.read())
f.close
print(f)