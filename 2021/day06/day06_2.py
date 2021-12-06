lanternfish_list = open("input.txt", "r").read().split(",")
days = 0
lanternfish_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
lanternfish = 0

for i in lanternfish_list:
    lanternfish_dict[int(i)] += 1

while days < 256:
    temp = lanternfish_dict[0]
    lanternfish_dict[0] = lanternfish_dict[1]
    lanternfish_dict[1] = lanternfish_dict[2]
    lanternfish_dict[2] = lanternfish_dict[3]
    lanternfish_dict[3] = lanternfish_dict[4]
    lanternfish_dict[4] = lanternfish_dict[5]
    lanternfish_dict[5] = lanternfish_dict[6]
    lanternfish_dict[6] = temp + lanternfish_dict[7]
    lanternfish_dict[7] = lanternfish_dict[8]
    lanternfish_dict[8] = temp
    days += 1

for x, y in lanternfish_dict.items():
    lanternfish += y

print(lanternfish)