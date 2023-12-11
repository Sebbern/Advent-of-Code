input_list = open("2023\\day10\\input.txt").read().splitlines()

labyrinth_list = []
lane_length = len(input_list[0])
start_index = 0
start_check = False
previous_list = []
direction_list = []
curr_index_list = []
length_index = 0

#Extra to draw a maze
length_list = []
maze_start = False

for i in input_list:
    for u in i:
        labyrinth_list.append(u)

for i in range(len(labyrinth_list)):
    length_list.append(".")

for i in labyrinth_list:
    if i == "S":
        break
    start_index += 1

while (True):
    length_index += 1
    if i == "S" and start_check == False:
        length_list[start_index] = "S"
        if labyrinth_list[start_index-1] in ("F","-","L"):
            previous_list.append("Left")
            direction_list.append(labyrinth_list[start_index-1])
            length_list[start_index-1] = labyrinth_list[start_index-1]
            curr_index_list.append(start_index-1)
        
        if labyrinth_list[start_index+1] in ("-","7","J"):
            previous_list.append("Right")
            direction_list.append(labyrinth_list[start_index+1])
            length_list[start_index+1] = labyrinth_list[start_index+1]
            curr_index_list.append(start_index+1)
        
        if labyrinth_list[start_index-lane_length] in ("|","7","F"):
            previous_list.append("Up")
            direction_list.append(labyrinth_list[start_index-lane_length])
            length_list[start_index-lane_length] = labyrinth_list[start_index-lane_length]
            curr_index_list.append(start_index-lane_length)

        if labyrinth_list[start_index+lane_length] in ("|","L","J"):
            previous_list.append("Down")
            direction_list.append(labyrinth_list[start_index+lane_length])
            length_list[start_index+lane_length] = labyrinth_list[start_index+lane_length]
            curr_index_list.append(start_index+lane_length)
            
        start_check = True
    else:
        route_index = 0
        for u in direction_list:
            if u == "F":
                if previous_list[route_index] == "Left":
                    previous_list[route_index] = "Down"
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]+lane_length]

                else:
                    previous_list[route_index] = "Right"
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]+1]

            elif u == "-":
                if previous_list[route_index] == "Right":
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]+1]
                else:
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]-1]

            elif u == "7":
                if previous_list[route_index] == "Up":
                    previous_list[route_index] = "Left"
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]-1]
                else:
                    previous_list[route_index] = "Down"
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]+lane_length]

            elif u == "L":
                if previous_list[route_index] == "Left":
                    previous_list[route_index] = "Up"
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]-lane_length]
                else:
                    previous_list[route_index] = "Right"
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]+1]

            elif u == "J":
                if previous_list[route_index] == "Right":
                    previous_list[route_index] = "Up"
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]-lane_length]
                else:
                    previous_list[route_index] = "Left"
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]-1]

            elif u == "|":
                if previous_list[route_index] == "Up":
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]-lane_length]
                else:
                    direction_list[route_index] = labyrinth_list[curr_index_list[route_index]+lane_length]

            #length_list and maze_start are used to draw a maze, not needed for the task
            match previous_list[route_index]:
                case "Up":
                    if maze_start == True:
                        length_list[curr_index_list[route_index]] = u
                    curr_index_list[route_index] = curr_index_list[route_index]-lane_length
                case "Down":
                    if maze_start == True:
                        length_list[curr_index_list[route_index]] = u
                    curr_index_list[route_index] = curr_index_list[route_index]+lane_length
                case "Left":
                    if maze_start == True:
                        length_list[curr_index_list[route_index]] = u
                    curr_index_list[route_index] = curr_index_list[route_index]-1
                case "Right":
                    if maze_start == True:
                        length_list[curr_index_list[route_index]] = u
                    curr_index_list[route_index] = curr_index_list[route_index]+1

            maze_start = True
            route_index += 1
    
    #Prints the solution
    if curr_index_list[0] == curr_index_list[1]:
        print(length_index)
        break

#Prints out the maze
for idx, x in enumerate(length_list):
    if idx % lane_length == 0:
        print("")
    print(x, end = "")