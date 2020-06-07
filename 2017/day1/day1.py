captcha = open("input.txt", "r").read()
sumcaptcha = 0
u = 0
y = 0

captchalist = [x for x in str(captcha)]

for i in captchalist:
    y = u
    u = i
    if y == u:
        sumcaptcha += int(y)

if captchalist[0] == captchalist[-1]:
    sumcaptcha += int(captchalist[0])

print(sumcaptcha)