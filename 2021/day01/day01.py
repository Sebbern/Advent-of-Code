depth = open("input.txt", "r").readlines()
increase = 0
temp = 0

for i in depth:
    if int(temp) != 0:
        if int(temp) < int(i):
            increase += 1

    temp = int(i)

print(increase)