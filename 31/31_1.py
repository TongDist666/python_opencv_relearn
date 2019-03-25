# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:19:55 2019

@author: TongDist
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

'''
通常情况下，
    1 输入的应该是灰度图像。
    2 然后确定你想要检测到的角点数目。
    3 再设置角点的质量水平，0到 1 之间。
        它代表了角点的最低质量，低于这个数的所有角点都会被忽略。
    4 最后在设置两个角点之间的最短欧式距离。
    
所有低于质量水平的角点都会被忽略。
然后再把合格角点按角点质量进行降序排列。
函数会采用角点质量最高的那个角点（排序后的第一个），
然后将它附近（最小距离之内）的角点都删掉。
按着这样的方式最后返回 N 个最佳角点。
'''
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
# 返回的结果是 [[ 311., 250.]] 两层括号的数组。
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()