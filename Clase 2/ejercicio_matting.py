import cv2
import numpy as np

imageF = cv2.imread('test_im.jpg')
imageA = cv2.imread('test_im-A.jpg')
imageB = cv2.imread('sky.jpg')

mask1 = imageA[:,:,0] <= 30
mask2 = imageA[:,:,1] <= 30
mask3 = imageA[:,:,2] <= 30

#1
np.copyto(imageF[:,:,0], imageB[:,:,0], where=mask1)
np.copyto(imageF[:,:,1], imageB[:,:,1], where=mask2)
np.copyto(imageF[:,:,2], imageB[:,:,2], where=mask3)

def show_img(img):
    cv2.imshow('Result', img)
    cv2.waitKey(0)

show_img(imageF)