'''
rows = int(input())
columns = int(input())
symbol = (input())

for x in range(rows):
    for y in range (columns) :
        print(symbol, end=" ")
    print() #New


import turtle 
nite = turtle.Turtle()
nite.color("cyan", "blue")


nite.forward(100)
nite.left(90)
nite.forward(100) 
nite.left(90)
nite.forward(100)
nite.left(90)
nite.forward(100) 

nite.penup()
nite.forward(100)
nite.pendown() 
nite.forward(100)

nite.left(90)
nite.forward(100) 
nite.left(90)
nite.forward(100)
nite.left(90)
nite.forward(100)



turtle.done()


import turtle 
import math
bob = turtle.Turtle()
bob.color("red", "yellow")
bob.speed(10)

bob.begin_fill()
for i in range(2000):
    bob.forward(math.sin(i/10)*25)
    bob.left(20)
bob.end_fill()

turtle.done() 


for _ in range(6) :
    print("Line" , _ , end=": ")
    for i in range(_): 
        print(i , end=" ")
    print(" ") 

s="kkk"
while s != "":
    s = input()
    if s!= "":
        print("Hello" , s)

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
    
    
min_num = float(input())
max_num = float(input())
while True:
    line = input()
    if line == '$':
        break
    num = int(line)
    min_num = min(min_num, num)
    max_num = max(max_num, num)
if min_num == float('inf'):
    print("Invalid input")
else:
    print(min_num)
    print(max_num)

n= int(input())
for i in range(10):
    print("x"*(i+1)) 
    
n=int(input()) 
for i in range(n):
    print("*"*(i)+ " " + "*"*(n-(i+1)))
    
    
def down(n):
    if n == 0:
        print(n)
    else:
        print(n)
        down(n-1) 

num = int(input())
down(num)


item = int(input())
sum = 0
while item > 0:
    sum += item
    item -= 0.1
print(item)

n = int(input())
print("$"*n)
'''
def find(x):
    diversors=[]
    for i in range(1 , x+1):
        if x % i ==0:
            diversors.append(i)
    return diversors
x = int(input())
diversors = find(x)
print(diversors)
