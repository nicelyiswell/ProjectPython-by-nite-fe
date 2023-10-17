min = 0
max = 0 
number = 0
while True:
    number = int(input())
    if number > max:
            max = max + number 
    elif number < min:
            min = min + number 
    if number == "$" :
            print(min + "\n" + max)  
            break
    