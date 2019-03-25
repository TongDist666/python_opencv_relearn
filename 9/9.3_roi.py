# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:31:48 2019

@author: TongDist
"""

import cv2
img=cv2.imread("1.jpg")
cv2.imshow("ROI",img[150:160,150:160])
cv2.imshow("ROI1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()