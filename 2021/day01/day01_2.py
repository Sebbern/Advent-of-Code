depth = open("input.txt", "r").read().splitlines()
increase = 0
groupA = 0
groupB = 0

while len(depth) > 3:
    groupA = int(depth[0]) + int(depth[1]) + int(depth[2])
    groupB = int(depth[1]) + int(depth[2]) + int(depth[3])
    if groupA < groupB:
        increase += 1
    depth = depth[1:]

print(increase)