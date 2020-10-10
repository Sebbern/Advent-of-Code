idlist = open("input.txt", "r").read().split()

checksum = 0
twos = 0
threes = 0
count = {}

for i in idlist:
    for u in i:
        if u in count:
            count[u] += 1
        else:
            count[u] = 1
    for checkforthree in count.values():
        if checkforthree == 3:
            threes += 1
            break
    for checkfortwo in count.values():
        if checkfortwo == 2:
            twos += 1
            break
    count = {}

checksum = twos * threes

print(checksum)