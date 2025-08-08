def print_list(list, indx=0):
    if indx == len(list):
        return
    print(list[indx])
    print_list(list, indx + 1)

fruit = ['mango', 'litchi', 'apple', 'banana']

print_list(fruit)