input = open("2024\\day02\\input.txt").read().splitlines()

safe = 0

for i in input:
    input_list = list(map(int,i.split(" ")))
    if input_list[0] > input_list[-1]:
        for u in range(len(input_list)):
            if u == len(input_list)-1:
                safe += 1
                break

            if input_list[u] > input_list[u+1] and 1 <= (input_list[u] - input_list[u+1]) <= 3:
                continue
            else:
                break

    elif input_list[0] < input_list[-1]:
        for u in range(len(input_list)):
            if u == len(input_list)-1:
                safe += 1
                break

            if input_list[u] < input_list[u+1] and 1 <= (input_list[u+1] - input_list[u]) <= 3:
                continue
            else:
                break

    input_list = []

print(safe)