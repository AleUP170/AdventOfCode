import re
import math

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

inputs = []
for x in lines:
    inputs.append(list(map(int,re.findall(r'[-]*[\d]+', x))))

# Brute forcing each input
total = 0
for x in inputs:
    # New list to store each new step
    steps = []
    steps.append(x)
    end = False
    iteration = 0
    while(not end):
        currStep = []
        totalCheck = 0
        for y in range(0, len(steps[iteration])-1):
            temp = steps[iteration][y+1] - steps[iteration][y]
            totalCheck += abs(temp) # If this adds up to 0 we know all elements in the current step are 0 and thus we end
            currStep.append(temp)
        steps.append(currStep)
        iteration += 1
        if(totalCheck == 0):
            end = True

    # We have all steps, just need to find the next value in the first one
    # Reversing it makes it easier
    steps.reverse()
    # Add a 0 to the last (now first) element
    steps[0].append(0)
    for y in range(0, len(steps)-1):
        temp = steps[y][-1] + steps[y+1][-1]
        steps[y+1].append(temp)
    total += steps[-1][-1]

print(total)