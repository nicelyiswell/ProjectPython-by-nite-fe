x = abs(int(input()))
number = 0 
while x>0 :
    number = number + (x%10)
    x = x//10 
print(number)