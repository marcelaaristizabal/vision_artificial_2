import cv2 
import numpy as np

img = cv2.imread('cat.jpg')

green_channel = img[:,:,1]

green_channel = np.where(green_channel > 200, 255, green_channel)

img[:, :, 1] = green_channel

mask = green_channel == 255

np.copyto(img[:,:,2], 255, where=mask)

np.copyto(img[:,:,0], 0, where=mask)

def show_img(img):
    cv2.imshow('window', img)
    cv2.waitKey(0)

show_img(img)