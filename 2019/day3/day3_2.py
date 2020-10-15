direction = open("input.txt")
wire1 = ["0,0"]
wire1x = 0
wire1y = 0
wire2 = ["0,0"]
wire2x = 0
wire2y = 0
cross = 0
steps = []

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
indices_A = [wire1.index(x) for x in cross]
indices_B = [wire2.index(x) for x in cross]

for a, b in zip(indices_A, indices_B):
    steps.append(a+b)
    
print(min([x for x in steps if x != 0]))