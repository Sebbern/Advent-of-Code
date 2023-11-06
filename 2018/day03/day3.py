import re

iList = open("input.txt", "r").read().splitlines()
claimList = [0] * (1000*1000)

for i in iList:
    compileI = re.compile(r"(\d+),(\d+)[:]\s(\d+)x(\d+)")
    reI = re.findall(compileI, i)
    x, y, xClaim, yClaim = reI[0][0], reI[0][1], reI[0][2], reI[0][3]
    claimStart = (int(x)+1000*int(y))

    for u in range(int(xClaim)):
        for t in range(int(yClaim)):
            claimList[claimStart+u+(t*1000)]+=1

count = 0
for i in claimList:
    if (i >= 2):
        count += 1
        
print(count)