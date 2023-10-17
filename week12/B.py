filename = input("Enter a filename: ")
try:
    with open(filename) as f:
        print(f.read())
except FileNotFoundError:
    print("ERROR: File not found")