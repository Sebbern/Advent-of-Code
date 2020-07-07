passphrase = open("input.txt", "r").read().splitlines()
validpassphrases = 0
word = []
anagram = []

for u in passphrase:
    validpassphrases += 1
    word = u.split()
    for i in word:
        i = str().join(sorted(i))
        if i in anagram:
            validpassphrases -= 1
            break
        anagram.append(i)
    anagram = []

print(validpassphrases)