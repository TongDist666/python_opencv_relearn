# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:05:43 2019

@author: TongDist
"""

import cv2

img=cv2.imread('1.jpg')
# 下面的 None 本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
# 因此这里为 None
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
#OR
# 这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
height,width=img.shape[:2]
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
while(1):
    cv2.imshow('res',res)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()