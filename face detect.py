#Importing face detection libraries
from imutils import face_utils
import dlib
import cv2
import matplotlib.pyplot as plt

#Receiving number of photos that we are going to learn
picture_count = int(input("Picture count of directory: "))

#Later on we will need this string to determine what format our photos are using
pic_format = ""

#Cycling through pictures
for ctr in range (picture_count):

    #Reading each photo indivitually
    address = "shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(address)

	#Coloring nodes for having a better undrestanding of codes mechanism
	#This part does not affect the code itself
    def color(num):
        if num < 17:
            return 'c'
        if num < 22:
            return 'b'
        if num < 27:
            return 'b'
        if num < 31:
            return 'g'
        if num < 36:
            return 'g'
        if num < 42:
            return 'k'
        if num < 48:
            return 'k'
        if num < 60:
            return 'r'
        if num < 68:
            return 'y'

	#Setting pic_format variable depending on
    if 45 <= ctr <= 188:
        pic_format = "bmp"
    else:
        pic_format = "jpg"

	#Grayscaling and preparing the photo for detection
    img = cv2.imread('./images/{}.{}'.format(ctr,pic_format))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rects = detector(gray,0)

	#Getting base image ready for visual representation of output nodes
    im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize = (20,50))
    plt.imshow(im_rgb)

	#Going through nodes
    for (i,rect) in enumerate(rects):

		#Painting a circle for each node
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

		#Writing node numbers beside their circle
        for j, (x,y) in enumerate(shape):
            plt.scatter([x],[y],c=color(j))
            plt.text(x,y,str(j))

			#Using try function to avoid code breakdown due to file opening errors
            try:
                file = open("./data/data{}.txt".format(ctr), "a+")
                file.write("{},{},{}".format(j,x,y) + "\n")
                file.close()
            except Exception as e:
                try:
                    if "[errno 2]" in str(e):
                        file = open("./data/data{}.txt".format(ctr), "w")
                        file.write("{},{},{}".format(j,x,y) + "\n")
                        file.close()
                except:
                    pass
    

    plt.show()
    pass