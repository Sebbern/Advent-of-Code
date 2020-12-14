passphrase = open("input.txt", "r").read().splitlines()
validpassphrases = 0
word = []

for u in passphrase:
    validpassphrases += 1
    word = u.split()
    for i in word:
        if word.count(i) > 1:
            validpassphrases -= 1
            break

print(validpassphrases)