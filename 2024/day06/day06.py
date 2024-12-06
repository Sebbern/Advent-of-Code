input = open("2024\\day06\\input.txt").read().splitlines()  

def string_change(str, index, input):
    row = list(str)
    row[index] = input
    str = ''.join(row)
    return str

direction_dict = {"^":">", ">":"v", "v":"<", "<":"^"}
move_dict = {"^":-1, ">":+1, "v":+1, "<":-1}
y = 0
x = 0
direction = "^"

for i in input:
    for u in i:
        if u == "^":
            break
        x += 1
    else:
        y += 1
        x = 0
        continue
    break

while True:
    if direction == "^" or direction == "v":
        if (y+move_dict[direction]) == -1 or (y+move_dict[direction]) == len(input):
            break
        if input[y+move_dict[direction]][x] == "#":
            direction = direction_dict[direction]
        else:
            input[y] = string_change(input[y],x,"X")
            y += move_dict[direction]
            input[y] = string_change(input[y],x,direction)
    
    elif direction == ">" or direction == "<":
        if (x+move_dict[direction]) == -1 or (x+move_dict[direction]) == len(input[y]):
            break
        if input[y][x+move_dict[direction]] == "#":
            direction = direction_dict[direction]
        else:
            input[y] = string_change(input[y],x,"X")
            x += move_dict[direction]
            input[y] = string_change(input[y],x,direction)

input[y] = string_change(input[y],x,"X")


count = 0

#Printing a map as well as the answer
for i in input:
    for u in i:
        if u == "X":
            count += 1
    print(i)

print(count)
