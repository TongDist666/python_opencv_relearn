# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:29:36 2019

@author: TongDist
"""

import cv2

img=cv2.imread('1.jpg',0)

def nothing(x):
    pass

#预先创建窗口
cv2.namedWindow('THRESH_BINARY')
cv2.namedWindow('THRESH_BINARY_INV')
cv2.namedWindow('THRESH_TRUNC')
cv2.namedWindow('THRESH_TOZERO')
cv2.namedWindow('THRESH_TOZERO_INV')
cv2.namedWindow('img')
#在原图上创建滑动条
cv2.createTrackbar('threshold','img',0,255,nothing)
cv2.imshow('img',img)

while(cv2.waitKey(1)!=27):
    thresh=cv2.getTrackbarPos('threshold','img')
    #输入参数：
    #   1 输入图像 黑白图像
    #   2 阈值
    #   3 阈值改变后的值
    #   4 阈值模式
    ret,thresh1=cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)
    ret,thresh2=cv2.threshold(img,thresh,255,cv2.THRESH_BINARY_INV)
    ret,thresh3=cv2.threshold(img,thresh,255,cv2.THRESH_TRUNC)
    ret,thresh4=cv2.threshold(img,thresh,255,cv2.THRESH_TOZERO)
    ret,thresh5=cv2.threshold(img,thresh,255,cv2.THRESH_TOZERO_INV)
    #显示图像
    cv2.imshow('THRESH_BINARY',thresh1)
    cv2.imshow('THRESH_BINARY_INV',thresh2)
    cv2.imshow('THRESH_TRUNC',thresh3)
    cv2.imshow('THRESH_TOZERO',thresh4)
    cv2.imshow('THRESH_TOZERO_INV',thresh5)

cv2.destroyAllWindows()