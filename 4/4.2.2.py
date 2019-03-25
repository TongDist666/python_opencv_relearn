import cv2
img = cv2.imread('1.jpg', 0)
# 参数用 cv2.WINDOW_AUTOSIZE窗口大小不可调整
cv2.namedWindow('named_window', cv2.WINDOW_NORMAL)
cv2.imshow('named_window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
