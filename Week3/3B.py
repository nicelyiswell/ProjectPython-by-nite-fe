import math
a = int(input())
b = int(input())
if a > 0 and b > 0 :
    for i in range(1, b+1):
        for x in range(math.floor(a/b)+1):
            if(i + (b*x) <= a ) :
                print(i + (b*x), end=" " )
        print(" ")      
              
            
else : 
    print("Invalid input")
