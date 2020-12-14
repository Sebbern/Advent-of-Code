numbers = open("input.txt", "r").read().splitlines()

preamble = []
result = 0

for i in numbers:
    if len(preamble) > 25:
        preamble = preamble[-25:]

    if len(preamble) == 25:
        for x in preamble:
            for y in preamble:
                if int(x) + int(y) == int(i):
                    if x != y:
                        result += 1
        
        if result == 0:
            print(i)
            break
        
        result = 0

    preamble.append(i)

