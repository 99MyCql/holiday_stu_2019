#encoding = utf-8
import  cv2

img = cv2.imread("j.jpg", 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# 卷积核、结构体元素
#dilation = cv2.dilate(src=img, kernel=kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
eroded = cv2.erode(img, kernel, iterations=1)
open = cv2.dilate(eroded, kernel, iterations=1)

gradient = dilation - eroded

gradient2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("src", img)
# cv2.imshow("dilate", dilation)
# cv2.imshow("erode", eroded)
# cv2.imshow("open", open)          # ctrl + /
cv2.imshow("gradient", gradient)
cv2.imshow("gradient2", gradient2)
cv2.waitKey(0)
