import math
#Reading points from data.txt
listFile = open('./points.txt','r')
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

#Save corresponding distance in result.txt
listFile = open('result.txt','w')
for i in range(68):
    for j in range(68):

        #Calculating corresponding distance
        fasele[i][j] = int(math.sqrt(((x_pos[i] - x_pos[j]) ** 2) + ((y_pos[i] - y_pos[j]) ** 2)))
        listFile.write(str(fasele[i][j]) + "\n")
listFile.close()