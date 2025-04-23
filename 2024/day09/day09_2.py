input = open("2024\\day09\\input.txt").read().splitlines()  
flip = False
checksum_list = []
id = 0
count_check_x = False
count_check_y = False

for i in input:
    for u in i:
        counter = int(u)
        while counter > 0:
            if flip == False:
                checksum_list.append(id)
            
            else:
                checksum_list.append(".")
            counter -= 1

        if flip == False:
            id += 1

        flip = not flip
    
    x_idx = 0
    y_idx = len(checksum_list)-1
    x = checksum_list[x_idx]
    y = checksum_list[y_idx]
    x_count = 0
    y_count = 0
    swap_idx = 0

    while x_idx != y_idx:
        if x != ".":
            x_idx += 1

        if y == ".":
            y_idx -= 1

        #Slow because x starts at the beginning of the list each time it doesn't find any space for y
        if x == "." and count_check_x == False and count_check_y == True:
            y_count = checksum_list.count(y)
            while True:
                if x != ".":
                    if x_count >= y_count:
                        x = checksum_list[x_idx]
                        x_idx -= x_count
                        count_check_x = True
                        break
                    else:
                        x_count = 0

                elif x == ".":
                    x_count += 1

                x_idx += 1
                x = checksum_list[x_idx]

                if x_idx == y_idx:
                    x_idx = 0
                    y_idx -= y_count
                    break

            x_count = 0

        if y != "." and count_check_y == False:
            count_check_y = True

        if x == "." and y != "." and count_check_x == True and count_check_y == True:
            while y_count > 0:
                checksum_list[x_idx+swap_idx] = y
                checksum_list[y_idx-swap_idx] = x
                swap_idx += 1
                x = checksum_list[x_idx+swap_idx]
                y = checksum_list[y_idx-swap_idx]
                y_count -= 1

            count_check_x = False
            count_check_y = False
            swap_idx = 0
            x_idx = 0

        x = checksum_list[x_idx]
        y = checksum_list[y_idx]
            
checksum = 0

for index, i in enumerate(checksum_list):
    if i != ".":
        checksum += (int(i) * int(index))

print(checksum)