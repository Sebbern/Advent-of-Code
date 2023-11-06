import re

iList = open("input.txt", "r").read().splitlines()
claimList = [0] * (1000*1000)
compileI = re.compile(r"[#](\d+)\s[@]\s(\d+),(\d+)[:]\s(\d+)x(\d+)")

for i in iList:
    reI = re.findall(compileI, i)
    id, x, y, xClaim, yClaim = reI[0][0], reI[0][1], reI[0][2], reI[0][3], reI[0][4]
    claimStart = (int(x)+1000*int(y))

    for u in range(int(xClaim)):
        for t in range(int(yClaim)):
            if (claimList[claimStart+u+(t*1000)] == 0):
                claimList[claimStart+u+(t*1000)] = id
            else:
                claimList[claimStart+u+(t*1000)] = "X"

for i in iList:
    test = False
    reI = re.findall(compileI, i)
    id, x, y, xClaim, yClaim = reI[0][0], reI[0][1], reI[0][2], reI[0][3], reI[0][4]
    claimStart = (int(x)+1000*int(y))

    for u in range(int(xClaim)):
        for t in range(int(yClaim)):
            if (claimList[claimStart+u+(t*1000)] == "X"):
                test = True
                break

        if (test == True):
            break

    if (test == False):
        break

print(id)