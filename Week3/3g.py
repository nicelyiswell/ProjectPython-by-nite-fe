n = int(input())  # TODO: Get the input

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            row = "(" + str(i) + "," + str(j) + "," + str(k) + ")"
            print(row)