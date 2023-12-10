input_list = open("input.txt").read().splitlines()
sum = 0

for i in input_list:
    left = 0; right = len(i)-1; left_number = ""; right_number = ""
    while True:
        if i[left].isdigit() == True and left_number == "":
            left_number = i[left]
        elif left_number == "":
            left += 1

        if i[right].isdigit() == True and right_number == "":
            right_number = i[right]
        elif right_number == "":
            right -= 1

        if left_number != "" and right_number != "":
            sum += int((left_number + right_number))
            break

print(sum)
