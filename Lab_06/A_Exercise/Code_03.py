balance = int(input("enter yourbalance1:"))
while True:
    if balance <= 9000:
        continue
    else:
        balance = balance + 999.99
        print("Balance is", balance)
        break