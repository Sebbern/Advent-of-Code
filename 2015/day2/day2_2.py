l = 0 #length
w = 0 #width
h = 0 #height
ribbon = 0
bow = 0
total = 0

for i in open("input.txt", "r"):
    l, w, h = i.split("x")
    l = int(l)
    w = int(w)
    h = int(h)
    bow = l*w*h
    ribbon = min(l+l+w+w, w+w+h+h, l+l+h+h)
    total += bow + ribbon

print(total)