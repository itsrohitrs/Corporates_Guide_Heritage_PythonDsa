history = []

while True:

    print("\n===== CALCULATOR MENU =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Quit")

    choice = int(input("Enter your choice: "))

    # Quit Option
    if choice == 6:

        print("\n===== CALCULATION HISTORY =====")

        if len(history) == 0:
            print("No operations performed.")

        else:
            for item in history:
                print(item)

        print("Calculator Closed.")
        break

    # Invalid Choice
    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid Choice! Please Try Again.")
        continue

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    match choice:

        case 1:
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"

        case 2:
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"

        case 3:
            result = num1 * num2
            operation = f"{num1} * {num2} = {result}"

        case 4:

            if num2 == 0:
                print("Error! Division by Zero is Not Allowed.")
                continue

            result = num1 / num2
            operation = f"{num1} / {num2} = {result}"

        case 5:
            result = num1 ** num2
            operation = f"{num1} ^ {num2} = {result}"

    print("Result =", result)

    history.append(operation)