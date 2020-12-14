report = open("input.txt", "r").readlines()

for i in report:
    for u in report:
        for y in report:
            if int(i) + int(u) + int(y) == 2020:
                print (int(i) * int(u) * int(y))
                break
        else:
            continue
        break
    else:
        continue
    break