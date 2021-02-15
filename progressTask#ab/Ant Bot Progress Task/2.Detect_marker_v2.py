import cv2
import numpy as np
import cv2.aruco as aruco
import time as t
cap = cv2.VideoCapture(1)
#img1 = cv2.imread('SIM.jpg')
while(1):
    ret, frame = cap.read()
    gray1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    aruco_dict1 = aruco.Dictionary_get(aruco.DICT_7X7_1000)
    parameters1 = aruco.DetectorParameters_create()
    corners1, ids1, _1 = aruco.detectMarkers(gray1, aruco_dict1, parameters = parameters1)
    for i in ids1:
        print('Img1_ID = ',i)
    t.sleep(0.5)
    cv2.imshow('AR', gray1)
    #if cv2.waitKey(1) == 27:  ## 27 - ASCII for escape key
     #   break
'''
img2 = cv2.imread('ArUco49.jpg')
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
aruco_dict2 = aruco.Dictionary_get(aruco.DICT_4X4_50)
parameters2 = aruco.DetectorParameters_create()
corners2, ids2, _2 = aruco.detectMarkers(gray2, aruco_dict2, parameters = parameters2)
print('Img2_ID = ',ids2)

img3 = cv2.imread('ArUco74.jpg')
gray3 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
aruco_dict3 = aruco.Dictionary_get(aruco.DICT_5X5_250)
parameters3 = aruco.DetectorParameters_create()
corners3, ids3, _3 = aruco.detectMarkers(gray3, aruco_dict3, parameters = parameters3)
print('Img3_ID = ',ids3)

img4 = cv2.imread('ArUco190.jpg')
gray4 = cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
aruco_dict4 = aruco.Dictionary_get(aruco.DICT_5X5_250)
parameters4 = aruco.DetectorParameters_create()
corners4, ids4, _4 = aruco.detectMarkers(gray4, aruco_dict4, parameters = parameters4)
print('Img4_ID = ',ids4)

img5 = cv2.imread('Image1.jpg')
gray5 = cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
aruco_dict5 = aruco.Dictionary_get(aruco.DICT_4X4_100)
parameters5 = aruco.DetectorParameters_create()
corners5, ids5, _5 = aruco.detectMarkers(gray5, aruco_dict5, parameters = parameters5)
print('Image1_ID = ',ids5)
'''
cv2.imshow('AR', gray1)
cv2.waitKey(0)
cv2.destroyAllWindows()
