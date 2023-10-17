with open('input.txt', 'r') as f, open('output.txt', 'w') as out:
    for line in f:
        out.write(line.capitalize())
