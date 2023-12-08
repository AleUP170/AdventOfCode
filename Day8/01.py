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
for x in lines:
    key = re.search(r'[A-Z]+',x).group()
    mappings = re.search(r'\(.+\)',x).group()
    mappings = re.findall(r'[A-Z]+', mappings)
    mapDict[key] = mappings
    
# Iterating through the map with the directions
steps = 0
currKey = 'AAA'
mod = len(directions)
while(True):
    currKey = mapDict[currKey][int(directions[steps%mod])]
    steps += 1
    if currKey == 'ZZZ':
        break

print(steps)