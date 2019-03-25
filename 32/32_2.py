# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:44:46 2019

@author: TongDist
"""

import cv2

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray ,None)

#cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS，
#就会绘制代表关键点大小的圆圈甚至可以绘制除关键点的方向。
img=cv2.drawKeypoints(gray,kp,img,
                      flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('test', img)

cv2.waitKey(0)
cv2.destroyAllWindows()