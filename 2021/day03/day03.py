binary = open("input.txt", "r").read().split()
binarycount = 0
zerocount = 0
onecount = 0
gammarate = [""]
epsilonrate = [""]

while binarycount < 12:
    for i in binary:
        if i[binarycount] == "0":
            zerocount += 1
        elif i[binarycount] == "1":
            onecount += 1
        
    if onecount > zerocount:
        gammarate[0] = gammarate[0] + "1"
        epsilonrate[0] = epsilonrate[0] + "0"
    elif zerocount > onecount:
        gammarate[0] = gammarate[0] + "0"
        epsilonrate[0] = epsilonrate[0] + "1"

    zerocount = 0
    onecount = 0
    binarycount += 1

powerconsumption = int(gammarate[0], 2) * int(epsilonrate[0], 2)
print(powerconsumption)