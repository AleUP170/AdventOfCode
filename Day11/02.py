import re
import math

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

# time to clean up the code from last part lol
# get coordinates of all #

distance = 1000000
coords = []
for i,x in enumerate(lines):
    for j,y in enumerate(x):
        if(y == '#'):
            tup = [i,j]
            coords.append(tup)

# go through lines, if row has no # add distance to 1st coordinate of every subsequent #
currMultiplier = 0
print(coords)
cordMults = []
for x in lines:
    if '#' not in x:
        currMultiplier += distance - 1
    cordMults.append(currMultiplier)

# tranversing in reverse order to avoid weird stuff
for x in range(len(cordMults)-1,-1,-1):
    for y in coords:
        if y[0] == x:
            y[0] += cordMults[x]

print(coords)    

# Transposes list
currMultiplier = 0
lines = list(map(list, zip(*lines)))
cordMults = []
for x in lines:
    if '#' not in x:
        currMultiplier += distance - 1
    cordMults.append(currMultiplier)

# tranversing in reverse order to avoid weird stuff
for x in range(len(cordMults)-1,-1,-1):
    for y in coords:
        if y[1] == x:
            y[1] += cordMults[x]
print(coords)

# for each pair just get the taxicab distance between them
total = 0
for i,x in enumerate(coords):
    for j in range(i+1,len(coords)):
        sub = abs(coords[j][0] - x[0]) + abs((coords[j][1] - x[1]))
        total += sub

print(total)