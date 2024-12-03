import re

input = open("2024\\day03\\input.txt").read().splitlines()

sum = 0

for i in input:
    input_list = re.findall(r'mul\(\d+,\d+\)', i)
    for mul in input_list:
        if mul[0:3] == "mul":
            numbers = re.findall(r"\d+", mul)
            x, y = numbers[0], numbers[1]
            sum += (int(x)*int(y))

print(sum)
