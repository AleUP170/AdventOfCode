import re

f = open("input.txt", "r")
indexSum = 0
for index, x in enumerate(f):
    flag = False
    for y in re.findall(r'\d+ green',x):
        temp = int(re.sub(r' green',"",y))
        if(temp > 13):
            flag = True

    for y in re.findall(r'\d+ blue',x):
        temp = int(re.sub(r' blue',"",y))
        if(temp > 14):
            flag = True

    for y in re.findall(r'\d+ red',x):
        temp = int(re.sub(r' red',"",y))
        if(temp > 12):
            flag = True

    if(not flag):
        indexSum += index + 1

print(indexSum)