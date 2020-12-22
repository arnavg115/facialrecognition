import tensorflow as tf
import numpy as np
import cv2

def prep(img):
    img = cropper(img)
    img = cv2.resize(img,(256,256))
    img = tf.image.rgb_to_grayscale(img)
    return img
def cropper(img):
    return img[100:600, 500:900]
def indiimg(img):
    img = prep(img)
    p = []
    p.append(img)
    p = np.asarray(p)
    return p