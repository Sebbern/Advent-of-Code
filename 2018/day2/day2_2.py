idlist = open("input.txt", "r").read().split()

iddict = {}
difference = 0
common_letters = ""

for i in idlist:
    for u in idlist:
        if u != i:
            for a, b in zip(i, u):
                iddict[a] = b
                if a != b:
                    difference += 1
            if difference == 1:
                for a, b in zip(i, u):
                    if a == b:
                        common_letters += a
                break
            difference = 0
    else:
        continue
    break

print(common_letters)