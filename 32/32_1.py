# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:37:16 2019

@author: TongDist
"""

import cv2

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray ,None)

img = cv2.drawKeypoints(gray, kp, img)
cv2.imshow('test', img)

cv2.waitKey(0)
cv2.destroyAllWindows()