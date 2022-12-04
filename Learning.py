import math

#Receiving number of photos that we are going to learn
picture_count = int(input("Picture count of directory: "))

#Cycling through points
for ctr in range(picture_count):

    #Reading points from data(k).txt
    listFile = open('./point/points{}.txt'.format(ctr),'r')
    file = listFile.read()
    lines = list(file.split("\n"))
    points_index = []
    x_pos = []
    y_pos = []

    for i in range(len(lines) - 1): 
        cleanedRow = list(lines[i].split(','))
        cleanedRow[-1] = cleanedRow[-1].replace('\n','')
        points_index.append(int(cleanedRow[0]))
        x_pos.append(int(cleanedRow[1]))
        y_pos.append(int(cleanedRow[2]))
    listFile.close()

    fasele = [[0] * 68] * 68

    #Save corresponding distance in fasele(p).txt
    listFile = open('./fasele/fasele{}.txt'.format(ctr),'w')
    for i in range(68):
        for j in range(68):

            #Calculating corresponding distance
            fasele[i][j] = int(math.sqrt(((x_pos[i] - x_pos[j]) ** 2) + ((y_pos[i] - y_pos[j]) ** 2)))
            listFile.write(str(fasele[i][j]) + "\n")
    listFile.close()

    #Save corresponding feelings in feeling(p).txt
    feeling = input("whats the feeling for image {}?".format(ctr))
    listfile = open('./feeling/feeling{}.txt'.format(ctr),'w')
    listfile.write(feeling)
    listfile.close()