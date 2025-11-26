balance = 1000

while True:
    type = input("Enter the type credit / debit / stop : ")
    if type == "stop":
        break
    elif type == "credit":
        credit_amount = int(input("Enter the credit amount: "))
        balance = balance + credit_amount
        print(f"The current Balance is {balance}")

    elif type == "debit":
        debit_amount = int(input("Enter the debit amount: "))
        if balance < debit_amount:
            print("Insufficient balance!")
        else:
            balance = balance - debit_amount
            print(f"The current Balance is {balance}")

    else:
        print("Invalid option! Try again.")
