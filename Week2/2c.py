a = float(input())
b = input()
if b == "USD" :
    c = a // 34.20
    print (int(c))
    print (round(a % 34.20 ,2))
elif b == "EUR" :
    c = a //38.47 
    print (int(c))
    print (round(a % 38.47 ,2))
elif b == "GBP" :
    c = a// 44.73 
    print(int(c))
    print(round(a%44.73 ,2))
elif b == "JPY" :
    c = (a//0.2476)
    print (int(c))
    print(round(a%0.2476 ,2))

