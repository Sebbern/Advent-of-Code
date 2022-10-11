digits = open("input.txt","r").read().splitlines()
digit_input_list = []
digit_output_list = []
numbers = []
input_index = 0
solution = 0
temp_solution = []
fake_numbers = [1,5,6]

for i in digits:
    digit_input, digit_output = i.split("|")
    digit_input_list.append(digit_input.strip())
    digit_output_list.append(digit_output.strip())

for i in digit_output_list:
    i = i.split(" ")
    temp = digit_input_list[input_index]
    temp = temp.split(" ")
    for x in temp:
        if len(x) not in numbers:
            numbers.append(len(x))

    for u in i:
        if len(u) in numbers and len(u) not in fake_numbers:
            temp_solution.append(len(u))
            solution += 1

    temp_solution = []
    numbers = []
    input_index += 1

print(solution)