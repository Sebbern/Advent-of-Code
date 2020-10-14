intcode = open("input.txt", "r").read().split(",")
position = 0

intcode[1] = 12
intcode[2] = 2

for i in intcode:
    i = int(i)
    if position % 4 == 0:
        if i == 99:
            print(intcode[0])
            break
        if i == 1:
            intcode[int(intcode[position+3])] = int(intcode[int(intcode[position+1])]) + int(intcode[int(intcode[position+2])])
        if i == 2:
            intcode[int(intcode[position+3])] = int(intcode[int(intcode[position+1])]) * int(intcode[int(intcode[position+2])])
    position += 1