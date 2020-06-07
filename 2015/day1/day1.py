floorlist = open("input.txt", "r").read()

floor = 0 # Part one

for i in floorlist:
    if i == "(":
        floor += 1
    else:
        floor -= 1

print(floor)

floortwo = 0 # Part two
position = 0

for i in floorlist:
    position += 1
    if i == "(":
        floortwo += 1
    else:
        floortwo -= 1
    if floortwo == (-1):
        break
        
print(position)