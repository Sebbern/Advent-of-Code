intcode = [int(i) for i in open("input.txt", "r").read().split(",")]
position = 0

intcode[1] = 12
intcode[2] = 2

while True:
    if position % 4 == 0:
        if intcode[position] == 99:
            print(intcode[0])
            break
        if intcode[position] == 1:
            intcode[int(intcode[position+3])] = int(intcode[int(intcode[position+1])]) + int(intcode[int(intcode[position+2])])
        if intcode[position] == 2:
            intcode[int(intcode[position+3])] = int(intcode[int(intcode[position+1])]) * int(intcode[int(intcode[position+2])])
    position += 1