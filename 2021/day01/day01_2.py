depth = open("input.txt", "r").readlines()
increase = 0
depthlist = []
groupA = 0
groupB = 0

for i in depth:
    depthlist.append(i)

while len(depthlist) > 3:
    groupA = int(depthlist[0]) + int(depthlist[1]) + int(depthlist[2])
    groupB = int(depthlist[1]) + int(depthlist[2]) + int(depthlist[3])
    if groupA < groupB:
        increase += 1
    depthlist = depthlist[1:]

print(increase)