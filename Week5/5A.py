def min(x,y,z):
    min = x
    if y < min:
        min = y 
    if z < min :
        min = z
    return (min) 

a = int(input())
b = int(input())
c = int(input())
print(min(a,b,c))
