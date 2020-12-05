boardingpasses = open("input.txt", "r").read().splitlines()


def front(rlist, lower, upper):
    upper = len(rlist)//2
    rlist = rlist[lower:upper]
    return(rlist)

def back(rlist, lower, upper):
    lower += len(rlist)//2
    rlist = rlist[lower:upper]
    return(rlist)

def left(clist, lower, upper):
    upper = len(clist)//2
    clist = clist[lower:upper]
    return(clist)

def right(clist, lower, upper):
    lower += len(clist)//2
    clist = clist[lower:upper]
    return(clist)

def main():
    seatidlist = []

    for i in boardingpasses:
        rowlist = [*range(0, 128)]
        columnlist = [*range(0, 8)]
        lower = rowlist[0]
        seatlower = columnlist[0]
        row = 0
        column = 0
        seatid = 8
        #print(len(rowlist), len(columnlist))

        for u in i:
            upper = rowlist[-1]
            seatupper = columnlist[-1]
            print(upper, seatupper, lower, seatlower)
            if u == "F":
                rowlist = front(rowlist, lower, upper)
            elif u == "B":
                rowlist = back(rowlist, lower, upper)
            elif u == "L":
                columnlist = left(columnlist, seatlower, seatupper)
            elif u == "R":
                columnlist = right(columnlist, seatlower, seatupper)
            #print(rowlist, columnlist)

        row = rowlist[0]
        column = columnlist[0]
        #print(rowlist, columnlist)
        seatidlist.append(int(row) * seatid + int(column))

    #return((rowlist))

print(main())