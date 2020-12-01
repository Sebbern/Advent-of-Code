report = open("input.txt", "r").readlines()

for i in report:
    for u in report:
        if int(i) + int(u) == 2020:
            print (int(i) * int(u))
            break