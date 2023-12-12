import re
import math

f = open("test.txt", "r")
lines = f.read().splitlines()
f.close()

newLines = []

for x in lines:
    newLines.append(x)
    # Append again
    if '#' not in x:
        newLines.append(x)

# Transposes list
lines = list(map(list, zip(*newLines)))

newLines = []

for x in lines:
    y = ''.join(x)
    newLines.append(y)
    # Append again
    if '#' not in y:
        newLines.append(y)


# Transpose back
lines = list(map(list, zip(*newLines)))

newLines = []

for x in lines:
    y = ''.join(x)
    newLines.append(y)

lines = newLines

# that was a mess
# next part is easy

# get coordinates of all #

coords = []
for i,x in enumerate(lines):
    for j,y in enumerate(x):
        if(y == '#'):
            tup = (i,j)
            coords.append(tup)

# for each pair just get the taxicab distance between them
total = 0
for i,x in enumerate(coords):
    for j in range(i+1,len(coords)):
        sub = abs(coords[j][0] - x[0]) + abs((coords[j][1] - x[1]))
        total += sub

print(total)