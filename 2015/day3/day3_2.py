direction = open("input.txt", "r").read()
santaX = 0
santaY = 0
roboX = 0
roboY = 0
coord = []
turn = 0

for i in direction:
    coord.append(str(santaX) + "," + str(santaY))
    coord.append(str(roboX) + "," + str(roboY))
    if turn == 0:
        if i == ">":
            santaX += 1
        elif i == "<":
            santaX -= 1
        elif i == "^":
            santaY += 1
        elif i == "v":
            santaY -= 1
        turn += 1
    elif turn == 1:
        if i == ">":
            roboX += 1
        elif i == "<":
            roboX -= 1
        elif i == "^":
            roboY += 1
        elif i == "v":
            roboY -= 1
        turn -= 1

uniquecoord = set(coord)
print(len(uniquecoord))