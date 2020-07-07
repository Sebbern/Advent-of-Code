import itertools

freqlist = open("input.txt", "r").read().split()
# Part one
freq = 0

for i in freqlist:
    freq += int(i)

print(freq)

# Part two
freqtwo = 0
sumlist = {0}

for i in itertools.cycle(freqlist):
    freqtwo += int(i)
    if freqtwo in sumlist:
        print(freqtwo)
        break
    sumlist.add(freqtwo)