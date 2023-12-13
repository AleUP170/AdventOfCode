import re
import math

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

seeds = []
mapRanges = []
seedRanges = []

# Dealing with the inputs
seeds = list(map(int,re.findall(r'[\d]+', lines[0])))
for x in range(0,len(seeds),2):
    seedRanges.append([seeds[x],seeds[x+1]])

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

# Doing it in reverse
mapRanges.reverse()

#Map checking
x = -1
found = False
while(not found):
    x += 1
    currentMap = x
    for i in mapRanges:
        for j in i:
            if(j[0] <= currentMap < j[0] + j[2]):
                currentMap = j[1] + (currentMap - j[0])
                break
    # Checking if seed is in any starting range

    for i in seedRanges:
        #print (f"Checking if {x} which maps to {currentMap} is in {i[0]} to {i[0] + i[1] - 1}")
        if(i[0] <= currentMap < i[0] + i[1]):
            found = True

    #print (currentMap)

print(x)
#print(min(seedLocations))