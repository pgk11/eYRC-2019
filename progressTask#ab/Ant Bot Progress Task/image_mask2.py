import cv2
import numpy as np
cap = cv2.VideoCapture(1)

#img = np.zeros((300, 500, 3), dtype = np.uint8)
#cv2.namedWindow('upper')
#cv2.namedWindow('lower')
#cv2.createTrackbar('R1', 'upper', 0, 255, r_u())
#cv2.createTrackbar('G1', 'upper', 0, 255, g_u())
#cv2.createTrackbar('B1', 'upper', 0, 255, b_u())
#cv2.createTrackbar('R2', 'lower', 0, 255, r_l())
#cv2.createTrackbar('G2', 'lower', 0, 255, g_l())
#cv2.createTrackbar('B2', 'lower', 0, 255, b_l())


while(1):
    #Setting upper nad lower limits
    #for blue
    upper0 = [127, 255, 155]
    #adjust saturation value corresponding to light conditions; the middle value in the bracket
    lower0 = [92, 111, 63]
    # check for the doc for red, green, and yellow ranges
    
    
    ## Read the image
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    ## Do the processing
    lower = np.array(lower0)    ## Convert the parameters into a form that OpenCV can understand
    upper = np.array(upper0)
    mask  = cv2.inRange(hsv, lower, upper)
    mask = cv2.medianBlur(mask, 5)
    #res   = cv2.bitwise_and(frame, frame, mask= mask)
    ## Show the image
    cv2.imshow('image',frame)
    cv2.imshow('mask',mask)
    

    ## End the video loop
    if cv2.waitKey(1) == 27:  ## 27 - ASCII for escape key
        break
############################################

############################################
## Close and exit
cap.release()
cv2.destroyAllWindows()
