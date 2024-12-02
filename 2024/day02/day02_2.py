#This shouldn't work, there is one specific edge case that I cannot find
input = open("2024\\day02\\input.txt").read().splitlines()

safe = 0
bad_level = False
i = 0

while i < len(input):
    if bad_level == False:
        input_list = input[i].split(" ")

    if (int(input_list[0]) > int(input_list[-1])) or ((int(input_list[0]) == int(input_list[-1])) and (int(input_list[0]) > int(input_list[1]))) or ((int(input_list[0]) > int(input_list[2])) and (int(input_list[0]) < int(input_list[1])) and (int(input_list[1]) > int(input_list[-1]))):
        for u in range(len(input_list)):
            if u == len(input_list)-1:
                safe += 1
                bad_level = False
                break

            if (int(input_list[u]) > int(input_list[u+1])) and (1 <= (int(input_list[u]) - int(input_list[u+1])) <= 3):
                if u+2 < len(input_list)-1:
                    if int(input_list[u]) > int(input_list[u+1]) and int(input_list[u+1]) < int(input_list[u+2]) and int(input_list[u]) == int(input_list[-1]) and bad_level == False:
                        input_list.pop(u)
                        i -= 1
                        bad_level = True
                        break
            else:
                if bad_level == False:
                    if u+2 < len(input_list)-1:
                        if (int(input_list[u+1]) > int(input_list[u+2])) and (1 <= (int(input_list[u+1]) - int(input_list[u+2])) <= 3):
                            input_list.pop(u)
                        elif (int(input_list[u]) > int(input_list[u+2])) and (1 <= (int(input_list[u]) - int(input_list[u+2])) <= 3):
                            input_list.pop(u+1)
                        elif (int(input_list[0]) > int(input_list[2])) and (int(input_list[0]) < int(input_list[1])):
                            input_list.pop(u+1)
                        else:
                            input_list.pop(u)
                        i -= 1
                        bad_level = True
                        break

                    if (int(input_list[u]) == int(input_list[u+1])):
                        input_list.pop(u) 
                    else:
                        input_list.pop(u+1)
                    i -= 1
                    bad_level = True
                    break
                else:
                    bad_level = False
                    break

    elif (int(input_list[0]) < int(input_list[-1])) or ((int(input_list[0]) == int(input_list[-1])) and (int(input_list[0]) < int(input_list[1]))) or ((int(input_list[0]) < int(input_list[2])) and (int(input_list[0]) > int(input_list[1])) and (int(input_list[1]) < int(input_list[-1]))):
        for u in range(len(input_list)):
            if u == len(input_list)-1:
                safe += 1
                bad_level = False
                break

            if (int(input_list[u]) < int(input_list[u+1])) and (1 <= (int(input_list[u+1]) - int(input_list[u])) <= 3):
                if u+2 < len(input_list)-1:
                    if int(input_list[u]) < int(input_list[u+1]) and int(input_list[u+1]) > int(input_list[u+2]) and int(input_list[u]) == int(input_list[-1]) and bad_level == False:
                        input_list.pop(u)
                        i -= 1
                        bad_level = True
                        break
            else:
                if bad_level == False:
                    if u+2 < len(input_list)-1:
                        if (int(input_list[u+1]) < int(input_list[u+2])) and (1 <= (int(input_list[u+2]) - int(input_list[u+1])) <= 3):
                            input_list.pop(u)
                        elif (int(input_list[u]) < int(input_list[u+2])) and (1 <= (int(input_list[u+2]) - int(input_list[u])) <= 3):
                            input_list.pop(u+1)
                        elif (int(input_list[0]) < int(input_list[2])) and (int(input_list[0]) > int(input_list[1])):
                            input_list.pop(u+1)
                        else:
                            input_list.pop(u)
                        i -= 1
                        bad_level = True
                        break

                    if (int(input_list[u]) == int(input_list[u+1])):
                        input_list.pop(u)
                    else:
                        input_list.pop(u+1)
                    i -= 1
                    bad_level = True
                    break
                else:
                    bad_level = False
                    break 

    i += 1

print(safe)