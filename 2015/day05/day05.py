string = open("input.txt","r").read().splitlines()
vowel = 0
vowellist = ['a','e','i','o','u']
templetter = ""
doubleletter = False
badwordlist = ['ab', 'cd', 'pq', 'xy']
badword = False
nicestring = 0

for i in string:
    for u in i:
        if u in vowellist:
            vowel += 1
        if u == templetter:
            doubleletter = True
        if templetter + u in badwordlist:
            badword = True

        templetter = u

    if vowel >= 3 and doubleletter == True and badword == False:
        nicestring += 1

    vowel = 0
    templetter = ""
    doubleletter = False
    badword = False

print(nicestring)