import re
import math

f = open("input.txt", "r")

lines = f.read().splitlines()
winningNums = []
cardNums = []
total = 0

def GetMatches(wNums, cNums):
    matches = 0
    for x in cNums:
        if x in wNums:
            matches += 1
    return matches


for x in lines:
    y = re.sub(r'Card[\s]+[\d]+: ',"",x).split(" | ")
    #print(list(map(int,re.findall(r'[\d]+',y[0]))))
    #print(re.findall(r'[\d]+',y[1]))
    winningNums.append(list(map(int,re.findall(r'[\d]+',y[0]))))
    cardNums.append(list(map(int,re.findall(r'[\d]+',y[1]))))

matchNum = []
copyNum = [1] * len(winningNums)

for i,x in enumerate(cardNums):
    matchNum.append(GetMatches(winningNums[i],x))

for i, x in enumerate(matchNum):
    for k in range (0, copyNum[i]):
        for j in range(i,x+i):
            copyNum[j+1] += 1

print(sum(copyNum))

print(matchNum)
print(copyNum)
#print(cardNums)