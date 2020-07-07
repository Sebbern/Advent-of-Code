masslist = open("input.txt", "r").read().split()

fuel = 0 # Part one

for mass in masslist:
    mass = int(mass)
    mass /= 3
    mass = int(mass)
    mass -= 2
    fuel += mass

print(fuel)

fueltwo = 0 # Part two

for mass in masslist: 
    while int(mass) > 0:
        mass = int(mass)
        mass /= 3
        mass = int(mass)
        mass -= 2
        if mass > 0:
            fueltwo += mass

print(fueltwo)