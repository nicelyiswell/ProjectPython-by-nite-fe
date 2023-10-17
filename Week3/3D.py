sum_so_far = 0
while True:
    n = (input())
    if n == '$':
        print(sum_so_far)
        break 
    n = int(n)
    if  n  <= 0 :
        sum_so_far += n
        continue
    sum_so_far += n