# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:43:24 2019

@author: TongDist
"""

import cv2
import numpy as np

img=cv2.imread('1.jpg')
rows,cols,ch=img.shape
pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])
M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(cols*2,rows*2))
#plt.subplot(121,plt.imshow(img),plt.title('Input'))
#plt.subplot(121,plt.imshow(img),plt.title('Output'))
#plt.show()
while True:
    cv2.imshow('Input',img)
    cv2.imshow('Output',dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()