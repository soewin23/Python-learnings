
# write mode "w"---> overwrite mode

file = open("write.txt", "w")
file.write("hello the is my week five of learning python\n" \
" And I'm very excctioed to learn this file IO")
file.close()

# appen d mode "a"---> write at the end mode
file1 = open("write.txt", "a")
file1.write("\nI'm watching a tutrorial ablut file IO")
file1.close()

# "a+" mode will read and write the file 
file2 = open("write.txt","a+")
print(file2.read())
file2.write("print(helloWorld)")

file2.close()
