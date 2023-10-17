n = abs(int(input())) 
total = 0
digits_found = []
if 0 <= n <=2**20:
     
    while n>0: 
        one_digit = n%10 
        if one_digit in digits_found:
            digits_found.append(one_digit)
            total += one_digit
        else:

        n = n//10 

    print(total) 

else :
    print("Error")
