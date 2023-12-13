import re

f = open("input.txt", "r")
indexSum = 0
for index, x in enumerate(f):

    maxGreen = 0
    for y in re.findall(r'\d+ green',x):
        temp = int(re.sub(r' green',"",y))
        if(temp > maxGreen):
            maxGreen = temp

    maxBlue = 0
    for y in re.findall(r'\d+ blue',x):
        temp = int(re.sub(r' blue',"",y))
        if(temp > maxBlue):
            maxBlue = temp

    maxRed = 0
    for y in re.findall(r'\d+ red',x):
        temp = int(re.sub(r' red',"",y))
        if(temp > maxRed):
            maxRed = temp

    indexSum += maxGreen*maxBlue*maxRed

print(indexSum)