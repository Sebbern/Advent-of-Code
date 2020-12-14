boardingpasses = open("input.txt", "r").read().splitlines()


def front(rlist, upper):
    upper = upper / 2
    rlist = rlist[0:int(upper)]
    return(rlist)

def back(rlist, lower):
    lower += (len(rlist) / 2)
    rlist = rlist[int(lower):]
    return(rlist)

def left(clist, upper):
    upper = upper / 2
    clist = clist[0:int(upper)]
    return(clist)

def right(clist, lower):
    lower += (len(clist) / 2)
    clist = clist[int(lower):]
    return(clist)

def main():
    seatidlist = []

    for i in boardingpasses:
        rowlist = [*range(0, 128)]
        columnlist = [*range(0, 8)]
        row = 0
        column = 0
        seatid = 8

        for u in i:
            upper = len(rowlist)
            lower = 0
            seatupper = len(columnlist)
            seatlower = 0
            
            if u == "F":
                rowlist = front(rowlist, upper)
            elif u == "B":
                rowlist = back(rowlist, lower)
            elif u == "L":
                columnlist = left(columnlist, seatupper)
            elif u == "R":
                columnlist = right(columnlist, seatlower)

        row = rowlist[0]
        column = columnlist[0]
        seatidlist.append(int(row) * seatid + int(column))
    
    return(max(seatidlist))

print(main())