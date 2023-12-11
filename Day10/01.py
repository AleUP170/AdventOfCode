import re
import math

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

# Find starting coordinate
coords = [0,0]
for i,x in enumerate(lines):
    if "S" in x:
        coords[0] = i
        coords[1] = x.index("S")

# Tranversing the maze 
# Cheated in a little and noticed there is only two directions connecting to S in a valid way
# I also assume all pipes in the main path lead to other valid pipes
# 0 - down to up, 1 up to down, 2 left to right, 3 right to left, my starting direction can be either 0 or 1 from my input
# Needed to know which entrance you"re going in for each character
direction = 0
steps = 0
currTile = lines[coords[0]][coords[1]]
while(True):
    steps += 1
    print(direction)
    match currTile:
        # These tiles don"t change direction
        case "|" | "S":
            if direction == 0:
                coords[0] -= 1
            else:
                coords[0] += 1
        case "-":
            if direction == 2:
                coords[1] += 1
            else:
                coords[1] -= 1
        case "L": 
            if direction == 1:
                coords[1] += 1
                direction = 2
            else:
                coords[0] -= 1
                direction = 0
        case "J": # ┘ should"ve been better
            if direction == 1:
                coords[1] -= 1
                direction = 3
            else:
                coords[0] -= 1
                direction = 0
        case "7": # ┐ 
            if direction == 0:
                coords[1] -= 1
                direction = 3
            else:
                coords[0] += 1
                direction = 1
        case "F" : # ┌
            if direction == 0:
                coords[1] += 1
                direction = 2
            else:
                coords[0] += 1
                direction = 1
        case _:
            print("?")
    currTile = lines[coords[0]][coords[1]]
    if(currTile == "S" or currTile == '.'):
        print(direction)
        print(coords)
        break

print(math.ceil(steps/2))