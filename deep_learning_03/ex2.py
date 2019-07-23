# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:40:10 2019

@author: ch
"""

import numpy as np
import cv2
import random
#  https://www.zybuluo.com/hanbingtao/note/485480
# 给一副图像，随便增加1000个噪点
def salt(img):
    for i in range(1000):
        x = random.randint(0, img.shape[0]-1) # 宽度
        y = random.randint(0, img.shape[1]-1) # 高度
        img[x,y] = [255,255,255]
    return img
def sharp(img):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]) # 锐化算子
    dst = cv2.filter2D(img, -1, kernel=kernel)  # 真正的卷积运算函数
    return dst
img = cv2.imread("butterfly.jpg")
img = salt(img)
blur1 = cv2.blur(img, (5,5))
blur2 = cv2.GaussianBlur(img, (5,5), 0)
blur3 = cv2.medianBlur(img, 5)
res = sharp(blur3)
cv2.imshow("blur1", blur1) # 卷积运算  ，  卷积核（邻域、结构元素）\算子
cv2.imshow("blur2", blur2)
cv2.imshow("blur3", blur3)
cv2.imshow("img", img)
cv2.imshow("sharp", res)
print(img.shape)
cv2.waitKey(0)