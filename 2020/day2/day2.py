passwordlist = open("input.txt", "r").read().split()
minmax = 0
letter = ""
password = ""
first = 0
second = 0
validpasswords = 0

while len(passwordlist) > 0:
    count = 0
    minmax = passwordlist[0]
    first, second = minmax.split("-")
    letter = passwordlist[1].strip(":")
    password = passwordlist[2]
    passwordlist = passwordlist[3:]

    for i in password:
        if letter == i:
            count += 1
    
    if count >= int(first) and count <= int(second):
        validpasswords += 1

print(validpasswords)