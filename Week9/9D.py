
list=[] 
count_list =0
while True:
    n = input()
    if n =="$":
        break
    else: 
        list.append(int(n))
        list.sort()  
        count_list = len(list)
if count_list%2 == 1:
    print(float(list[count_list // 2]))
else: 
    print(float((list[count_list // 2 - 1 ] + list[count_list // 2]) / 2.0 ))
            

        
