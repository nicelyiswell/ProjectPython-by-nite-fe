integer = int(input())

if 1 <= integer <= 1000:
    for d in range(1, integer + 1):
        if integer % d == 0:
            print(d)
else:
    print("Invalid input")