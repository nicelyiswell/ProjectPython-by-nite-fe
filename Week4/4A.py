x = int(input())
re = ""
if 0<= x <= 2**20:
    while x>0 :
        b = x%2
        x = x//2
        
        re = str(b) + re
    if re == "":
        re = "0"
else : 
    print("Invalid input")
print(re)