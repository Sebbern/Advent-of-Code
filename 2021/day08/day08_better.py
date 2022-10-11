digits = open("input.txt","r").read().splitlines()
digit_output_list = []
solution = 0
real_numbers = [2,3,4,7]

for i in digits:
    digit_input, digit_output = i.split("|")
    digit_output_list.append(digit_output.strip())

for i in digit_output_list:
    for u in i.split(" "):
        if len(u) in real_numbers:
            solution += 1

print(solution)