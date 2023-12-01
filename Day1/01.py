import re
import math

f = open("input.txt", "r")

noChars = []
for x in f:
    noChars.append(re.sub(r'[a-zA-Z\n]', "",x))
intList = []
for i in noChars:
    intList.append(int(i[0]+i[-1]))
totalSum = sum(intList)
print(totalSum)