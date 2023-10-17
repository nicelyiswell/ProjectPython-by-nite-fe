import math

min_so_far = math.inf
max_so_far = -math.inf

num_entered = False

while True:
    input_ = input()

    if input_ == "$":
        break

    integer = int(input_)
    num_entered = True 

   
    if integer < min_so_far:
        min_so_far = integer

   
    if integer > max_so_far:
        max_so_far = integer

if input_ == "$" :
    print(min_so_far)
    print(max_so_far)
else:
    print("Invalid input")