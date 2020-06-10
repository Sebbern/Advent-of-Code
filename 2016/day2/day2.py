codelist = open("input.txt", "r").read().split()

position = 5
code = []

def goUp():
    global position
    if position not in [1,2,3]:
        position -= 3

def goDown():
    global position
    if position not in [7,8,9]:
        position += 3

def goLeft():
    global position
    if position not in [1,4,7]:
        position -= 1

def goRight():
    global position
    if position not in [3,6,9]:
        position += 1

print(position)

for i in codelist:
    while len(i) > 0:
        if i[0] == "U":
            goUp()
        elif i[0] == "D":
            goDown()
        elif i[0] == "L":
            goLeft()
        elif i[0] == "R":
            goRight()
        i = i[1:]
        print(position)
        #print(i)
    if len(i) == 0:
        code.append(position)

print(code)

