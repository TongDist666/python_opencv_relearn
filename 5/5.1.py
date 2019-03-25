import cv2

cap = cv2.VideoCapture(0)
while cv2.waitKey(1) & 0xFF != 27:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('123', gray)
cap.release()
cv2.destroyAllWindows()
