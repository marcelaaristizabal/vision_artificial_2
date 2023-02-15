import cv2 as cv
import numpy as np

s = 100

def img_1():
    im = np.zeros((100,100))
    for i in range (s):
        im[i,i] = 255

        cv.imwrite('imagen1.jpg', im)

img_1()

def img_2():
    im = np.zeros ((100,100))
    for i in range (s):
        im[30:70, 30:70] = 255
        im[40:60, 40:60] = 0
        cv.imwrite('imagen2.jpg', im)
img_2()