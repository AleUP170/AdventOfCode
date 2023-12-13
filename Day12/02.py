from functools import cache

# Was completely stumped with this one, shoutouts to u/AllanTaylor314 for the breakdown of the logic

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

# oh boy 1D picross
inputs = []
# get inputs
for x in lines:
    springs, groups = x.split()
    groups = tuple(map(int, groups.split(',')))
    inputs.append((springs,groups))

# time to learn functools i guess
# i hate recursion
@cache
def checkValid(springs, groups, count = 0):
    # reached end of spring list
    if not springs:
        # quick check if current group size is still valid
        lasG = len(groups)
        # current run is same size as last group or there's no current run and no remaining groups
        if ((lasG == 1 and groups[0] == count) or (lasG == 0 and count == 0)):
            return 1
        # not valid, end
        return 0

    
    currSpring = springs[0]
    springs = springs[1:]
    # getting current group, making a new tuple with the rest, checks in case of end of list of groups
    currGroup, *newGroups = groups or [0]
    newGroups = tuple(newGroups)
    
    # recursively call, with the two possible options of ?
    if currSpring == '?':
        return checkValid('#'+springs, groups, count) + checkValid('.'+springs, groups, count)
    
    # counting runs of #
    if currSpring == '#':
        # overshot, not valid, exit recursion
        if count == currGroup:
            return 0
        # still valid
        else:
            return checkValid(springs, groups, count+1)
    
    # check if we have to move onto the next group
    if currSpring == '.':
        # haven't found a new group yet, keep going
        if count == 0:
            return checkValid(springs, groups, 0)
        # reached end of group, still valid, keep going with new remaining groups
        if count == currGroup:
            return checkValid(springs, newGroups, 0)
        # reached end of group, incorrect size, invalid, end recursion
        return 0

# unfolding
unfoldedInputs = []
# fancy python list operations
for x in inputs:
    unfoldedInputs.append(('?'.join([x[0]]*5), x[1]*5))


total = 0
for x in unfoldedInputs:
    total += checkValid(x[0],x[1])

print(total)