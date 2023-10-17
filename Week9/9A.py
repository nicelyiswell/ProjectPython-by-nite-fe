import math

seqeuence = []
while True:
    line = input()
    if line=="$":
        break
    else:
        seqeuence.append(int(line))
n = len(seqeuence)

mean = sum(seqeuence)/n

sum_squated_diff = sum((x-mean)**2 for x in seqeuence)
variance = sum_squated_diff/n
std_deviation = math.sqrt(variance)
print (round(std_deviation ,2))
