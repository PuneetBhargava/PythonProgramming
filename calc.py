isCont = 'Y'
print("Welcome to the calculator application")
while isCont == 'Y' or isCont == 'y':
    print("1. Addition")
    print("2. Multiplication")
    print("3. Division")
    print("4. Subtraction")
    operation = int(input("Please select the operation : "))
    if operation == 1:
        print("-------------------------------------")
        print("you have selected Addition operation")
        print("-------------------------------------")
        n1 = int(input("Please enter first number : "))
        n2 = int(input("Please enter first number : "))
        addition = n1 + n2
        print("Sum of n1 & n2 is =", addition)
        print("-------------------------------------")
    elif operation == 2:
        print("-------------------------------------")
        print("you have selected Multiplication operation")
        print("-------------------------------------")
        n1 = int(input("Please enter first number : "))
        n2 = int(input("Please enter first number : "))
        multiplication = n1 * n2
        print("Sum of n1 & n2 is =", multiplication)
        print("-------------------------------------")
    elif operation == 3:
        print("-------------------------------------")
        print("you have selected Division operation")
        print("-------------------------------------")
        n1 = int(input("Please enter first number : "))
        n2 = int(input("Please enter first number : "))
        division = n1 / n2
        print("Sum of n1 & n2 is =", division)
        print("-------------------------------------")
    elif operation == 4:
        print("-------------------------------------")
        print("you have selected Subtraction operation")
        print("-------------------------------------")
        n1 = int(input("Please enter first number : "))
        n2 = int(input("Please enter first number : "))
        subtraction = n1 - n2
        print("Sum of n1 & n2 is =", subtraction)
        print("-------------------------------------")
    else:
        print("invalid operation selected")
    isCont = input("press Y to continue..")


