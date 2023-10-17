number = int(input())
if number >= 1 and number < 21 :
    for i in range(number) :
        print(" "*i+ "*")
        
else :
    print("Invalid input")