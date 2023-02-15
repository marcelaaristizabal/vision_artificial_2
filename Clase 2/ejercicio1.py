import numpy as np 
import cv2 as cv 

W = 500
H = 500

def show_im(im):
    cv.imshow('window', im)
    cv.waitKey(0)

def draw (triangle, im, color = (255,0, 0)):
    cv.drawContours(im, [triangle.astype(int)], 0, color, -1)

def translate(triangle, dx, dy):
    t = np.array([dx, dy])
    return triangle + t

def scale (triangle, dx, dy):
    s= np.array([dx, dy])
    return triangle * s

def rotation (triangle, angle):
    r = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    return triangle @ r

im = np.zeros([W, H, 3], np.uint8)
triangle = np.array([[10, 10],[70,10],[40,60]])
draw(triangle,im)
t1= translate (triangle, 500, 350)
e1= scale (triangle, 2, 2)
r1 = rotation (e1, 50)
draw(r1,im, color=(0, 0, 255))

show_im(im)