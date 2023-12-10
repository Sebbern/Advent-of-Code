import re
import math

input_list = open("input.txt").read().splitlines()
node_dict = {}
direction = list(input_list[0])
test = False
steps = 0
ghost_list = []
math_list = []
loop_list = []
max_steps = 1

for i in input_list[2:]:
    a = re.split(r"[\W]+", i)
    node_dict[a[0]] = (a[1], a[2])

for x in node_dict:
    if x[-1] == "A":
        ghost_list.append(x)

for i in range(len(ghost_list)*2):
    math_list.append("")

for i in range(len(ghost_list)):
    loop_list.append("")

while (True):
    for u in direction:
        steps += 1
        index = 0
        for p in ghost_list:
            if p[-1] == "Z" and math_list[index] != "" and loop_list[index] == "":
                loop_list[index] = steps - math_list[index+len(ghost_list)]
            
            if p[-1] == "Z" and math_list[index] == "":
                math_list[index] = p
                math_list[index+len(ghost_list)] = steps

            node_tuple = node_dict.get(p)
            if u == "L":
                ghost_list[index] = node_tuple[0]
            else:
                ghost_list[index] = node_tuple[1]
            
            index += 1

        if "" not in loop_list:
            for c in loop_list:
                max_steps = math.lcm(c,max_steps)
            print(max_steps)
            break

    else:
        continue
    break