import cv2
import numpy as np
import cv2.aruco as aruco
import Characteristics_of_AH as CAH
import Convert_Id_2_Binary as D2B
import csv
import serial as ser
# Indivisual SIM Arrays 
SIM0 = [] 
SIM1 = []
SIM2 = []
SIM3 = []

ser = ser.Serial('COM4', 9600)
#data = ser.Serial('COM7', 9600)
AH_Num = []
AH_Trash =[]
a = [] # SIM ID's
biN = [] # ID's Converted to binary
img1 = cv2.VideoCapture(0)
ret, frame = img1.read()
gray1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
aruco_dict1 = aruco.Dictionary_get(aruco.DICT_7X7_1000)
parameters1 = aruco.DetectorParameters_create()
corners1, ids1, _1 = aruco.detectMarkers(gray1, aruco_dict1, parameters = parameters1)
# Take the SIM ids in an array
for i in ids1:
    print('Img1_ID = ',i)
    #a.append(i)
    a.extend(i)
#Set 'j' counter to 0
j = 0
# Convert ids in Binary
for j in range(4):
    biN.append(format(a[j], '08b'))
    j += 1
# Convert the numbers into string
for j in range(4):
    a[j] = str(a[j])
    j += 1
j = 0

#print(biN)
j=0
# Read Return Value of Ah Type
for j in range(4):
    CAH.Get_AH_Type(biN[j])
    j += 1
j = 0
#Read Return of AH Number
for j in range(4):
    CAH.Get_AH_Num(biN[j])
    j += 1
j = 0
# Convert AH number into string
for j in range(4):
    AH_Num.extend(str(CAH.Get_AH_Num(biN[j])))
    j +=1
j = 0
for j in range(4):
    CAH.Get_AH_Supply_Loc2(biN[j])
    j += 1
j = 0
for j in range(4):
    CAH.Get_AH_Supply_Loc1(biN[j])
    j += 1
j = 0
for j in range(4):
    CAH.Get_AH_Trash(biN[j])
    j += 1
j = 0
for j in range(4):
    AH_Trash.extend(str(CAH.Get_AH_Trash(biN[j])))
    j += 1
j = 0
# Write a value in each SIM array
SIM0.extend(CAH.Get_AH_Type(biN[0]))
SIM1.extend(CAH.Get_AH_Type(biN[1]))
SIM2.extend(CAH.Get_AH_Type(biN[2]))
SIM3.extend(CAH.Get_AH_Type(biN[3]))
# Add Values in each SIM arrays
SIM0.append(a[0])
SIM0.append(AH_Num[0])
SIM0.append(CAH.Get_AH_Supply_Loc2(biN[0]))
SIM0.append(CAH.Get_AH_Supply_Loc1(biN[0]))
SIM0.append(AH_Trash[0])
SIM1.append(a[1])
SIM1.append(AH_Num[1])
SIM1.append(CAH.Get_AH_Supply_Loc2(biN[1]))
SIM1.append(CAH.Get_AH_Supply_Loc1(biN[1]))
SIM1.append(AH_Trash[1])
SIM2.append(a[2])
SIM2.append(AH_Num[2])
SIM2.append(CAH.Get_AH_Supply_Loc2(biN[2]))
SIM2.append(CAH.Get_AH_Supply_Loc1(biN[2]))
SIM2.append(AH_Trash[2])
SIM3.append(a[3])
SIM3.append(AH_Num[3])
SIM3.append(CAH.Get_AH_Supply_Loc2(biN[3]))
SIM3.append(CAH.Get_AH_Supply_Loc1(biN[3]))
SIM3.append(AH_Trash[3])
# Create a SIM list Containing all indivisual SIM lists
SIM = [SIM0, SIM1, SIM2, SIM3]
print(SIM)
ser.
