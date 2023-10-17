number = int(input())
number_row = int(input()) 
if number and number_row > 0:
    print(('*'*number+'\n')*number_row)
else :
    print("Invalid input")
    
