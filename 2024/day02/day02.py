input = open("2024\\day02\\input.txt").read().splitlines()

safe = 0

for i in input:
    input_list = i.split(" ")
    if int(input_list[0]) > int(input_list[-1]):
        for u in range(len(input_list)):
            if u == len(input_list)-1:
                safe += 1
                break

            if (int(input_list[u]) > int(input_list[u+1])) and (1 <= (int(input_list[u]) - int(input_list[u+1])) <= 3):
                continue
            else:
                break

    elif int(input_list[0]) < int(input_list[-1]):
        for u in range(len(input_list)):
            if u == len(input_list)-1:
                safe += 1
                break

            if (int(input_list[u]) < int(input_list[u+1])) and (1 <= (int(input_list[u+1]) - int(input_list[u])) <= 3):
                continue
            else:
                break

    input_list = []

print(safe)