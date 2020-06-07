freqlist = open("input.txt", "r").read().split()
freq = 0

for i in freqlist:
    freq += int(i)

print(freq)
