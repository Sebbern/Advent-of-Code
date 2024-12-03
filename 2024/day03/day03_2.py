import re

input = open("2024\\day03\\input.txt").read().splitlines()

sum = 0
do = True

for i in input:
    input_list = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", i)
    for mul in input_list:
        if mul == "do()":
            do = True
        elif mul == "don't()":
            do = False
        elif mul[0:3] == "mul" and do == True:
            numbers = re.findall(r"\d+", mul)
            x, y = numbers[0], numbers[1]
            sum += (int(x)*int(y))

print(sum)