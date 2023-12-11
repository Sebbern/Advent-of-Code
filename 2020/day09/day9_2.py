numbers = open("2020\\day09\\input.txt", "r").read().splitlines()

preamble = []
result = 0

for i in numbers:
    if len(preamble) > 25:
        preamble = preamble[-25:]

    if len(preamble) == 25:
        for x in preamble:
            for y in preamble:
                if int(x) + int(y) == int(i):
                    result += 1
        
        if result == 0:
            break
        
        result = 0

    preamble.append(i)

preamble.clear()

for u in numbers:
    preamble.append(u)

while True:
    temp_sum = 0
    temp_list = []
    for x in preamble:
        temp_list.append(int(x))
        temp_sum += int(x)
        if temp_sum == int(i):
            break
        elif temp_sum > int(i):
            preamble.pop(0)
            break
    
    if temp_sum == 23278925 and len(temp_list)>1:
        break

print(max(temp_list)+min(temp_list))