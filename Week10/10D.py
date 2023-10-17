def longest_stutter(seq):
    if not seq:
        return 0

    current_number = seq[0]
    current_length = 1
    max_length = 1

    for num in seq[1:]:
        if num == current_number:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1
            current_number = num

    if current_length > max_length:
        max_length = current_length
        
    return max_length


# Read input sequence
sequence = []
while True:
    line = input()
    if line == '$':
        break
    sequence.append(int(line))

# Compute and print the result
print(longest_stutter(sequence))
