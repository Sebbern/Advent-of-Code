#!/usr/bin/env python

captcha = open("input.txt", "r").read()
captchalist = [x for x in str(captcha)]

# Part one
sumcaptcha = 0
u = 0
y = 0

for i in captchalist:
    y = u
    u = i
    if y == u:
        sumcaptcha += int(y)

if captchalist[0] == captchalist[-1]:
    sumcaptcha += int(captchalist[0])

print(sumcaptcha)

# Part two
sumcaptchatwo = 0
halfoflist = int(len(captchalist)/2)
uu = 0

for i, ii in enumerate(captchalist):
    uu = int(ii)
    i += halfoflist
    try:
        ii = captchalist[i]
    except:
        IndexError
        break
    if uu == int(ii):
        sumcaptchatwo += int(ii) * 2
    
print(sumcaptchatwo)
