import cv2
import tensorflow as tf
from tensorflow import keras
import numpy
import os
from tensorflow.python.keras import models

model = models.load_model('model.h5')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
categories = os.listdir('image_data/')
while True:
    abc, imgs = cap.read()
    gray = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cord1 = (x,y)
        cord2 = (x+w,y+h)

        cv2.rectangle(imgs, cord1, cord2, (255, 255, 255), 2)
        img = imgs[cord1[1]:cord2[1], cord1[0]:cord2[0]]
        unmodded = img
        img = cv2.resize(img,(256,256))
        pl = []
        pl.append(img)
        pl = numpy.asarray(pl)
        predictions = model.predict(pl)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strg = categories[int(numpy.argmax(predictions[0]))]
        cv2.putText(imgs,strg,cord1, font, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", imgs)
    cv2.waitKey(1)
