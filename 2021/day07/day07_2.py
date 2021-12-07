import sys

crab_pos = open("input.txt", "r").read().split(",")
crab_pos = [int(x) for x in crab_pos]
fuel = 0
min_fuel = sys.maxsize
difference = 0

for i in range(max(crab_pos)):
    for u in crab_pos:
        difference = max(u, i) - min(u, i)
        for y in range(difference):
            fuel += (y+1)
    
    if min_fuel > fuel:
        min_fuel = fuel
    fuel = 0

print(min_fuel)