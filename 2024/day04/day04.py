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

direction_checks = []

for i in input:
    for u in i:
        if u == "X":
            if x not in [0,1,2]: #Backwards
                if input[y][x-1] == "M":
                    direction_checks.append(4)
            if x not in [len(i)-3,len(i)-2,len(i)-1]: #Forwards
                if input[y][x+1] == "M":
                    direction_checks.append(6)
            if y not in [0,1,2]: #Upwards
                if input[y-1][x] == "M":
                    direction_checks.append(8)
            if y not in [len(input)-3,len(input)-2,len(input)-1]: #Downward
                if input[y+1][x] == "M":
                    direction_checks.append(2)
            if x not in [0,1,2] and y not in [len(input)-3,len(input)-2,len(input)-1]: #Downback
                if input[y+1][x-1] == "M":
                    direction_checks.append(1)
            if x not in [0,1,2] and y not in [0,1,2]: #Upback
                if input[y-1][x-1] == "M":
                    direction_checks.append(7)
            if x not in [len(i)-3,len(i)-2,len(i)-1] and y not in [len(input)-3,len(input)-2,len(input)-1]: #Downforward
                if input[y+1][x+1] == "M":
                    direction_checks.append(3)
            if x not in [len(i)-3,len(i)-2,len(i)-1] and y not in [0,1,2]: #Upforward
                if input[y-1][x+1] == "M":
                    direction_checks.append(9)

            while direction_checks:
                direction = direction_checks[0]

                y_check = y
                x_check = x

                y_check += direction_dict_y[direction] #Twice because M is already found
                x_check += direction_dict_x[direction]
                y_check += direction_dict_y[direction]
                x_check += direction_dict_x[direction]

                if input[y_check][x_check] == "A":
                    y_check += direction_dict_y[direction]
                    x_check += direction_dict_x[direction]
                    if input[y_check][x_check] == "S":
                        xmas += 1
                direction_checks = direction_checks[1:]
        x += 1

    y += 1
    x = 0

print(xmas)