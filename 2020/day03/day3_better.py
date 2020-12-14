slope = open("input.txt", "r").read().splitlines()

x = 0
y = 0
tree = 0

while y < len(slope):
    if slope[y][x % len(slope[0])] == "#":
        tree += 1

    y += 1
    x += 3

print(tree)