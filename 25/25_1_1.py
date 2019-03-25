# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:20:09 2019

@author: TongDist
"""
import cv2
import numpy as np
img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

cv2.namedWindow('img',1)
def nothing(x):
    pass

cv2.createTrackbar('t', 'img', 100, 200, nothing)

while(cv2.waitKey(1)!=27):
    
    t = cv2.getTrackbarPos('t', 'img')
    #lines = cv2.HoughLines(edges,1,np.pi/180,200)
    
    lines = cv2.HoughLines(edges,1,np.pi/180,t)
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.imshow('img', img)

cv2.destroyAllWindows()