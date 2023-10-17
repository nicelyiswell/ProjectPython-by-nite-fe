def recursion(num):
    
    if num>0:
        recursion(num-1)
        print(num)
    return(num)

n= int(input()) 
(recursion(n))