# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:43:39 2019

@author: TongDist
"""

import cv2
import numpy as np

img=cv2.imread('1.jpg')
rows,cols,ch=img.shape

#需要一个变换矩阵
#从原图中三个点   映射到输出图像中的三个点
pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])
M=cv2.getAffineTransform(pts1,pts2)

#参数：
#   1 原图
#   2 变换矩阵
#   3 一个元组  指定输出图像的尺寸
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('output',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
