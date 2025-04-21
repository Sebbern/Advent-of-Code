input = open("2024\\day09\\input.txt").read().splitlines()  
flip = False
checksum_list = []
id = 0

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
    
    x_count = 0
    y_count = len(checksum_list)-1
    x = checksum_list[x_count]
    y = checksum_list[y_count]

    while x_count != y_count: 
        if x != ".":
            x_count += 1

        if y == ".":
            y_count -= 1

        if x == "." and y != ".":
            checksum_list[x_count] = y
            checksum_list[y_count] = x
            x_count += 1
            y_count -= 1
                
        x = checksum_list[x_count]
        y = checksum_list[y_count]

checksum = 0

for index, i in enumerate(checksum_list):
    if i != ".":
        checksum += (int(i) * int(index))

print(checksum)