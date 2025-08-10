
count =0

with open("A.txt","r")as file:
    data = file.read()

    nums = data.split(",")
    for val in nums:
        if (int(val) %2 ==0):
            count += 1 
            
print(count)