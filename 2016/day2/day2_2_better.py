codelist = open("input.txt", "r").read().split()

doorcode = ["x", "x",  1 , "x", "x",
            "x",  2 ,  3 ,  4 , "x",
             5 ,  6 ,  7 ,  8 ,  9 ,
            "x", "A", "B", "C", "x",
            "x", "x", "D", "x", "x"]

position = doorcode[10]
code = []

def goUp():
    global position
    if position not in [1,2,4,5,9]:
        s = doorcode.index(position)
        position = doorcode[s-5]

def goRight():
    global position
    if position not in [1,4,9,"C","D"]:
        s = doorcode.index(position)
        position = doorcode[s+1]

def goLeft():
    global position
    if position not in [1,2,5,"A","D"]:
        s = doorcode.index(position)
        position = doorcode[s-1]

def goDown():
    global position
    if position not in [5,9,"A","C","D"]:
        s = doorcode.index(position)
        position = doorcode[s+5]

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
    if len(i) == 0:
        code.append(position)

print(code)