commands = open("input.txt","r").read().split()
depth = 0
horipos = 0
aim = 0
mode = ""

for i in commands:
    if i[0].isdigit() == False:
        mode = i
    
    if i[0].isdigit() == True:
        if mode == "forward":
            horipos += int(i)
            depth += int(i)*aim
        elif mode == "up":
            aim -= int(i)
        elif mode == "down":
            aim += int(i)
            
print(horipos*depth)