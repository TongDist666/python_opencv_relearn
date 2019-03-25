# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:11:37 2019

@author: TongDist
"""
import cv2
import numpy as np
img = cv2.imread('1.jpg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
