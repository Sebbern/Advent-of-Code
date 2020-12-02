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
    first = int(first) - 1
    second = int(second) - 1
    letter = passwordlist[1].strip(":")
    password = passwordlist[2]
    passwordlist = passwordlist[3:]
    print(first, second, letter, password, password[first], password[second])

    if password[first] == letter or password[second] == letter:
        if password[first] != password[second]:
            validpasswords += 1
            print("yes")

print(validpasswords)