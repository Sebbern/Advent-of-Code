import re

input_list = open("input.txt").read().splitlines()
card_dict = {}

for i in input_list:
    a, right = re.split(r"[|]", i)
    left = re.split(r"[:]", a)
    winning_numbers = re.split("\s", left[1])
    winning_numbers = list(filter(None, winning_numbers))
    numbers = re.split("\s", right)
    numbers = list(filter(None, numbers))
    winning_count = 0

    for u in numbers:
        if u in winning_numbers:
            print(left[0], u, winning_numbers)
            winning_count += 1
    
    if winning_count == 1:
        card_dict[left[0]] = 1
    elif winning_count > 1:
        card_dict[left[0]] = 1*2**(winning_count-1)
    
sum = sum(card_dict.values())
print(sum)