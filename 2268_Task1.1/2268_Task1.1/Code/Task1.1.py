# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  E-Yantra Robotics Competition
*                  ================================
*  This software is intended to check version compatiability of open source software
*  Theme: ANT BOT
*  MODULE: Task1.1
*  Filename: Task1.1.py
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
"""

import numpy
import cv2
import cv2.aruco as aruco

def aruco_gen(id_aruco, num_pixels, grid_size, num_comb):                                                    
    text = 'ArUco ID = '                                                                #Text to be displayed on the image
    name = 'ArUco' + str(id_aruco) + '.jpg'                                             #Name by which the file is to be saved
    color = [0,0,255]                                                                   #Color of the text on the image
    
    if(grid_size<4 or grid_size>7):
        print('Error : Please enter any grid size between 4 to 7.')        
        
    if(num_comb <= id_aruco):
        print('Error : Please make sure num_comb > id_aruco.')
            
    if(grid_size == 4 and num_comb == 50):                                              #Conditions to choose appropriate dictionary
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    if(grid_size == 4 and num_comb == 100):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
    if(grid_size == 4 and num_comb == 250):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    if(grid_size == 4 and num_comb == 1000):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    if(grid_size == 5 and num_comb == 50):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_50)
    if(grid_size == 5 and num_comb == 100):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_100)
    if(grid_size == 5 and num_comb == 250):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
    if(grid_size == 5 and num_comb == 1000):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_1000)
    if(grid_size == 6 and num_comb == 50):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_50)
    if(grid_size == 6 and num_comb == 100):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_100)
    if(grid_size == 6 and num_comb == 250):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    if(grid_size == 6 and num_comb == 1000):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_1000)
    if(grid_size == 7 and num_comb == 50):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_50)
    if(grid_size == 7 and num_comb == 100):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_100)
    if(grid_size == 7 and num_comb == 250):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_250)
    if(grid_size == 7 and num_comb == 1000):
        aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_1000)                    

    img = aruco.drawMarker(aruco_dict, id_aruco, num_pixels)                                #Draw a marker with parameters as dictionary, ID, length & width in pixels

    mod_img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)                                          #Convert image from Gray scale to color
    cv2.rectangle(mod_img,(12,12),(int(num_pixels-12),int(num_pixels-12)),(255,255,255),25) #Draw frame on the image

    font = 5                                                                                #Set font to FONT_HERSHEY_COMPLEX_SMALL = 5
    cv2.putText(mod_img, str(text), (int((num_pixels/2)-90),17), font, 1, color, 2)         #Put text along the central axis of the image  
    cv2.putText(mod_img, str(id_aruco), (int((num_pixels/2)+60),17), font, 1, color, 2)

    cv2.imwrite(name,mod_img)                                                               #Save image as name.jpg

    cv2.imshow('Image',mod_img)                                                             #Display the marker

    cv2.waitKey(0)
    '''
    code here for saving the Aruco image as a "jpg" by following the steps below:
    1. save the image as a colour RGB image in OpenCV color image format
    2. embed a boundary of 25 pixels on all four sides and three channels of the image
    3. save the image as "ArUcoID.jpg" where ID is the digits of id_aruco i.e. if the ID is 26 the name should be: ArUco26.jpg
    4. APIs which are permitted to be used are:
    a. cvtColor
    b. imwrite
    and other OpenCV APIs.
    5. You are permitted to modify n, C and variables id_aruco and num_pixels
    '''

    cv2.destroyAllWindows()


if __name__ == "__main__":    
    aruco_gen(10, 400, 4, 50)
    aruco_gen(49, 400, 4, 50)
    aruco_gen(74, 400, 5, 250)
    aruco_gen(190, 400, 5, 250)
