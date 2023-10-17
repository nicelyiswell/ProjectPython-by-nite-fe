while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        print("The sum is", num1 + num2)
        break
    except ValueError:
        print("ERROR: Invalid input")