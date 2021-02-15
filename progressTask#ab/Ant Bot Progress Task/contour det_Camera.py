import numpy as np
import cv2
img =  cv2.VideoCapture(0)
while(1):
    #color detection
    ret, frame = img.read()
    
    upper0 = [127, 255, 155]
    lower0 = [92, 111, 63]
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower = np.array(lower0)
    upper = np.array(upper0)
    mask  = cv2.inRange(hsv, lower, upper)
    mask = cv2.medianBlur(mask, 5)
    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    #contour detection
    '''
    bgr = cv2.cvtColor(mask,cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    '''
    _,ctrs,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    final = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    final = cv2.medianBlur(final, 3)
    cv2.drawContours(final, ctrs, 0,(255, 0 ,0), 3)
    if (ctrs == 1):
        for i in ctrs:
            M = cv2.moments(i)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
        cv2.imshow('image', final)
    print(cx, cy)

    
    if cv2.waitKey(1) == 27:
        break

