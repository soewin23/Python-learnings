
"""Personal Expanse Tracker """
def show_menu():
    print("\n===== Expense Tracker Menu =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter Expenses")
    print("4. Save to File")
    print("5. Load from File")
    print("6. Exit")

expense =[]

while True:
    show_menu()
    choice = input("Enter your choice (1-6) : ")

    if choice == "1":
        print("Add Expense selected")
        break
    elif choice == "2":
        print("View Expense selected")
    elif choice == "3":
        print("Filter seleceted")
    elif choice == "4":
        print("Saving to file...")
    elif choice == "5":
        print("Loading from file..")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invaid choice.Please enter 1-6.")

def add_expanse():
    try:
        amount = float(input("Enter amount : "))
        category = input("Enter category: ")
        date = input("Enter date (e.g. 2025-08-02): ")
        note = input("Enter note(optinal): ")
        expenses = {
        "Amount" : amount,
        "Category" : category,
        "Date" : date,
        "Note": note
    }
        expense.append(expenses)
        print("Expense added succeddfully .")
    except ValueError:
        print("Invalid amount. Please enter a number.")


if choice =="1":
    add_expanse()