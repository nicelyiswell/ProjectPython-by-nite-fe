n = int(input())

if n > 1 :
    x=[]
    for i in range(0,n):
        _in = input()
        _split = _in.split()
        x.append([int(_split[0]),int(_split[1])])

        x_min = min(x, key=lambda p: p[0])[0]
        x_max = max(x, key=lambda p: p[0])[0]
        y_min = min(x, key=lambda p: p[1])[1]
        y_max = max(x, key=lambda p: p[1])[1]

        _find = max(x_max-x_min,y_max-y_min)
        _square = _find**2

        print(_square)