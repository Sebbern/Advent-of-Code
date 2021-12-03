binary = open("input.txt", "r").read().split()
binarycount = 0
zerocount = 0
onecount = 0
realbinary = ""
co2binarylist = binary
co2binary = ""

while binarycount < 12:
    for i in binary:
        if i[binarycount] == "0":
            zerocount += 1
        elif i[binarycount] == "1":
            onecount += 1

    if zerocount > onecount:
        realbinary += "0"
    elif onecount > zerocount or onecount == zerocount:
        realbinary += "1"
        
    if len(binary) > 1:
        binary = [x for x in binary if x.startswith(realbinary)]
        
    zerocount = 0
    onecount = 0
    binarycount += 1

binarycount = 0

while binarycount < 12:
    for u in co2binarylist:
        if u[binarycount] == "0":
            zerocount += 1
        elif u[binarycount] == "1":
            onecount += 1

    if zerocount > onecount:
        co2binary += "1"
    elif onecount > zerocount or onecount == zerocount:
        co2binary += "0"

    if len(co2binarylist) > 1:
        co2binarylist = [x for x in co2binarylist if x.startswith(co2binary)]

    zerocount = 0
    onecount = 0
    binarycount += 1

lifesupportrating = int(binary[0], 2) * int(co2binarylist[0], 2)
print(lifesupportrating)