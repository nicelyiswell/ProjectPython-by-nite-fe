a = int(input())
b = int(input())
if a > 0 and b > 0 :
        for i in range(1 , a+1) :
            if i%b == 0  :
                print(i)
            else :
                print(i , end=" ")
            
                
            
            
else : 
    print("Invalid input")