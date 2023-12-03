import re

f = open("input.txt", "r")
numPositions = []
inputList = []

lines = f.read().splitlines()

def FindSymbols(startX:int, startY:int, lenght:int):
    flag = False
    for i in range(-1,2):
        row = ''
        for j in range(-1,lenght+1):
            if(startY+i >= 0 and startY+i < len(inputList) and startX+j >= 0 and startX+j < len(inputList[startY+i])):
                if(re.match(r'[^\d\.\n]',inputList[startY+i][startX+j])):
                    flag = True
    return flag

for x in lines:
    inputList.append(x)
    tempList = []
    for y in re.finditer(r"\d+",x):
        z = [y.start(), int(y.end()-y.start()), int(y.group())]
        tempList.append(z)
    numPositions.append(tempList)

validNums = 0

for index, posRow in enumerate(numPositions):
    for numInfo in posRow:
        if(FindSymbols(numInfo[0], index, numInfo[1])):
            validNums+=numInfo[2]

print(validNums)