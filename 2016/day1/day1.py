movementlist = open("input.txt", "r").read().replace(",", "").split()

f = 0
x = 0
y = 0

def directionL(): # Turn left
    global f
    if f == 0:
        f -= 1
    elif f == (-1):
        f -= 1
    elif f == (-2):
        f += 3
    elif f == 1:
        f -= 1

def directionR(): # Turn right
    global f
    if f == 0:
        f += 1
    elif f == 1:
        f -= 3
    elif f == (-2):
        f += 1
    elif f == (-1):
        f += 1

for i in movementlist:
    if i[0] == "L":
        directionL()
    elif i[0] == "R":
        directionR()
    i = i[1:]
    if f == 0: # North
        y += int(i)
    elif f == 1: # East
        x += int(i)
    elif f == (-2): # South
        y -= int(i)
    elif f == (-1): # West
        x -= int(i)

print(abs(x) + abs(y))