direction = open("input.txt")
wire1 = []
wire1x = 0
wire1y = 0
wire2 = []
wire2x = 0
wire2y = 0
cross = 0
closestcross = []

for line, i in enumerate(direction):
    if line == 0:
        for u in i.split(","):
            if u[0] == "U":
                u = u[1:]
                while int(u) > 0:
                    wire1y += 1
                    u = int(u) - 1
                    wire1.append(str(wire1x) + "," + str(wire1y))

            elif u[0] == "D":
                u = u[1:]
                while int(u) > 0:
                    wire1y -= 1
                    u = int(u) - 1
                    wire1.append(str(wire1x) + "," + str(wire1y))

            elif u[0] == "R":
                u = u[1:]
                while int(u) > 0:
                    wire1x += 1
                    u = int(u) - 1
                    wire1.append(str(wire1x) + "," + str(wire1y))

            elif u[0] == "L":
                u = u[1:]
                while int(u) > 0:
                    wire1x -= 1
                    u = int(u) - 1
                    wire1.append(str(wire1x) + "," + str(wire1y))

    elif line == 1:
        for u in i.split(","):
            if u[0] == "U":
                u = u[1:]
                while int(u) > 0:
                    wire2y += 1
                    u = int(u) - 1
                    wire2.append(str(wire2x) + "," + str(wire2y))

            elif u[0] == "D":
                u = u[1:]
                while int(u) > 0:
                    wire2y -= 1
                    u = int(u) - 1
                    wire2.append(str(wire2x) + "," + str(wire2y))

            elif u[0] == "R":
                u = u[1:]
                while int(u) > 0:
                    wire2x += 1
                    u = int(u) - 1
                    wire2.append(str(wire2x) + "," + str(wire2y))

            elif u[0] == "L":
                u = u[1:]
                while int(u) > 0:
                    wire2x -= 1
                    u = int(u) - 1
                    wire2.append(str(wire2x) + "," + str(wire2y))

cross = set(wire1).intersection(wire2)
for i in cross:
    a, b = i.split(",")
    a, b = abs(int(a)), abs(int(b))
    closestcross.append((a+b))
    
print(min(closestcross))