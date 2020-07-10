checksumlist = open("input.txt", "r").read().splitlines()

def checksum(s):
    checksum = 0
    difference = 0
    for u in checksumlist:
        s = u.split('\t')
        difference = int(max(s, key=int)) - int(min(s, key=int))
        checksum += difference
    print(checksum)

checksum([])
