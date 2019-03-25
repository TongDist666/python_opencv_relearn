# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:33:05 2019

@author: TongDist
"""

# -*- coding: utf-8 -*-

import cv2
import numpy as np

#mouse callback function
count=0
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global count
        print('第'+str(count+1)+'次点击  x坐标：'+str(x))
        print('第'+str(count+1)+'次点击  y坐标：'+str(y))
        count=count+1
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()