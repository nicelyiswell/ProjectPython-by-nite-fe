number = int(input())
if number > 0 and number < 11:
    while number > -1 :
        print(number)
        number -= 1
elif number == 0 :
    print("0")
else :
    print("Invalid input")