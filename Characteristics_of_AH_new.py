"""
*******************************************************************************************************************************************
* TeamId :           2268
* Author :           Amogh Amonkar
* Filename :         Characteristics_of_AH
* Theme :            Ant Bot
* Functions :        Get_AH_Type
* Global Variables : None
*******************************************************************************************************************************************
"""

import cv2
import numpy as np
import cv2.aruco as aruco

"""
*******************************************************************************************************************************************
* Function Name : Get_AH_Type
* Input :         Binary_num -> Binary number equal to ID of ArUco Marker
* Output :        'Q' if AH is QAH, 'R' if AH is RAH
* Logic :         Checks if 7th bit 1 or 0, if 1 return 'Q' else return 'R'
* Example Call :  Type = Get_AH_Type(10101001)
*******************************************************************************************************************************************
"""
#Checks 7th bit of the binary number of the ArUco ID and identifies if it is QAH or RAH
def Get_AH_Type(Binary_num):
    #Convert Binary_number into a string
    #Binary_num = str(Binary_num)
    #Converts Binary_number from string to binary
    Binary_num = int(Binary_num,2)
    #Mask that will separate out bit7
    mask_to_filter_bit7 = '10000000'
    #Converts mask_to_filter_bit7 from string to binary
    mask_to_filter_bit7 = int(mask_to_filter_bit7,2)
    #Separation of the bit 7 by bitwise ANDing Binary_num with the mask
    Type_Flag = (Binary_num & mask_to_filter_bit7)
    #If the 7 bit is one, its decimal equivalent is 128, to convert it into one or zero  
    Type_Flag = int(Type_Flag/128)
    
    #If Flag is set
    if (Type_Flag):
        #Reset the flag
        Type_Flag = 0
        #Return 'Q'
        return 'Q'
    
    #Else return 'R'
    else:                            
        return 'R'

"""
*******************************************************************************************************************************************
* Function Name : Get_AH_Num
* Input :         Binary_num -> Binary number equal to ID of ArUco Marker
* Output :        3, 2, 1 or 0 according to the bit 6 and 5
* Logic :         Checks if 6th and 5th bit is '11','10','01' or '00' accordingly return 3,2,1 or 0
* Example Call :  number = Get_AH_Num(10101001)
*******************************************************************************************************************************************
"""
#Checks 6th and 5th bit of the binary number of the ArUco ID and identifies number of Ant Hill
def Get_AH_Num(Binary_num):
    #Convert Binary_number into a string
    #Binary_num = str(Binary_num)
    #Converts Binary_number from string to binary
    #Binary_num = int(Binary_num,2)
    #Mask that will separate out bit 6 and 5 
    mask_to_filter_bit_6_5 = '01100000'
    #Converts mask_to_filter_bit_6_5 from string to binary
    mask_to_filter_bit_6_5 = int(mask_to_filter_bit_6_5 ,2)
    #Separation of the bit 6 and 5 by bitwise ANDing Binary_num with the mask
    number = int(Binary_num & mask_to_filter_bit_6_5)       

    #If number = 96, decimal of 01100000
    if (int(number) == 96):
        #Return 3
        return 3                        

    #If number = 10, decimal of 01000000
    elif (int(number) == 64):
        #Return 2
        return 2
    
    #If number = 1, decimal of 00100000
    elif (int(number) == 32):
        #Return 1
        return 1
    
    #Else return 0
    else:
        return 0                        

"""
*******************************************************************************************************************************************
* Function Name : Get_AH_Supply_Loc2
* Input :         Binary_num -> Binary number equal to ID of ArUco Marker
* Output :        'W', 'L', 'H' or 0 according to the bit 4 and 3
* Logic :         Checks if 4th and 3rd bit is '11','10','01' or '00' accordingly return 'W','L','H' or 0
* Example Call :  supply2 = Get_AH_Supply_Loc2(10101001)
*******************************************************************************************************************************************
"""
#Checks 4th and 3th bit of the binary number of the ArUco ID and identifies the supply required at location 2
def Get_AH_Supply_Loc2(Binary_num):
    #Convert Binary_number into a string
    #Binary_num = str(Binary_num)
    #Converts Binary_number from string to binary
    Binary_num = int(Binary_num,2)
    #Mask that will separate out bit 4 and 3 
    mask_to_filter_bit_4_3 = '00011000'
    #Converts mask_to_filter_bit_4_3 from string to binary
    mask_to_filter_bit_4_3 = int(mask_to_filter_bit_4_3 ,2)
    #Separation of the bit 4 and 3 by bitwise ANDing Binary_num with the mask
    supply2 = int(Binary_num & mask_to_filter_bit_4_3)

    #If number = 24, decimal of 00011000
    if (int(supply2) == 24):
        #Return 'W'
        return 'W'                      

    #If number = 16, decimal of 00010000
    elif (int(supply2) == 16):
        #Return 'L'
        return 'L'                      

     #If number = 8, decimal of 00001000
    elif (int(supply2) == 8):
        #Return 'H'
        return 'H'                      

    #Else return 0
    else:
        return '0'                       

"""
*******************************************************************************************************************************************
* Function Name : Get_AH_Supply_Loc1
* Input :         Binary_num -> Binary number equal to ID of ArUco Marker
* Output :        'W', 'L', 'H' or 0 according to the bit 2 and 1
* Logic :         Checks if 2nd and 1st bit is '11','10','01' or '00' accordingly return 'W','L','H' or 0
* Example Call :  supply1 = Get_AH_Supply_Loc1(10101001)
*******************************************************************************************************************************************
"""
#Checks 2th and 1th bit of the binary number of the ArUco ID and identifies the supply required at location 1
def Get_AH_Supply_Loc1(Binary_num):
    #Convert Binary_number into a string
    #Binary_num = str(Binary_num)
    #Converts Binary_number from string to binary
    Binary_num = int(Binary_num,2)
    #Mask that will separate out bit 4 and 3 
    mask_to_filter_bit_2_1 = '00000110'
    #Converts mask_to_filter_bit_4_3 from string to binary
    mask_to_filter_bit_2_1 = int(mask_to_filter_bit_2_1 ,2)
    #Separation of the bit 4 and 3 by bitwise ANDing Binary_num with the mask
    supply1 = int(Binary_num & mask_to_filter_bit_2_1)      

    #If number = 6, decimal of 110
    if (int(supply1) == 6):
        #Return 'W'
        return 'W'                      

    #If number = 4, decimal of 100
    elif (int(supply1) == 4):
        #Return 'L'
        return 'L'                      

    #If number = 2, decimal of 10
    elif (int(supply1) == 2):
        #Return 'H'
        return 'H'                      

    #Else return 0
    else:
        return 'O'                        

"""
*******************************************************************************************************************************************
* Function Name : Get_AH_Trash
* Input :         Binary_num -> Binary number equal to ID of ArUco Marker
* Output :        'Q' if AH is QAH, 'R' if AH is RAH
* Logic :         Checks if 0th bit 1 or 0
* Example Call :  Type = Get_AH_Type(10101001)
*******************************************************************************************************************************************
"""
#Checks 0th bit and identifies if it needs cleaning of trash or not
def Get_AH_Trash(Binary_num):
    #Convert Binary_number into a string
    #Binary_num = str(Binary_num)    
    #Converts Binary_number from string to binary
    Binary_num = int(Binary_num,2)  
    #Mask that will separate out bit7
    mask_to_filter_bit0 = '1'       
    #Converts mask_to_filter_bit7 from string to binary
    mask_to_filter_bit0 = int(mask_to_filter_bit0,2)  
    #Separation of the bit 7 by bitwise ANDing Binary_num with the mask
    Trash_Flag = int(Binary_num & mask_to_filter_bit0)

    #Return value of 0th bit
    return Trash_Flag               
    
if (__name__ == '__main__'):
    print(Get_AH_Type(11110001))
    print(Get_AH_Type(1011010))
    print(Get_AH_Type(11101100))
    print(Get_AH_Type(11100111))
    
