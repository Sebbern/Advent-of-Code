depth = open("input.txt", "r").read().splitlines()
increase = 0
temp = 0

for i in depth:
    if temp != 0:
        if temp < int(i):
            increase += 1

    temp = int(i)

print(increase)