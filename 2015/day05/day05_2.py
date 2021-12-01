string = open("input.txt","r").read().splitlines()
fourletters = ""
pair = ""
pairlist = []
doublepair = False
letterrepeat = False
nicestring = 0

for i in string:
    for u in i:
        fourletters += u
        pair += u
        if len(pair) > 1:
            if pair in pairlist:
                if i.count(pair) != 2: #What a bandaid
                    continue
                doublepair = True

            pairlist.append(pair)
            pair = pair[1:]

        if len(fourletters) > 3:
            if fourletters[0] == fourletters[2] or fourletters[1] == fourletters[3]:
                letterrepeat = True

            fourletters = fourletters[1:]

    if doublepair == True and letterrepeat == True:
        nicestring += 1

    pairlist = []
    doublepair = False
    letterrepeat = False
    pair = ""
    fourletters = ""

print(nicestring)