import re
import math

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

hands = []

for x in lines:
    temp = []
    temp.append(re.search(r'[\dAKQJT]+', x).group())
    temp.append(int(re.search(r' [\d]+', x).group()))
    hands.append(temp)

# matches[0] = five of a kind
# matches[1] = four of a kind
# matches[2] = full house
# matches[3] = three of a kind
# matches[4] = two pairs
# matches[5] = one pair
# matches[6] = highest card

matches = [[],[],[],[],[],[],[]]

# Find matches
for x in hands:
    count = {}
    # Count each instance of a card
    for i in x[0]:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # Sort hand into different categories
    # I realized that you can multiply every number of matches and get a different number for each category
    value = 1
    for i in count:
        value *= count[i]

    # Wow python finally added switch-cases
    match value:
        case 1:
            matches[6].append(x)
        case 2:
            matches[5].append(x)
        case 3:
            matches[3].append(x)
        # The only exception is when it's 4, which could be either two pairs or 4 of a kind
        case 4:
            if(len(count) == 2):
                matches[1].append(x)
            else:
                matches[4].append(x)
        case 5:
            matches[0].append(x)
        case 6:
            matches[2].append(x)
        case _:
            print("oh no")

convertedMatches = []

# Turning into numbers and ordering each category
for x in matches:
    temp = []
    for i in x:
        # Substituting T J Q K A with A B C D E for ordering later
        y = re.sub(r'A',r'E',i[0])
        y = re.sub(r'T',r'A',y)
        y = re.sub(r'J',r'B',y)
        y = re.sub(r'Q',r'C',y)
        y = re.sub(r'K',r'D',y)
        temp.append([int(y,16),i[1]])
    temp.sort()
    temp.reverse()
    print(temp)
    for i in temp:
        convertedMatches.append(i)

print(convertedMatches)

total = 0
for x in range(0,len(convertedMatches)):
    total += (convertedMatches[x][1] * (len(convertedMatches)-x))

print(total)