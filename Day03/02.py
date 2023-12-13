import re

f = open("input.txt", "r")
numPositions = []
inputList = []

lines = f.read().splitlines()
gearsFound = {}

def FindSymbols(startX:int, startY:int, lenght:int, value:int):
    for i in range(-1,2):
        row = ''
        for j in range(-1,lenght+1):
            if(startY+i >= 0 and startY+i < len(inputList) and startX+j >= 0 and startX+j < len(inputList[startY+i])):
                if(re.match(r'[\*]',inputList[startY+i][startX+j])):
                    key = fr'{startY+i},{startX+j}'
                    if key in gearsFound:
                        gearsFound[key].append(value)
                    else:
                        gearsFound[key] = [value]

for x in lines:
    inputList.append(x)
    tempList = []
    for y in re.finditer(r"\d+",x):
        z = [y.start(), int(y.end()-y.start()), int(y.group())]
        tempList.append(z)
    numPositions.append(tempList)

validGears = []

for index, posRow in enumerate(numPositions):
    for numInfo in posRow:
        FindSymbols(numInfo[0], index, numInfo[1], numInfo[2])

total = 0

for k in gearsFound:
    if len(gearsFound[k]) is 2:
        total += gearsFound[k][0] * gearsFound[k][1]

print(total)