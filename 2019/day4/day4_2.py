minpuzzle = 231832
maxpuzzle = 767346
passwords = []

for i in range(minpuzzle, maxpuzzle + 1):
    i = [int(x) for x in str(i)]
    if i == sorted(i):
        for u in i:
            if i.count(u) == 2:
                passwords.append(i)
                break

print(len(passwords))