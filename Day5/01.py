import re
import math

f = open("test2.txt", "r")
lines = f.read().splitlines()
f.close()

seeds = []
mapRanges = []

# Dealing with the inputs
seeds = list(map(int,re.findall(r'[\d]+', lines[0])))

lines = lines[3:]
mapTypes = 0

tempRange = []
for x in lines:
    # New type of map starts
    if(re.search(r'map',x)):
        mapRanges.append(tempRange)
        tempRange = []
    else:
        if(len(x) > 0):
            tempRange.append(list(map(int,re.findall(r'[\d]+', x))))
mapRanges.append(tempRange)          

# mapTypes[n] = [destination, origin, range]
seedLocations = []

#Map checking
for x in seeds:
    currentMap = x
    for i in mapRanges:
        print (fr'{currentMap} maps to ', end='')
        for j in i:
            if(j[1] <= currentMap < j[1] + j[2]):
                currentMap = j[0] + (currentMap - j[1])
                break
    print (fr'{currentMap}')
    seedLocations.append(currentMap)

print(min(seedLocations))