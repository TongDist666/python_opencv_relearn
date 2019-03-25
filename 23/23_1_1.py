# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:09:08 2019

@author: TongDist
"""
'''
Numpy 中的 FFT 包可以帮助我们实现快速傅里叶变换。
函数 np.fft.fft2() 可以对信号进行频率转换，输出结果是一个复杂的数组。
本函数的
    第一个参数是输入图像，要求是灰度格式。
    第二个参数是可选的, 决定输出数组的大小。输出数组的大小和输入图像大小一样。
    如果输出结果比输入图像大，输入图像就需要在进行 FFT 前补0。
    如果输出结果比输入图像小的话，输入图像就会被切割。
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('1.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
# 这里构建振幅图的公式没学过
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image1'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

fshift[int(crow-30):int(crow+30), int(ccol-30):int(ccol+30)] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image2'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()