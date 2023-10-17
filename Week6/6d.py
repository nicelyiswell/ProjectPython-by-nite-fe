def recursion(num,count):
    print(" "*count+num*"*")
    if num > 1:
        recursion(num-1,count+1)
    
def Out_put (num,count=0):
    if num>1:
        recursion(num,count)
        Out_put(num-1,count+1) 

n= int(input()) 
Out_put(n)
