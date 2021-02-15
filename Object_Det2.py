"""
*******************************************************************************************************************************************
* TeamId :           2268
* Author :           Amogh Amonkar, Priyan Kotwal
* Filename :         Object Detection
* Theme :            Ant Bot
* Functions :        None
* Global Variables : None
*******************************************************************************************************************************************
"""


import numpy as np
import cv2

img =  cv2.VideoCapture(0)
while(1):
    ret, frame = img.read()
    if frame is None:
        break    
    upper0 = [109, 255, 255]                             #Setting the threshold for color filterring
    lower0 = [90, 163, 168]
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)          #Converting the image from RGB Color space to HSV
    lower = np.array(lower0)
    upper = np.array(upper0)
    mask  = cv2.inRange(hsv, lower, upper)               #Filtering the desired color 
    ret, thresh = cv2.threshold(mask, 127, 255, 0)       #Binarization of the image
    thresh = cv2.medianBlur(thresh, 5)                   #Blurring the image for noise cancellation

    _,contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  #Detect the contours

    final = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)     #Converting the image back to RGB colorspace
    cv2.drawContours(final, contours, -1,(255, 0 ,0), 3) #Drawing the contours

    center = None

    if len(contours) > 0:                                #Proceed only if at least one contour is detected
        L_contour = max(contours, key=cv2.contourArea)          #Finding the largest contour in the mask
        ((x, y), radius) = cv2.minEnclosingCircle(L_contour)    #Find smallest circle enclosing the object
        M = cv2.moments(L_contour)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))        #Marking the centroid
        
        if radius > 10:                                                      #If the radius is bigger than the required size proceed
            #cv2.circle(final, (int(x), int(y)), int(radius),(0, 255, 255), 2)#Draw the circle and centroid on the frame,
            cv2.circle(final, center, 3, (0, 0, 255), -1)                   
            print(center)
            if(int(x) < 300):
                side = 'L'
            elif(int(x) >= 300):
                side = 'R'
            print(side)
    
    cv2.imshow('image', final)
    
    if cv2.waitKey(1) == 27:
        break

img.release()
cv2.destroyAllWindows()
