import re
import math

f = open("input.txt", "r")
noChars = []
for x in f:
    newStr = re.sub(r'one',"o1e",x)
    newStr = re.sub(r'two',"t2o",newStr)
    newStr = re.sub(r'three',"t3e",newStr)
    newStr = re.sub(r'four',"f4r",newStr)
    newStr = re.sub(r'five',"f5e",newStr)
    newStr = re.sub(r'six',"s6x",newStr)
    newStr = re.sub(r'seven',"s7n",newStr)
    newStr = re.sub(r'eight',"e8t",newStr)
    newStr = re.sub(r'nine',"n9e",newStr)
    noChars.append(re.sub(r'[a-zA-Z\n]', "",newStr))

intList = []
for i in noChars:
    intList.append(int(i[0]+i[-1]))
totalSum = sum(intList)
print(totalSum)