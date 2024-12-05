from collections import defaultdict

input = open("2024\\day05\\input.txt").read().splitlines()

input_list = []
page_dict = defaultdict(list)

for idx, i in enumerate(input):
    if i == "":
        idx += 1
        break
    input_list = list(map(int,i.split("|")))
    x = input_list[0]
    y = input_list[1]

    page_dict.setdefault(x, []).append(y)

correct_list = []

for i in input[idx:]:
    input_list = list(map(int,i.split(",")))
    for idx_u, u in enumerate(input_list):
        idx_u_check = idx_u
        while idx_u_check >= 0:
            if input_list[idx_u_check] in page_dict[u]:
                break
            idx_u_check -= 1
        else:
            continue
        break
    else:
        correct_list.append(i)

sum = 0

for i in correct_list:
    sum_list = list(map(int,i.split(",")))
    sum += sum_list[len(sum_list)//2]

print(sum)