# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:36:20 2019

@author: TongDist
"""
'''
cv2.HoughCircles(image, method, 
                 dp, minDist, 
                 circles=None, 
                 param1=None, param2=None, 
                 minRadius=None, maxRadius=None)

其中：
    image:8位，单通道图像。如果使用彩色图像，需要先转换为灰度图像。
    method：定义检测图像中圆的方法。目前唯一实现的方法是cv2.HOUGH_GRADIENT。
    dp：累加器分辨率与图像分辨率的反比。dp获取越大，累加器数组越小。
    minDist：检测到的圆的中心，（x,y）坐标之间的最小距离。
        如果minDist太小，则可能导致检测到多个相邻的圆。
        如果minDist太大，则可能导致很多圆检测不到。
    param1：用于处理边缘检测的梯度值方法。
    param2：cv2.HOUGH_GRADIENT方法的累加器阈值。阈值越小，检测到的圈子越多。
    minRadius：半径的最小大小（以像素为单位）。
    maxRadius：半径的最大大小（以像素为单位）。

'''

import cv2
import numpy as np
img = cv2.imread('1.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

def nothing(x):
    pass

cv2.namedWindow('hough',1)
cv2.createTrackbar('minDist', 'hough',10,100,nothing)
cv2.createTrackbar('param1', 'hough',50,100,nothing)
cv2.createTrackbar('param2', 'hough',30,60,nothing)
cv2.createTrackbar('minRadius', 'hough',0,50,nothing)


while(cv2.waitKey(1)!=27):
    img_copy = cimg.copy()
    minDist_0 = cv2.getTrackbarPos('minDist', 'hough')
    param1_0 = cv2.getTrackbarPos('param1', 'hough')
    param2_0 = cv2.getTrackbarPos('param2', 'hough')
    minRadius_0 = cv2.getTrackbarPos('minRadius', 'hough')
    maxRadius_0 = cv2.getTrackbarPos('maxRadius', 'hough')
    
    try:
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist_0,
                               param1=param1_0,param2=param2_0,
                               minRadius=minRadius_0,maxRadius=100)
        #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                   #param1=50,param2=30,minRadius=0,maxRadius=0)
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(img_copy,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(img_copy,(i[0],i[1]),2,(0,0,255),3)
        cv2.imshow('hough',img_copy)
    except:
        print('something wrong!!!')
        continue

cv2.destroyAllWindows()

