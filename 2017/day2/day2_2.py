checksumlist = open("input.txt", "r").read().splitlines()
templist = []
checksum = 0
dividesum = 0
test = 0

for u in checksumlist:
    templist = u.split('\t')
    for i in templist:
        for o in templist:
            if int(i) % int(o) == 0 and i != o:
                dividesum = int(i) / int(o)
                checksum += dividesum
                break
            else:
                continue
            break

print(int(checksum))