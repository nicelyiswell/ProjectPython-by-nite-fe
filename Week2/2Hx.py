xa1 = int(input())
ya1 = int(input())
xa2 = int(input())
ya2 = int(input())
xb1 = int(input())
yb1 = int(input())
xb2 = int(input())
yb2 = int(input())

if xa1 > xb1 :
    left = xa1
else :
    left = xb1
    
if xa2 < xb2 :
    right = xa2
else :
    right = xb2 
    
if ya1 < yb1 :
    top = ya1
else : 
    top = yb1

if ya2 > yb2 :
    low = ya2
else : 
    low = yb2
    
if left < right and top > low :
    width = right - left
    hight = top - low
    print(width * hight) 
else :
    print(0)