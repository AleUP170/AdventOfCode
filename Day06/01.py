import re
import math

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

timeList = list(map(int,re.findall(r'[\d]+', lines[0])))
distList = list(map(int,re.findall(r'[\d]+', lines[1])))

total = 1

# Simple math for this problem
for x,y in zip(timeList,distList):
    # Only really need to check half of the times since winning times are symmetrical 
    lowBound = 0
    for lowBound in range(math.ceil(x/2)):
        if lowBound * (x-lowBound) > y:
            break
    # Somehow getting an off by one error on all bound lengths so just adding 1 to each lol
    total *= (x - 2*lowBound)+1

print(total)