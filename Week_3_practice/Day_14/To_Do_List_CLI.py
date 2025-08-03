# To-Do List CLI App

tasks =[]
while True:
        print("\nTo Do List MEnu")
        print("1. Add Task")
        print("2. View task")
        print("3. Remove Task")
        print("4. Quit")
        choice = input("Enter your choice(1/2/3/4) :")
    
        if choice == "1":
            task = input("Enter you task : ")
            tasks.append(task)
            print("Task added")

        elif choice == "2":
            print("\n Your Tasks : ")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif choice =="3":
            task_num = int(input("Enter a task number to reomve : "))
            if 1 <= task_num <= len(tasks):
                remove = tasks.pop(task_num - 1)
                print(f"remove taks : {remove}")
            else :
                print("invalid Number ")
        elif choice == "4":
            print("Good bye, See you soon😊😊")
            break
        else:
            print("invalid Text")

print("Memory-Based project complete✅")