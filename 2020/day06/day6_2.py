answers = open("input.txt", "r").read().split("\n")

groupyes = []
yes = 0
person = 0

for i in answers:
    if not i:
        allyes = list(set([x for x in groupyes if groupyes.count(x) >= person]))
        yes += len(allyes)

        groupyes = []
        person = 0
        continue
    for u in i:
        groupyes.append(u)
    person += 1

print(yes)