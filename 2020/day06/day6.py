answers = open("input.txt", "r").read().split("\n")

groupyes = []
yes = 0

for i in answers:
    if not i:
        uniqueyes = set(groupyes)
        yes += len(uniqueyes)

        groupyes = []
    for u in i:
        groupyes.append(u)

print(yes)