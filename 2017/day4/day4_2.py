#!/usr/bin/env python

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
            print(word)
            print(i)
            validpassphrases -= 1
            anagram = []
            break
        anagram.append(i)

print(validpassphrases)