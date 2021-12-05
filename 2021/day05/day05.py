coordinates = open("input.txt", "r").read().splitlines()
lines = []

for i in coordinates:
    a, b = i.split("->")
    a, b = a.strip(" "), b.strip(" ")
    x1, y1 = a.split(",")
    x2, y2 = b.split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    while (str(x1)+","+str(y1)) != (str(x2)+","+str(y2)):
        if x1 != x2 and y1 == y2:
            lines.append (str(x1)+","+str(y1))
            while x1 != x2:
                if x1 > x2:
                    x1 = int(x1) - 1
                    
                elif x1 < x2:
                    x1 = int(x1) + 1

                lines.append (str(x1)+","+str(y1))

        elif x1 == x2 and y1 != y2:
            lines.append (str(x1)+","+str(y1))
            while y1 != y2:
                if y1 > y2:
                    y1 = int(y1) - 1
                    
                elif y1 < y2:
                    y1 = int(y1) + 1

                lines.append (str(x1)+","+str(y1))

        break

counted_coords = []
overlap = 0

for i in lines:
    if i not in counted_coords:
        if lines.count(i) > 1:
            overlap += 1

        counted_coords.append(i)

print(overlap) # Takes 3 minutes to run