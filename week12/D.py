import re

filename = input("Enter a filename: ")
try:
    with open(filename) as f, open('dict.txt') as d:
        dictionary = set(d.read().split())
        
    for i, line in enumerate(f, 1):
        for word in re.findall(r"[a-zA-Z]+", line):
            if word.lower() not in dictionary and len(word) <= 16:
                print(f"Line {i}: {word}") 
except FileNotFoundError:
    print("Error: Cannot open the file")