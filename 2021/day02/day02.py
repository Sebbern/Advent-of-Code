commands = open("input.txt","r").read().split()
depth = 0
horipos = 0
mode = ""

for i in commands:
    if i[0].isdigit() == False:
        mode = i
    
    if i[0].isdigit() == True:
        if mode == "forward":
            horipos += int(i)
        elif mode == "up":
            depth -= int(i)
        elif mode == "down":
            depth += int(i)
            
print(horipos*depth)