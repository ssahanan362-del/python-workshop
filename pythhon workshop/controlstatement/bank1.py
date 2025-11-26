balance=10000
cd=input("enter a amount whether you have to credit /debit")
if(cd=="Debit"):
    amount = int(input("Enter amount to dedit: "))
    if amount <= 0:
        print("Invalid amount.")
    else:
        balance = balance - amount
        print("Amount dedited successfully!")
        print("Updated Balance:", balance)
elif(cd=="Credit"):
    amount = int(input("Enter amount to dedit: "))
        balance = balance + amount
        print("Amount dited successfully!")
        print("Updated Balance:", balance)
    else:
    print("enter the correct choice")