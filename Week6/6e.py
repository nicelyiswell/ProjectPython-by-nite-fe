
def binary(quotient, printZero =True):
    if quotient>0:
        binary(quotient//2 , False)
        print(quotient%2, end="")
    elif printZero == True:
        print("0",end="")

binary(int(input()))
print()
