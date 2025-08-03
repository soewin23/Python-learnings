# filter()<---Keep items that match condition	


# filter() selects only the items that pass a condition 
# (the condition is written as a function like a lambda).

num = [1,2,3,4,5,6,7,8,9,10]
# keep only even numbers
even = tuple(filter(lambda i: i%2==0,num))#filter() applies this condition to each number.
# Only numbers where the condition is True are kept.
print(even) #(2, 4, 6, 8, 10)

a = []
for i in range(1,11):
    a.append(i**2)
evens= list(filter(lambda i: i%2==0,a))#filter() applies this condition to each number.
print(evens)
print(a)


