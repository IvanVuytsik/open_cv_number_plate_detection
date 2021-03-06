import cv2
import numpy as np
#--------------------------------------
frameWidth = 640
frameHeight = 480
plateCascade = cv2.CascadeClassifier("haarcascade_plate_number.xml")
minArea = 500
color = (255,0,255)
count = 0
#---------------------------------------
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,100)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numPlates = plateCascade.detectMultiScale(imgGray, 1.1,4)

    for (x,y,w,h) in numPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x,y),(x+w,y+h), (255,0,255), 2)
            cv2.putText(img, 'NumberPlate', (x,y-10),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgReg = img[y:y+h, x:x+w]
            cv2.imshow("Region", imgReg)

    cv2.imshow("output", img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
       cv2.imwrite('scanned_plates/NoPlate_' + str(count)+".jpg",imgReg)
       cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
       cv2.putText(img,'Scan Saved', (150,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
       cv2.imshow("output", img)
       cv2.waitKey(500)
       count +=1
    elif cv2.waitKey(1) & 0xFF ==ord('q'):
        break