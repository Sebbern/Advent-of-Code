codelist = open("input.txt", "r").read().split()
position = 5
code = []

def goUp():
    global position
    if position not in [1,2,4,5,9]:
        if position in [6,7,8]:
            position -= 4
        elif position == 3:
            position -= 2
        elif position == "A":
            position = 6
        elif position == "D":
            position = "B"
        elif position == "C":
            position = 8
        elif position == "B":
            position = 7

def goDown():
    global position
    if position not in [5,9,"D"]:
        if position in [2,3,4]:
            position += 4
        elif position == 1:
            position += 2
        elif position == 6:
            position = "A"
        elif position == 7:
            position = "B"
        elif position == 8:
            position = "C"
        elif position == "B":
            position = "D"

def goLeft():
    global position
    if position not in [1,2,5,"A","D"]:
        if position in [3,4,6,7,8,9]:
            position -= 1
        elif position == "B":
            position = "A"
        elif position == "C":
            position = "B"

def goRight():
    global position
    if position not in [1,4,9,"C","D"]:
        if position in [2,3,5,6,7,8]:
            position += 1
        elif position == "A":
            position = "B"
        elif position == "B":
            position = "C"

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
    code.append(position)

print(code)