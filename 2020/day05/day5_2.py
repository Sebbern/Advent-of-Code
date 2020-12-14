boardingpasses = open("input.txt", "r").read().splitlines()

seatidlist = []

for i in boardingpasses:
    rlist = [*range(0, 128)]
    clist = [*range(0, 8)]
    row = 0
    column = 0
    seatid = 8

    for u in i:
        upper = len(rlist)
        lower = 0
        seatupper = len(clist)
        seatlower = 0
        if u == "F":
            upper = upper / 2
            rlist = rlist[0:int(upper)]
        elif u == "B":
            lower += (len(rlist) / 2)
            rlist = rlist[int(lower):]
        elif u == "L":
            seatupper = seatupper / 2
            clist = clist[0:int(seatupper)]
        elif u == "R":
            seatlower += (len(clist) / 2)
            clist = clist[int(seatlower):]
            
    row = rlist[0]
    column = clist[0]
    seatidlist.append(row * seatid + column)
    seatidlist = sorted(seatidlist)

print([x for x in range(seatidlist[0], seatidlist[-1]+1) if x not in seatidlist])