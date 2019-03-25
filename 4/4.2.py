# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:22:36 2019

@author: TongDist
"""
import numpy as np
import cv2

img=cv2.imread('1.jpg')
cv2.imshow('image',img)

#函数会返回按键的 ASCII 码值
if cv2.waitKey(0)==27:
    print('收到退出命令！！！')
    
    #可以使用 cv2.destroyWindow()，在括号内输入你想删除的窗口名
    cv2.destroyAllWindows()