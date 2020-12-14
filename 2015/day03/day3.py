direction = open("input.txt", "r").read()
x = 0
y = 0
coord = []

for i in direction:
    coord.append(str(x) + "," + str(y))
    if i == ">":
        x += 1
    elif i == "<":
        x -= 1
    elif i == "^":
        y += 1
    elif i == "v":
        y -= 1

uniquecoord = set(coord)
print(len(uniquecoord))
