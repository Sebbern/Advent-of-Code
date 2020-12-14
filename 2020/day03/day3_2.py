slope = open("input.txt", "r").read().splitlines()
directions = [(1,1), (3,1), (5,1), (7,1), (1,2)]

x = 0
y = 0
tree = 0
treemultiply = 1

for (i,u) in directions:
    x = 0
    y = 0
    tree = 0
    while y < len(slope):
        if slope[y][x % len(slope[0])] == "#":
            tree += 1

        x += i
        y += u

    treemultiply *= tree

print(treemultiply)