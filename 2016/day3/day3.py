trianglelist = open("input.txt", "r").read().split()

validtriangle = 0

while len(trianglelist) > 0:
    a = int(trianglelist[0])
    b = int(trianglelist[1])
    c = int(trianglelist[2]) 
    if a + b > c and b + c > a and a + c > b:
        validtriangle += 1
        trianglelist = trianglelist[3:]
    else:
        trianglelist = trianglelist[3:]

print(validtriangle)
