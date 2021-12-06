lanternfish_list = open("input.txt", "r").read().split(",")
days = 0
updated_list = lanternfish_list

while days < 80:
    idx = 0
    for i in updated_list:
        if int(i) != 0:
            lanternfish_list[idx] = int(updated_list[idx]) - 1
        elif int(i) == 0:
            lanternfish_list[idx] = 6
            lanternfish_list.append(9)
        idx += 1
    days += 1
    updated_list = lanternfish_list

print(len(updated_list))