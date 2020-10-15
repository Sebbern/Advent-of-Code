minpuzzle = 231832
maxpuzzle = 767346
passwords = []

for i in range(minpuzzle, maxpuzzle + 1):
    for a,b,c,d,e,f in zip(str(i)[0:],str(i)[1:],str(i)[2:],str(i)[3:],str(i)[4:],str(i)[5:]):
        if a <= b <= c <= d <= e <= f:
            if a == b or b == c or c == d or d == e or e == f:    
                passwords.append(i)

print(len(passwords))