input_list = open("2024\\day01\\input.txt").read().splitlines()
list_a = []
list_b = [] 

for i in input_list:
    x, y = str.split(i)
    list_a.append(int(x))
    list_b.append(int(y))

list_a.sort()
list_b.sort()
diff = 0

for a, b in zip(list_a, list_b):
    diff += abs(a-b)

print(diff)