def rotate_string(s):
    """Generate all rotations of a given string."""
    return [s[i:] + s[:i] for i in range(len(s))]

def is_same_bracelet(s1, s2):
    """Check if two sequences represent the same bracelet design."""
    # Check if the sequences are already the same
    if s1 == s2:
        return True
    # Check rotational symmetry
    for rotated_s1 in rotate_string(s1):
        if rotated_s1 == s2:
            return True
    # Check reflective symmetry
    reversed_s1 = s1[::-1]
    for rotated_s1 in rotate_string(reversed_s1):
        if rotated_s1 == s2:
            return True
    return False

# Input
seq1 = input().split()
seq2 = input().split()

# Check if they represent the same bracelet design
if is_same_bracelet(seq1, seq2):
    print("same")
else:
    print("different")
