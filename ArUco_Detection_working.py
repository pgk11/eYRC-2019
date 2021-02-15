import cv2
import numpy as np
import cv2.aruco as aruco
import Characteristics_of_AH_new as CAH
#import SIM_Array as SA

ID = []
ID1 = [0, 0, 0, 0]
biN = []
SIM0 = []
SIM1 = []
SIM2 = []
SIM3 = []
SIM = [SIM0, SIM1, SIM2, SIM3]
#Type =
mask34 = '00011000'
mask12 = '00000110'
aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_1000)  #Sets the dictionary for the required ArUco id 
parameters = aruco.DetectorParameters_create()          #Detects the parameter required for detection
count = None
cap = cv2.VideoCapture(0)                                #Starts the video recording
while(1):
    ret, frame = cap.read()                              #Read the captured image
    count = 0    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)        #Converts the image into the grayscale image                       
    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters = parameters)    #Retrival of id from the marker
    ids = np.array(ids)

    if(ids.all() == None):
        pass
    else:
        for i in ids:
            for j in ID:
                if(i[0] == j):
                    count += 1
            if(count == 0 and len(ID) <= 4):
                ID.append(int(i))                
            #print(i[0])        
    print(ID)
    cv2.imshow('Amogh', frame)#Display image
    if(len(ID) < 4):
        continue
    #To sort IDs wrt ah_num
    for i in range (0,4):
        if(CAH.Get_AH_Num(ID[i]) == 0 and ID1[0] == 0):
            ID1[0] = ID[i]
       
    for i in range (0,4):
        if(CAH.Get_AH_Num(ID[i]) == 1 and ID1[1] == 0):
            ID1[1] = ID[i]
        
    for i in range (0,4):
        if(CAH.Get_AH_Num(ID[i]) == 2 and ID1[2] == 0):
            ID1[2] = ID[i]
        
    for i in range (0,4):
        if(CAH.Get_AH_Num(ID[i]) == 3 and ID1[3] == 0):
            ID1[3] = ID[i]
    for i in range (0, 4):
        SIM[i].extend((ID1[i]))
    for i in range (0,4):
        if(ID1[i]>127):
            SIM[i].append('Q')
        elif(ID1[i]<128):
            SIM[i].append('R')
    #convert to binary
    for i in range(0,4):
        biN.append(format(ID1[i], '08b'))
        '''
    for i in range (0,4):
        s2 = biN[i] & mask34
        if(int(s2) == 24):
            SIM[i].append('W')
        if(int(s2) == 16):
            SIM[i].append('L')
        if(int(s2) == 8):
            SIM[i].append('H')
        if(int(s2) == 0):
            SIM[i].append('0')
    for i in range (0,4):
        s1 = biN[i] & mask12
        if(int(s2) == 6):
            SIM[i].append('W')
        if(int(s2) == 4):
            SIM[i].append('L')
        if(int(s2) == 2):
            SIM[i].append('H')
        if(int(s2) == 0):
            SIM[i].append('0')
            '''
    for i in range (0,4):
        if(ID1[i]%2 == 1):
            SIM[i].append('T')
        else:
            SIM[i].append('0')
    
            
            
    
    
    '''
    # Read Return Value of Ah Type
    j = 0
    for j in range(4):
        CAH.Get_AH_Type(biN[j])
        j += 1
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
    if(cv2.waitKey(1) == 27):       #Wait till escape key is pressed
        break;
        '''
    if(ID1[0] != 0 and ID1[1] != 0 and ID1[2] != 0 and ID1[3] != 0):
        break
print(ID1)
#SA.IDdATA(ID1)
'''
SIM0.extend(str(ID1[0]))
SIM0.append(char.Get_AH_Type[0])
SIM0.append(char.Get_AH_Supply_Loc2(ID1[0]))
SIM0.append(char.Get_AH_Supply_Loc1(ID1[0]))
SIM0.append(char.Get_AH_Trash[0])
SIM1.extend(str(ID1[1]))
SIM1.append(char.Get_AH_Type[1])
SIM1.append(char.Get_AH_Supply_Loc2(ID1[1]))
SIM1.append(char.Get_AH_Supply_Loc1(ID1[1]))
SIM1.append(char.Get_AH_Trash[1])
SIM2.extend(str(ID1[2]))
SIM2.append(char.Get_AH_Type[2])
SIM2.append(char.Get_AH_Supply_Loc2(ID1[2]))
SIM2.append(char.Get_AH_Supply_Loc1(ID1[2]))
SIM2.append(char.Get_AH_Trash[2])
SIM3.extend(str(ID1[3]))
SIM3.append(char.Get_AH_Type[3])
SIM3.append(char.Get_AH_Supply_Loc2(ID1[3]))
SIM3.append(char.Get_AH_Supply_Loc1(ID1[3]))
SIM3.append(char.Get_AH_Trash[3])
#
print(SIM0)
print(SIM1)
print(SIM2)
print(SIM3)
'''
print(SIM)
cap.release()                       #Terminate the reading of image
cv2.destroyAllWindows()             #Close all the windows


