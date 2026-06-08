# ATM System

correct_pin = 1234
balance = 10000

# PIN Verification
pin = int(input("Enter ATM PIN: "))

if pin == correct_pin:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    choice = int(input("Enter your choice (1-3): "))

    match choice:

        case 1:
            print("Current Balance: Rs.", balance)

        case 2:
            amount = float(input("Enter withdrawal amount: "))

            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print("Withdrawal Successful")
                    print("Remaining Balance: Rs.", balance)
                else:
                    print("Insufficient Funds")
            else:
                print("Invalid Amount")

        case 3:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Deposit Successful")
                print("Updated Balance: Rs.", balance)
            else:
                print("Invalid Amount")

        case _:
            print("Invalid Menu Choice")

else:
    print("Incorrect PIN")