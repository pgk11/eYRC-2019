# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  E-Yantra Robotics Competition
*                  ================================
*  This software is intended to check version compatiability of open source software
*  Theme: ANT BOT
*  MODULE: Task1.2
*  Filename: Task1.2.py
*  Version: 1.0.0  
*  Date: October 31, 2018
*  
*  Author: e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""

"""
ArUco ID Dictionaries: 4X4 = 4-bit pixel, 4X4_50 = 50 combinations of a 4-bit pixel image
List of Dictionaries in OpenCV's ArUco library:
DICT_4X4_50	 
DICT_4X4_100	 
DICT_4X4_250	 
DICT_4X4_1000	 
DICT_5X5_50	 
DICT_5X5_100	 
DICT_5X5_250	 
DICT_5X5_1000	 
DICT_6X6_50	 
DICT_6X6_100	 
DICT_6X6_250	 
DICT_6X6_1000	 
DICT_7X7_50	 
DICT_7X7_100	 
DICT_7X7_250	 
DICT_7X7_1000	 
DICT_ARUCO_ORIGINAL

Reference: http://hackage.haskell.org/package/opencv-extra-0.2.0.1/docs/OpenCV-Extra-ArUco.html
Reference: https://docs.opencv.org/3.4.2/d9/d6a/group__aruco.html#gaf5d7e909fe8ff2ad2108e354669ecd17
"""

import numpy as np
import cv2
import cv2.aruco as aruco
import aruco_lib as arc                #To include the file for using the given funtions

def aruco_detect(path_to_image,color,sides):
    '''
    you will need to modify the ArUco library's API using the dictionary in it to the respective
    one from the list above in the aruco_lib.py. This API's line is the only line of code you are
    allowed to modify in aruco_lib.py!!!
    '''
    img = cv2.imread(path_to_image)     #give the name of the image with the complete path
    img2 = cv2.imread(path_to_image)
    id_aruco_trace = 0
    det_aruco_list = {}
    print("Select the type of ArUco Marker \n1. 4X4_100 \n2. 5X5_1000 \n3. 7X7_250 \n")
    code_type = int(input("1, 2 or 3 ? "))
    if( code_type == 1):                #Conditions for appropriate selection of dictionaries
        det_aruco_list = arc.detect_Aruco(img,4,100) #Modified the ArUco fuction so as to accept image, grid size and combination as parameters
    if( code_type == 2):
        det_aruco_list = arc.detect_Aruco(img,5,1000)
    if( code_type == 3):
        det_aruco_list = arc.detect_Aruco(img,7,250)
    print(det_aruco_list)
    if det_aruco_list:
        img_name = 'ArUco' + path_to_image[len(path_to_image) - 5] + '.jpg, '  #Creates file name
        img2 = arc.mark_Aruco(img2,det_aruco_list)
        id_aruco_trace = arc.calculate_Robot_State(img2,det_aruco_list)
        print(id_aruco_trace)
        ID = str(det_aruco_list.keys())
        with open("2268_Task1.2.csv" , 'a+') as file:        #Creates the required csv file
            file.write("\nImage Name, ArUco ID, (x y) Object-1, (x y) Object-2 ") #Starts writiing into csv file
            file.write('\n')
            file.write(img_name)
            file.write(ID[11])
            file.write(', ')
            file.close()

        '''
        Code for triggering color detection on ID detected
        '''
        img_name1 = 'ArUco' + path_to_image[len(path_to_image) - 5] + '.jpg ' #Creates name of the output file
        if(color != 'none'  and  sides != 0):
            color_detect(img2,color,sides,1,img_name1)        #First Shape detection
        
        clr2 = str(input('\n Enter object of 2nd color to be detected R, G or B or none ? \n '))
        shp2 = int(input('\n Also enter the number of sides of required shape Triangle(3), Square(4) or Circle(15) or none(0) \n '))

        if(clr2 != 'none'  and  shp2 != 0): 
            color_detect(img2,clr2,shp2,2,img_name1)
        
def color_detect(img,color,sides,num,name):   #Color should be mentioned as R, G, B and number of sides of the polygon to be detected as int along with number of shape and name of output file
    '''
    code for color Image processing to detect the color and shape of the 2 objects at max.
    mentioned in the Task_Description document. Save the resulting images with the shape
    and color detected highlighted by boundary mentioned in the Task_Description document.
    The resulting image should be saved as a jpg. The boundary should be of 25 pixels wide.
    '''
    if(str(color) == 'G' or str(color) == 'g'):
        lower_color = np.array([30,80,40])                  #Set the lower limits for masking green color
        upper_color = np.array([100,255,255])               #Set the upper limits for masking green color
        clr_f = (255,0,0)
    if(str(color) == 'R' or str(color) == 'r'):
        lower_color = np.array([0,215,215])                 #Set the lower limits for masking Red color

        upper_color = np.array([255,255,255])               #Set the upper limits for masking Red color
        clr_f = (0,255,0)
    if(str(color) == 'R' or str(color) == 'r' or str(color) == 'G' or str(color) == 'g'):   #This block is only applicablr for filtering green or Red color
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)           #Convert the image into HSV color space         
        mask = cv2.inRange(hsv, lower_color, upper_color)   #Mask the image for green color
        ret, thresh = cv2.threshold(mask,127,255,0)         #Threshold the image
        thresh = cv2.medianBlur(thresh,5)
      
    if(str(color) == 'B' or str(color) == 'b'): #This block is only applicable for filtering blue color
        lower_color = np.array([80,20,150])                 #Set the lower limits for masking Blue color
        upper_color = np.array([255,255,220])               #Set the upper limits for masking Blue color
        clr_f = (0,0,255)

        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)           #Convert the image into HSV color space
        mask = cv2.inRange(hsv, lower_color, upper_color)   #Mask the image for green color
        ret, thresh = cv2.threshold(mask,127,255,0)         #Threshold the image

        thresh = cv2.medianBlur(thresh,5)                   #To Cancel the noise

    _,contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   #Contours detection

    
    a = []
    
    f3 = 0
    f4 = 0         # Flags for carryin out shape detection only once
    f15 = 0   
    n = 0
    
    for i in contours:                                      #Loop for shape detection
        l = cv2.arcLength(i,True)
        app_vert = cv2.approxPolyDP(i,0.01*l,True)
        length = len(app_vert)
        if (length > 13 and length < 17):
            length = 15
        if(length == sides ):
            for j in contours:                              #Loop for centroid detection of the required shapes
                vert_1 = cv2.approxPolyDP(j,0.01*l,True)               
                length_1 = len(vert_1)               
                if (length_1 > 14 and length_1 < 17):       #For detection of circle
                    length_1 = 15
                if(length_1 == sides ):                     #Prints centroid only for the required shape
                    M = cv2.moments(j)
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    text = "(" + str(cx) + "," + str(cy) + ")"  #Creates the text for printing coo ordinates
                    text1 = "(" + str(cx) + "  " + str(cy) + ")"
                    if( n < 3):
                        n = n + 1
                        cv2.putText(img,str(text), (cx-20,cy-20), 5, 0.8, (0,0,0), 2)  #Prints the coordinates                  
                        with open("2268_Task1.2.csv" , 'a') as file:
                            file.write(text1)
                            if (num == 1):
                                file.write(', ')
                            file.close()
                        
            if(sides==3 and f3 == 0):
                app_vert = app_vert.reshape((-1,1,2))
                cv2.line(img,(int(app_vert[0][0][0]),int(app_vert[0][0][1])),(int(app_vert[2][0][0]),int(app_vert[2][0][1])),clr_f,25,cv2.LINE_AA)  
                cv2.line(img,(int(app_vert[2][0][0]),int(app_vert[2][0][1])),(int(app_vert[1][0][0]),int(app_vert[1][0][1])),clr_f,25,cv2.LINE_AA) # Draws triangular border around the triangle
                cv2.line(img,(int(app_vert[0][0][0]),int(app_vert[0][0][1])),(int(app_vert[1][0][0]),int(app_vert[1][0][1])),clr_f,25,cv2.LINE_AA)          
                f3 = 1
            if(sides==4 and f4 == 0):
                app_vert = app_vert.reshape((-1,1,2))
                cv2.rectangle(img,(int(app_vert[0][0][0]+6),int(app_vert[0][0][1]+6)),(int(app_vert[2][0][0]-6),int(app_vert[2][0][1]-6)),clr_f,25,cv2.LINE_AA)  #Draws a square after detecting the square
                f4 = 1
            if(sides==15 and f15 == 0):
                cv2.circle(img,(cx,cy),127,clr_f,25) #Draws a circle after detecting the circle
                f15 = 1

    if(num == 2):
        cv2.imwrite(str(name),img)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

if __name__ == "__main__":
    image = str(input('\n Enter the path of the image \n '))
    clr = str(input('\n Enter color of the first image to be detected R, G or B or none ? \n '))
    shp = int(input('\n Enter the number of sides of required shape Triangle(3), Square(4) or Circle(15) or none(0) \n '))
    aruco_detect(image,clr,shp)

