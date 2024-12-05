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

incorrect_list = []
incorrect = False

while idx < len(input):
    i = input[idx]
    if incorrect == False:
        input_list = list(map(int,i.split(",")))
    for idx_u, u in enumerate(input_list):
        idx_u_check = idx_u
        while idx_u_check >= 0:
            if input_list[idx_u_check] in page_dict[u]:
                incorrect = True
                idx -= 1
                input_list[idx_u_check], input_list[idx_u] = input_list[idx_u], input_list[idx_u_check]
                break
            idx_u_check -= 1
        else:
            continue
        break
    else:
        if incorrect == True:
            incorrect_list.append(input_list)
            incorrect = False

    idx += 1
sum = 0

for i in incorrect_list:
    sum += i[len(i)//2]

print(sum)