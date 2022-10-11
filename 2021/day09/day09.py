lavatube_points = open("input.txt","r").read().splitlines()
count = 0
idx = 0
risk_level = 0

for i in lavatube_points:
    for u in i:
        if idx == 0:
            if count == 0:
                if int(u) < int(lavatube_points[count][idx+1]) and int(u) < int(lavatube_points[count+1][idx]):
                    risk_level += (1+int(u))

            elif count == 99:
                if int(u) < int(lavatube_points[count][idx+1]) and int(u) < int(lavatube_points[count-1][idx]):
                    risk_level += (1+int(u))

            else:
                if int(u) < int(lavatube_points[count][idx+1]) and int(u) < int(lavatube_points[count+1][idx]) and int(u) < int(lavatube_points[count-1][idx]):
                    risk_level += (1+int(u))

        elif idx == 99:
            if count == 0:
                if int(u) < int(lavatube_points[count][idx-1]) and int(u) < int(lavatube_points[count+1][idx]):
                    risk_level += (1+int(u))

            elif count == 99:
                if int(u) < int(lavatube_points[count][idx-1]) and int(u) < int(lavatube_points[count-1][idx]):
                    risk_level += (1+int(u))

            else:
                if int(u) < int(lavatube_points[count][idx-1]) and int(u) < int(lavatube_points[count+1][idx]) and int(u) < int(lavatube_points[count-1][idx]):
                    risk_level += (1+int(u))

        else:
            if count == 0:
                if int(u) < int(lavatube_points[count][idx-1]) and int(u) < int(lavatube_points[count][idx+1]) and int(u) < int(lavatube_points[count+1][idx]):
                    risk_level += (1+int(u))

            elif count == 99:
                if int(u) < int(lavatube_points[count][idx-1]) and int(u) < int(lavatube_points[count][idx+1]) and int(u) < int(lavatube_points[count-1][idx]):
                    risk_level += (1+int(u))

            else:
                if int(u) < int(lavatube_points[count][idx-1]) and int(u) < int(lavatube_points[count][idx+1]) and int(u) < int(lavatube_points[count-1][idx]) and int(u) < int(lavatube_points[count+1][idx]):
                    risk_level += (1+int(u))

        idx += 1

    count += 1
    idx = 0

print(risk_level) #if statements galore