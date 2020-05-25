import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lowBlue = np.array([100, 100, 23], np.uint8)
highBlue = np.array([125, 255, 255], np.uint8)


while True:
  ret,frame = cap.read()
  if ret == True:
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV, lowBlue, highBlue)
  
    cv2.imshow('maskBlue', mask)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()