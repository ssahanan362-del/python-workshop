def userInput():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1, num2


def add(a=0, b=0):
    return a + b

def sub(a=0, b=0):
    return a - b

def multi(a=0, b=0):
    return a * b

def div(a=0, b=0):
    if b == 0:
        return "Error! Division by zero."
    return a / b


print("Welcome to Calculator")
while True:
    print("\nSelect a choice:\n 1: Add\n 2: Sub\n 3: Div\n 4: Multi\n 5: Stop")
    choose = int(input("Enter the choice: "))

    if choose == 1:
        x, y = userInput()
        print(f"Addition: {add(x, y)}")

    elif choose == 2:
        x, y = userInput()
        print(f"Subtraction: {sub(x, y)}")

    elif choose == 3:
        x, y = userInput()
        print(f"Division: {div(x, y)}")

    elif choose == 4:
        x, y = userInput()
        print(f"Multiplication: {multi(x, y)}")

    elif choose == 5:
        print("Calculator Stopped.")
        break

    else:
        print("Invalid choice! Try again.")
