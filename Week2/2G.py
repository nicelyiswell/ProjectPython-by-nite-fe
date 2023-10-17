a = int(input())
b = 0
if a >= 1 and a <21:
    for i in range(a, 0, -1):
        print(" "*b +("*"*i))
        b +=1

else :
    print("Invalid input")
