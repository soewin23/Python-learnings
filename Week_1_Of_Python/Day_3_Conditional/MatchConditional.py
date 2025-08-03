# The Python Match Statement
"""Instead of writing many if..else statements, you can use the match statement.

The match statement selects one of many code blocks to be executed."""
"""Example

match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
    
    """


Day = int(input("Enter a num (1-7)"))

match Day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesay")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
        