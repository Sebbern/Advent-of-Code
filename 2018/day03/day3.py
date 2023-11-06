import re

iList = open("input.txt", "r").read().splitlines()
claimList = []

for i in range(1000*1000):
    claimList.append(0)

for i in iList:
    compileI = re.compile(r"(\d+),(\d+)")
    compileClaim = re.compile(r"(\d+)x(\d+)")
    reI = re.findall(compileI, i)
    reClaim = re.findall(compileClaim, i)
    x, y = reI[0][0], reI[0][1]
    xClaim, yClaim = reClaim[0][0], reClaim[0][1]
    claimStart = (int(x)+1000*int(y))

    for u in range(int(xClaim)):
        for t in range(int(yClaim)):
            claimList[claimStart+u+(t*1000)]+=1

count = 0
for i in claimList:
    if (i >= 2):
        count += 1
        
print(count)