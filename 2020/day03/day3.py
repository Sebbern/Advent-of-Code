slope = open("input.txt", "r").read().splitlines()

x = 0
y = 0
tree = 0
row = 0

while y < len(slope) - 1:
    y += 1
    row = slope[y]
    x += 3

    if x >= len(slope[0]):
        x -= len(slope[0])

    if row[x] == "#":
        tree += 1

print(tree)