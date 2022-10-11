bingo_subsystem = open("input.txt", "r").read().split()
bingo_numbers = bingo_subsystem[0]
bingo_numbers = bingo_numbers.split(",")
bingo_boards = bingo_subsystem[1:]
bingo_count = 0
idx = 0
fixed_bingo_boards = []
winning_sum = 0
winning_boards = 0
last_winning_board = []
discarded_boards = []

for x in range(100):
    fixed_bingo_boards.append([])

for i in bingo_boards:
    fixed_bingo_boards[idx].append(i)
    if len(fixed_bingo_boards[idx]) == 25:
        idx += 1

while True:
    idx = 0
    for i in fixed_bingo_boards:
        for u in str(i).split(","):
            u = u.strip(" '[] ")
            if u == bingo_numbers[bingo_count]:
                fixed_bingo_boards[idx] = ["*" if x == u else x for x in fixed_bingo_boards[idx]]
        idx += 1

    bingo_count += 1
    if bingo_count > 99:
        break

    if bingo_count > 5:
        for x in range(100):
            for y in range(0, 25, 5):
                if fixed_bingo_boards[x][y] == fixed_bingo_boards[x][y+1] == fixed_bingo_boards[x][y+2] == fixed_bingo_boards[x][y+3] == fixed_bingo_boards[x][y+4]:
                    if x not in discarded_boards and len(discarded_boards) < 99:
                        winning_boards += 1
                        discarded_boards.append(x)

                    if x not in discarded_boards and len(discarded_boards) == 99:
                        last_winning_board = fixed_bingo_boards[x]
                        break

            for y in range(0,5,1):
                if fixed_bingo_boards[x][y] == fixed_bingo_boards[x][y+5] == fixed_bingo_boards[x][y+10] == fixed_bingo_boards[x][y+15] == fixed_bingo_boards[x][y+20]:
                    if x not in discarded_boards and len(discarded_boards) < 99:
                        winning_boards += 1
                        discarded_boards.append(x)

                    if x not in discarded_boards and len(discarded_boards) == 99:
                        last_winning_board = fixed_bingo_boards[x]
                        break

            else:
                continue
            break

        else:
            continue
        break

for i in last_winning_board:
    if str(i)[0].isdigit():
        winning_sum += int(i)

winning_sum = winning_sum * int(bingo_numbers[bingo_count-1])

print(winning_sum)