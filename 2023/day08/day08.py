import re

input_list = open("input.txt").read().splitlines()
node_list = {}
direction = list(input_list[0])
curr = "AAA"
steps = 0

for i in input_list[2:]:
    a = re.split(r"[\W]+", i)
    node_list[a[0]] = (a[1], a[2])

while (True):
    for u in direction:
        steps += 1
        node_tuple = node_list.get(curr)
        if u == "L":
            curr = node_tuple[0]
        else:
            curr = node_tuple[1]

        if curr == "ZZZ":
            break
    
    else:
        continue
    break

print(steps)

    

