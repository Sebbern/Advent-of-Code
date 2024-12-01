input_list = open("2024\\day01\\input.txt").read().splitlines()
list_a = []
list_b = []
set_a = set()
set_b = set()

for i in input_list:
    x, y = str.split(i)
    list_a.append(int(x))
    list_b.append(int(y))

diff = 0

for a in list_a:
    diff += (a*list_b.count(a))

print(diff)