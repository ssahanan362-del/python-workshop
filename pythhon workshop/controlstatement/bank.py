balance=10000
choice=input("Enter whether you want to Credit or Debit:")

if choice=="Debit":
    amount=int(input("Enter amount to debit:"))
    if amount<=0:
        print("Invalid amount.")
    elif amount>balance:
        print("Not sufficient balance!")
    else:
        balance=balance-amount
        print("Amount debited successfully!")
        print("Updated Balance:", balance)

elif choice=="Credit":
    amount=int(input("Enter amount to credit:"))
    if amount<=0:
        print("Invalid amount.")
    else:
        balance=balance+amount
        print("Amount credited successfully")
        print("Updated Balance:",balance)
else:
    print("Enter the correct choice")
balance = 10000
choice = input("Enter whether you want to Credit or Debit:")

if choice == "Debit":
    amount = int(input("Enter amount to debit:"))
    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Not sufficient balance!")
    else:
        balance = balance - amount
        print("Amount debited successfully!")
        print("Updated Balance:", balance)

elif choice == "Credit":
    amount = int(input("Enter amount to credit:"))
    if amount <= 0:
        print("Invalid amount.")
    else:
        balance = balance + amount
        print("Amount credited successfully")
        print("Updated Balance:", balance)
else:
    print("Enter the correct choice")


