intcode = [int(i) for i in open("input.txt", "r").read().split(",")]
position = 0
program = intcode[:]

while True:
    opcode = program[position] % 100
    mode1 = (program[position] // 100) % 10
    mode2 = (program[position] // 1000) % 10
    mode3 = (program[position] // 10000) % 10
    value1 = 0
    value2 = 0

    if opcode == 99:
        break

    if opcode == 1:
        value1 = int(program[int(program[position+1])]) if mode1 == 0 else int(program[position+1])
        value2 = int(program[int(program[position+2])]) if mode2 == 0 else int(program[position+2])
        program[int(program[position+3])] = value1 + value2
        position += 4

    if opcode == 2:
        value1 = int(program[int(program[position+1])]) if mode1 == 0 else int(program[position+1])
        value2 = int(program[int(program[position+2])]) if mode2 == 0 else int(program[position+2])
        program[int(program[position+3])] = value1 * value2
        position += 4

    if opcode == 3:
        program[int(program[position+1])] = int(input("Enter 1 for part 1 or 5 for part 2: "))
        position += 2

    if opcode == 4:
        value1 = int(program[int(program[position+1])]) if mode1 == 0 else int(program[position+1])
        print(value1)
        position += 2

    if opcode == 5:
        value1 = int(program[int(program[position+1])]) if mode1 == 0 else int(program[position+1])
        value2 = int(program[int(program[position+2])]) if mode2 == 0 else int(program[position+2])
        if value1 != 0:
            position = value2
        else:
            position += 3

    if opcode == 6:
        value1 = int(program[int(program[position+1])]) if mode1 == 0 else int(program[position+1])
        value2 = int(program[int(program[position+2])]) if mode2 == 0 else int(program[position+2])
        if value1 == 0:
            position = value2
        else:
            position += 3

    if opcode == 7:
        value1 = int(program[int(program[position+1])]) if mode1 == 0 else int(program[position+1])
        value2 = int(program[int(program[position+2])]) if mode2 == 0 else int(program[position+2])
        if value1 < value2:
            program[int(program[position+3])] = 1

        else:
            program[int(program[position+3])] = 0
        position += 4

    if opcode == 8:
        value1 = int(program[int(program[position+1])]) if mode1 == 0 else int(program[position+1])
        value2 = int(program[int(program[position+2])]) if mode2 == 0 else int(program[position+2])
        if value1 == value2:
            program[int(program[position+3])] = 1
        else:
            program[int(program[position+3])] = 0
        position += 4