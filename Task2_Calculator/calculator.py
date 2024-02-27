# Python Programming Internship
# Roaa Fathi
# Last Submission Date: 5 Sep.
# Simple Calculator Task

# Adds two numbers
def add(x, y):
    return x + y


# Subtracts two numbers
def subtract(x, y):
    return x - y


# Multiplies two numbers
def multiply(x, y):
    return x * y


# Divides two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"


# Checks operation validation
def check_operation(operation_list):
    if len(operation_list) != 3:
        return True
    return False


# Displays main menu and enables input
def calculator():
    while True:
        print("========= Welcome to Simple Calculator ===========")
        print("** Write end to exit **")
        operation = input("Enter two numbers and an operation as in normal calculator separated by spaces (e.g. 5 + "
                          "8): ")
        if operation == "end":
            print("Thanks for using our Calculator!\n")
            break

        operation_list = operation.split()
        if check_operation(operation_list):
            print("Invalid input format. Please provide two numbers and an operation.")
        else:
            try:
                num1 = float(operation_list[0])
                num2 = float(operation_list[2])
                operator = operation_list[1]

                if operator == '+':
                    result = add(num1, num2)
                elif operator == '-':
                    result = subtract(num1, num2)
                elif operator == '*':
                    result = multiply(num1, num2)
                elif operator == '/':
                    result = divide(num1, num2)
                else:
                    print("Invalid operator. Please use +, -, *, or /.")
                    continue  # Skip the calculation if the operator is invalid
                print("Result:", result)

            except ValueError:
                print("Invalid input format. Please provide valid numeric input.")


calculator()
