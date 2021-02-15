"""
*******************************************************************************************************************************************
* TeamId :           2268
* Author :           Amogh Amonkar
* Filename :         Convert_Id_2_Binary
* Theme :            Ant Bot
* Functions :        Get_ID(str), cvt_2_binary(int), main()
* Global Variables : None
*******************************************************************************************************************************************
"""

import cv2
import numpy as np
import cv2.aruco as aruco

"""
*******************************************************************************************************************************************
* Function Name : Get_ID
* Input :         path_of_image -> Path to the required image with ArUco marker(s)
* Output :        List of ids of all the ArUco markers in the given images
* Logic :         Converts image into grayscale and then detects the ID of the ArUco Marker
* Example Call :  ID = Get_ID('Image.jpg')
*******************************************************************************************************************************************
"""
#The following block of code reads ArUco marker and returns ID of the marker
def Get_ID(path_of_image):
    #Reads the image
    img1 = cv2.imread(path_of_image)
    #Convert image from BGR color space to Gray
    gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    #Choose suitable dictionary
    aruco_dict1 = aruco.Dictionary_get(aruco.DICT_4X4_100)
    #Detects parameters for ArUco ID Detection
    parameters1 = aruco.DetectorParameters_create()
    #Identifies ArUco ID
    corners1, ids1, _1 = aruco.detectMarkers(gray1, aruco_dict1, parameters = parameters1)
    #Return the list of ids
    return ids1                                             


"""
*******************************************************************************************************************************************
* Function Name : cvt_2_binary
* Input :         ArUco_ID -> ID of a ArUco Marker
* Output :        Binary number equal to the ArUco Marker ID
* Logic :         1. Divide number by 2
                  2. Store remainder and quotient
                  3. Set Binary Number to 0, Binary Number = Binary Number + (remainde*10**(iteration counter))
                  4. ID = quotient
                  5. Repeat till quotient != 0
* Example Call :  Binary_number = cvt_2_binary(ID)
*******************************************************************************************************************************************
"""
#The snippet of the code below converts a ArUco ID into its binary number
def cvt_2_binary(ArUco_ID, i):
    #Initialize the variable storing binary number as 0
    Binary_num = 0
    #Initializing quotient with any random non zero number
    quotient = 1
    #iteration counter is set to zero
    iteration_cnt = 0

    #While quotient in not equal to zero repeat
    while(quotient != 0):
        #Store remainder of the division
        remainder = (int(ArUco_ID[i][0]) % 2)
        #Store quotient of the division
        quotient = (int(ArUco_ID[i][0]) / 2)
        #Binary Number is intial value + (remainder*10**(iteration counter))
        Binary_num = Binary_num + int(remainder*(10**(iteration_cnt)))
        #ID = quotient of the division
        ArUco_ID[i][0] = int(quotient)
        #Increment in the iteration counter
        iteration_cnt = iteration_cnt + 1       

    #Return the binary number 
    return Binary_num                           


