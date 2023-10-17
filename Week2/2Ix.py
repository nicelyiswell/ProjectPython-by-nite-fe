n = int(input())
if n % 2 != 0 and 1 <= n <= 29 : 
    
    for i in range(0 , n // 2) : 
        left_top = i
        right_top = (n-2)-2*i
        print(" "*left_top + "\\" + " "*right_top + "/" + " "*left_top)
        
    print(" " * (n//2) + "X" + " " * (n//2))
    
    for i in range(n // 2 -1 , -1 , -1):
        left_bottom = i
        right_bottom = (n - 2) - 2 * i
        print(" "*left_bottom + "/" + " "*right_bottom + "\\" + " "* left_bottom )
else :
    print("Invalid input") 
    
    