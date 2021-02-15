import cv2
import numpy as np
cap = cv2.VideoCapture(0)
h2 = 'lowh'
s2 = 'lows'
v2 = 'lowv'
h1 = 'maxh'
s1 = 'maxs'
v1 = 'maxv'
img = np.zeros((300, 500, 3), dtype = np.uint8)
cv2.namedWindow('upper')
cv2.namedWindow('lower')
def h_u(h1):
    #global low_H
    #global high_H
    h1 = val
    h1 = min(h1, h2 + 1)
    cv2.setTrackbarPos(h1, upper, maxh)

def h_l(h2):
    h2 = val
    h2 = min(h1 - 1, h2)
    cv2.setTrackbarPos(h2, lower, lowh)

def s_u(s1):
    s1 = val
    s1 = min(s1, s2 + 1)
    cv2.setTrackbarPos(s1, upper, maxs)
def s_l(s2):
    s2 = val
    s2 = min(s1 - 1, s2)
    cv2.setTrackbarPos(s2, lower, lows)

def v_u(v1):
    v1 = val
    v1 = min(v1, v2 + 1)
    cv2.setTrackbarPos(v1, upper, maxv)

def v_l(v2):
    v2 = val
    v2 = min(v1 - 1, v2)
    cv2.setTrackbarPos(v1, lower, lowv)


cv2.createTrackbar('H1', 'upper', h1, maxh, h_u())
cv2.createTrackbar('S1', 'upper', s1, maxs, s_u())
cv2.createTrackbar('V1', 'upper', v1, maxv, v_u())
cv2.createTrackbar('H2', 'lower', 0, maxh, h_l())
cv2.createTrackbar('S2', 'lower', 0, maxs, s_l())
cv2.createTrackbar('V2', 'lower', 0, maxv, v_l())


while(1):
    #Setting upper nad lower limits
    upper0 = [h1,s1,v1]
    lower0 = [h2,s2,v2]
    #
    
    ## Read the image
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    ## Do the processing
    lower = np.array(lower0)    ## Convert the parameters into a form that OpenCV can understand
    upper = np.array(upper0)
    mask  = cv2.inRange(hsv, lower, upper)
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
