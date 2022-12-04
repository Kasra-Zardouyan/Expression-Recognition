#Receiving number of photos that we are going to map
picture_count = int(input("Picture count of directory: "))

#Cycling through data
for k in range(picture_count):

    #Reading points from data(k).txt
    listFile = open('./data/data{}.txt'.format(k),'r')
    file = listFile.read()
    lines = list(file.split("\n"))

    #points_index = index of points
    #x_pos = x position of points
    #y_pos = y position of points
    #x_border_pos = x position of border & important points
    #y_border_pos = y position of border & important points
    points_index = []
    x_pos = []
    y_pos = []
    x_border_pos = [0]*100
    y_border_pos = [0]*100

    #Saving x & y position & index from file
    for j in range(len(lines) - 1): 
        cleanedRow = list(lines[j].split(','))
        cleanedRow[-1] = cleanedRow[-1].replace('\n','')
        points_index.append(int(cleanedRow[0]))
        x_pos.append(int(cleanedRow[1]))
        y_pos.append(int(cleanedRow[2]))
    listFile.close()

    #Saving border & important points positions
    x_border_pos[30] = x_pos[30]
    x_border_pos[0] = x_pos[0]
    x_border_pos[16] = x_pos[16]
    x_border_pos[24] = x_pos[24]
    x_border_pos[30] = x_pos[30]
    x_border_pos[8] = x_pos[8]
    x_border_pos[19] = x_pos[19]
    y_border_pos[30] = y_pos[30]
    y_border_pos[0] = y_pos[0]
    y_border_pos[16] = y_pos[16]
    y_border_pos[24] = y_pos[24]
    y_border_pos[30] = y_pos[30]
    y_border_pos[8] = y_pos[8]
    y_border_pos[19] = y_pos[19]

    #Mapping to 400 x 400
    for i in points_index:
        if 14 <= points_index[i] <= 16 or 42 <= points_index[i] <= 47 or 22 <= points_index[i] <= 26 or 27 <= points_index[i] <= 30 :
            x_pos[i] = int(200 + (x_pos[i] - x_border_pos[30]) * (200 / (x_border_pos[16] - x_border_pos[30])))
            y_pos[i] = int(200 - (-y_pos[i] + y_border_pos[30]) * (200 / (-y_border_pos[24] + y_border_pos[30])))

        if 17 <= points_index[i] <= 21 or 36 <= points_index[i] <= 41 or 0 <= points_index[i] <= 2  :
            x_pos[i] = int(200 - (-x_pos[i] + x_border_pos[30]) * (200 / (x_border_pos[30] - x_border_pos[0])))
            y_pos[i] = int(200 - (-y_pos[i] + y_border_pos[30]) * (200 / (-y_border_pos[19] + y_border_pos[30])))

        if 3 <= points_index[i] <= 8 or 48 <= points_index[i] <= 51 or 57 <= points_index[i] <= 59 or 60 <= points_index[i] <= 61 or points_index[i] == 67 or 31 <= points_index[i] <= 33 or points_index[i] == 62 or points_index[i] == 66:
            x_pos[i] = int(200 - (-x_pos[i] + x_border_pos[30]) * (200 / (x_border_pos[30] - x_border_pos[0])))
            y_pos[i] = int(200 + (y_pos[i] - y_border_pos[30]) * (200 / (y_border_pos[8] - y_border_pos[30])))

        if 9 <= points_index[i] <= 13 or 52 <= points_index[i] <= 56 or 63 <= points_index[i] <= 65 or 34 <= points_index[i] <= 35:
            x_pos[i] = int(200 + (x_pos[i] - x_border_pos[30]) * (200 / (x_border_pos[16] - x_border_pos[30])))
            y_pos[i] = int(200 + (y_pos[i] - y_border_pos[30]) * (200 / (y_border_pos[8] - y_border_pos[30])))
    
    #Save mapped points in points(k).txt
    listFile = open('./point/points{}.txt'.format(k),'w')
    for ctr in points_index:
        listFile.write(str(points_index[ctr]) + "," + str(x_pos[ctr]) + "," + str(y_pos[ctr]) + '\n')
    listFile.close()