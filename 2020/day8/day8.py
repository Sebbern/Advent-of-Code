boot = open("input.txt", "r").read().splitlines()

acc = 0
idx = 0
idxlist = [0]
op = boot[idx]

while True:
    instruction, count = op.split()
    if instruction == "nop":
        idx += 1
        op = boot[idx]
    elif instruction == "jmp":
        idx += int(count)
        op = boot[idx]
    elif instruction == "acc":
        acc += int(count)
        idx += 1

    if idx in idxlist:
        break

    idxlist.append(idx)
    op = boot[idx]
    
print(acc)