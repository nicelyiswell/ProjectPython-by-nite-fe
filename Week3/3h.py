n = int(input())
ball = 0

print(ball + 1)  
ball = (ball + 3) % n 


while ball != 0:  
    print(ball + 1) 
    ball = (ball + 3) % n