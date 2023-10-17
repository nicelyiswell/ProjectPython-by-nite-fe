# Step 1: Parsing Input
p = list(map(int, input().split()))
q = list(map(int, input().split()))

# Step 2: Setting Up the Result Polynomial
result = [0] * (len(p) + len(q) - 1)

# Step 3: Calculating the Result Polynomial
for i in range(len(p)):
    for j in range(len(q)):
        result[i+j] += p[i] * q[j]

# Step 4: Output the Result
print(' '.join(map(str, result)))
