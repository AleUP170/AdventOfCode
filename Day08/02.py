import re
import math

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

# Getting directions, turning L to 0 and R to 1
directions = re.sub(r'L','0',lines[0])
directions = re.sub(r'R','1',directions)

lines = lines[2:]
# Getting key: [value1, value2] from each line
mapDict = {}
startA = []
for x in lines:
    key = re.search(r'[A-Z]+',x).group()
    mappings = re.search(r'\(.+\)',x).group()
    mappings = re.findall(r'[A-Z]+', mappings)
    mapDict[key] = mappings
    # Get keys that end with A
    if re.match(r'..A',key):
        startA.append(key)

print(startA)

# Iterating through the map with the directions
steps = 0
currentKeys=startA
mod = len(directions)
stepsList = [None] * len(currentKeys)
# Bruteforcing would take too long and it can't really be parallelized
# Thankfully the input is set up so that the length of the first loop
# (from xxA to xxZ) is the same and subsequent loops of xxZ to xxZ
# This isn't obvious unless you print a couple loops (which is kinda bad from a design perspective imo)
while(True):
    for i,k in enumerate(currentKeys):
        currKey = mapDict[k][int(directions[steps%mod])]
        currentKeys[i] = currKey
        if re.match(r'..Z',currKey):
            stepsList[i] = steps + 1
    steps += 1
    if None not in stepsList:
        break

# Since we know the length of each loop we can just find the least common multiplier
total = math.lcm(*stepsList)
print(total)