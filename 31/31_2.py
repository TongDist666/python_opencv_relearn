# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:23:29 2019

@author: TongDist
"""

import numpy as np
import cv2

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('test', 1)

def nothing(x):
    pass
cv2.createTrackbar('point_wei', 'test', 10, 100, nothing)
cv2.createTrackbar('point_num', 'test', 25, 50, nothing)
cv2.createTrackbar('point_jvli', 'test', 10, 50, nothing)

while(cv2.waitKey(1)!=27):
    cimg=img.copy()
    param2=cv2.getTrackbarPos('point_num', 'test')
    param3=cv2.getTrackbarPos('point_wei', 'test')
    param4=cv2.getTrackbarPos('point_jvli', 'test')
    #corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
    corners = cv2.goodFeaturesToTrack(gray,param2,param3/100,param4)
    # 返回的结果是 [[ 311., 250.]] 两层括号的数组。
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(cimg,(x,y),3,255,-1)
    cv2.imshow('test', cimg)
'''
通常情况下，
    1 输入的应该是灰度图像。
    2 然后确定你想要检测到的角点数目。
    3 再设置角点的质量水平，0到 1 之间。
        它代表了角点的最低质量，低于这个数的所有角点都会被忽略。
    4 最后在设置两个角点之间的最短欧式距离。
'''
cv2.destroyAllWindows()
