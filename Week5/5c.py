def avg(a=None,b=None,c=None): 
    line = 3
    if b == None:
        line -= 1
        b = 0 
    if c == None:
        line -= 1
        c = 0 
    return round((a+b+c)/(line),2)
    


a = int(input())
b = int(input())
c = int(input())
print(avg(a,b,c))
print(avg(a,b))
print(avg(a))