boot = open("input.txt", "r").read().splitlines()

acc = 0
idx = 0
idxlist = [0]
op = boot[idx]
checkforerror = 0

while True:
    instruction, count = op.split()
    if instruction == "nop":
        if checkforerror == 0:
            originalinstruction, originalcount, originalidxlist, originalidx, originalacc = instruction, count, idxlist.copy(), idx, acc
            checkforerror = 1
            instruction = "jmp"
            idx += int(count)
        else:
            idx += 1

    elif instruction == "jmp":
        if checkforerror == 0:
            originalinstruction, originalcount, originalidxlist, originalidx, originalacc = instruction, count, idxlist.copy(), idx, acc
            checkforerror = 1
            instruction = "nop"
            idx += 1
        else:
            idx += int(count)

    elif instruction == "acc":
        acc += int(count)
        idx += 1
    
    if idx in idxlist:
        instruction, count, idxlist, idx, acc = originalinstruction, originalcount, originalidxlist.copy(), originalidx, originalacc
        checkforerror = 0
        if instruction == "nop":
            idx += 1
        elif instruction == "jmp":
            idx += int(count)

    idxlist.append(idx)
    op = boot[idx]

    if idx == (len(boot) - 1):
        break

print(acc)