from collections import defaultdict

input = open("2024\\day04\\input.txt").read().splitlines()

x = 0
y = 0
x_check = 0
y_check = 0
direction = 0
xmas = 0

direction_dict_y = {7:-1, 8:-1, 9:-1,
                    4:0 , 5:0 , 6:0 ,
                    1:+1, 2:+1, 3:+1}

direction_dict_x = {7:-1, 8:0, 9:+1,
                    4:-1, 5:0, 6:+1,
                    1:-1, 2:0, 3:+1}

a_cross_dict = defaultdict(int)

direction_checks = []

for i in input:
    for u in i:
        if u == "M":
            if x not in [0,1] and y not in [len(input)-2,len(input)-1]: #Downback
                if input[y+1][x-1] == "A":
                    direction_checks.append(1)
            if x not in [0,1] and y not in [0,1]: #Upback
                if input[y-1][x-1] == "A":
                    direction_checks.append(7)
            if x not in [len(i)-2,len(i)-1] and y not in [len(input)-2,len(input)-1]: #Downforward
                if input[y+1][x+1] == "A":
                    direction_checks.append(3)
            if x not in [len(i)-2,len(i)-1] and y not in [0,1]: #Upforward
                if input[y-1][x+1] == "A":
                    direction_checks.append(9)

            while direction_checks:
                direction = direction_checks[0]

                y_check = y
                x_check = x
                
                #Twice because A is already found
                y_check += direction_dict_y[direction] 
                x_check += direction_dict_x[direction]
                y_check += direction_dict_y[direction]
                x_check += direction_dict_x[direction]

                if input[y_check][x_check] == "S":
                    a_cross_dict[(y_check-direction_dict_y[direction],x_check-direction_dict_x[direction])] += 1

                direction_checks = direction_checks[1:]
        x += 1
        
    y += 1
    x = 0

values_of_mas_cross = list(a_cross_dict.values())

for i in values_of_mas_cross:
    if i >= 2:
        xmas += 1

print(xmas)