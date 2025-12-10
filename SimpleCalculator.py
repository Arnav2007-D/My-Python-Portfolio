while True:
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    option = int(input("Choose an Operation: "))
    result = 0
    if option in [1, 2, 3, 4]:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a number: "))

        if option == 1:
            result = num1 + num2
        elif option == 2:
            result = num1 - num2
        elif option == 3:
            result = num1 * num2
        elif option == 4:
            result = num1 / num2

        print("The result of this operation is {}".format(result))

    else:
        print("Invalid Operation entered")

    print("1. Another problem")
    print("2. Exit")
    selection = int(input("Enter Choice: "))

    if selection == 2:
        break
