trianglelist = open("input.txt", "r").read().split()

validtriangle = 0

while len(trianglelist) > 0:
    oneA = int(trianglelist[0])
    oneB = int(trianglelist[1])
    oneC = int(trianglelist[2]) 
    trianglelist = trianglelist[3:]
    twoA = int(trianglelist[0])
    twoB = int(trianglelist[1])
    twoC = int(trianglelist[2])
    trianglelist = trianglelist[3:]
    threeA = int(trianglelist[0])
    threeB = int(trianglelist[1])
    threeC = int(trianglelist[2])
    if oneA + twoA > threeA and twoA + threeA > oneA and oneA + threeA > twoA:
        validtriangle += 1
    if oneB + twoB > threeB and twoB + threeB > oneB and oneB + threeB > twoB:
        validtriangle += 1
    if oneC + twoC > threeC and twoC + threeC > oneC and oneC + threeC > twoC:
        validtriangle += 1
    trianglelist = trianglelist[3:]

print(validtriangle)
