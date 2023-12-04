import re

f = open("input.txt", "r")
numPositions = []
inputList = []

# Save each line into an array for  easier access
lines = f.read().splitlines()

# Checks if a symbol is in a rectangle box around each found digit
def FindSymbols(startX:int, startY:int, lenght:int):
    flag = False
    # Checking the box, making sure not going out of bounds (looping to the other end of the array since python)
    for i in range(-1,2):
        #row = ''
        for j in range(-1,lenght+1):
            if(startY+i >= 0 and startY+i < len(inputList) and startX+j >= 0 and startX+j < len(inputList[startY+i])):
                # Checks for symbols that aren't digits, . and \n 
                if(re.match(r'[^\d\.\n]',inputList[startY+i][startX+j])):
                    flag = True
    return flag

# For every number we find, we store the position and the length (to make the box around it) and the value of the number to add it if it's valid
for x in lines:
    inputList.append(x)
    tempList = []
    # Regex for finding all sequences of digits 
    for y in re.finditer(r"\d+",x):
        z = [y.start(), int(y.end()-y.start()), int(y.group())]
        tempList.append(z)
    numPositions.append(tempList)

validNums = 0

# Adds all the valid numbers found
# numInfo[0] = x position in array, index from the enumeration can be used as y position
# numInfo[1] = length
# numInfo[2] = value
for index, posRow in enumerate(numPositions):
    for numInfo in posRow:
        if(FindSymbols(numInfo[0], index, numInfo[1])):
            validNums+=numInfo[2]

print(validNums)