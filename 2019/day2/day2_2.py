intcode = [int(i) for i in open("input.txt", "r").read().split(",")]

for noun in range(100):
    for verb in range(100):
        position = 0
        program = intcode[:]
        program[1] = noun
        program[2] = verb
        while True:
            if position % 4 == 0:
                if program[position] == 99:
                    break
                if program[position] == 1:
                    program[int(program[position+3])] = int(program[int(program[position+1])]) + int(program[int(program[position+2])])
                if program[position] == 2:
                    program[int(program[position+3])] = int(program[int(program[position+1])]) * int(program[int(program[position+2])])
            position += 1
        if program[0] == 19690720:
            print(100 * noun + verb)
            break