nav = open("input.txt", "r").read().splitlines()

x = 0
y = 0
direction = 2 # 1 north, 2 east, 3 south, 4 west

for i in nav:
    a = i[0]
    b = int(i[1:])

    if a == "N":
        y += b
    elif a == "S":
        y -= b
    elif a == "E":
        x += b
    elif a == "W":
        x -= b
    elif a == "L":
        if b == 90:
            direction -= 1
        elif b == 180:
            direction -= 2
        elif b == 270:
            direction -= 3

        if direction == 0:
            direction = 4
        elif direction == -1:
            direction = 3
        elif direction == -2:
            direction = 2
    elif a == "R":
        if b == 90:
            direction += 1
        elif b == 180:
            direction += 2
        elif b == 270:
            direction += 3

        if direction == 5:
            direction = 1
        elif direction == 6:
            direction = 2
        elif direction == 7:
            direction = 3
    elif a == "F":
        if direction == 1:
            y += b
        elif direction == 2:
            x += b
        elif direction == 3:
            y -= b
        elif direction == 4:
            x -= b

print (abs(x) + abs(y))