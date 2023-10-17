def recursion(num):
    print(num)
    if num > 1:
        recursion(num-1)
    return(num)

n= int(input()) 
(recursion(n))