import cv2
img = cv2.imread('1.jpg', 0)
cv2.imshow('123', img)
while cv2.waitKey(0) & 0xFF != 27:
    print('running!')
cv2.destroyAllWindows()
