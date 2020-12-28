
import os
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
kjl = 500
for img in os.listdir("main"):
    imgl = cv2.imread("main/"+img)
    gray = cv2.cvtColor(imgl, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cord1 = (x,y)
        cord2 = (x+w,y+h)
        cv2.rectangle(imgl, cord1, cord2, (255, 255, 255), 2)
        img = imgl[cord1[1]:cord2[1], cord1[0]:cord2[0]]
        cv2.imwrite("face/"+str(kjl)+".jpg",img)
        kjl+=1
print("DONE")
