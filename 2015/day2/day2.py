l = 0 #length
w = 0 #width
h = 0 #height
area = 0
slack = 0
total = 0

for i in open("input.txt", "r"):
    l, w, h = i.split("x")
    l, w, h = int(l), int(w), int(h)
    area = 2*l*w + 2*w*h + 2*l*h
    slack = min(l*w, w*h, l*h)
    total += area + slack

print(total)
