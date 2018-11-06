import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
# def nothing(x):
#     pass
# cv.namedWindow('Contours');
# cv.createTrackbar('H', 'Contours', 10, 255, nothing)
# cv.createTrackbar('S', 'Contours', 77, 255, nothing)
# cv.createTrackbar('V', 'Contours', 185, 255, nothing)
# cv.createTrackbar('X', 'Contours', 26, 255, nothing)
# cv.createTrackbar('Y', 'Contours', 135, 255, nothing)
# cv.createTrackbar('Z', 'Contours', 251, 255, nothing)

while(True):
    ret,frame = cap.read()
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    dp = 2
    min_dist = 20
    param1 = 2;
    param2 = 20;
    
    lowerG = np.array([10,77,185])
    upperG = np.array([26,135,251])
    # lowerG = np.array([cv.getTrackbarPos('H', 'Contours'),cv.getTrackbarPos('S', 'Contours'),cv.getTrackbarPos('V', 'Contours')])
    # upperG = np.array([cv.getTrackbarPos('X', 'Contours'),cv.getTrackbarPos('Y', 'Contours'),cv.getTrackbarPos('Z', 'Contours')])

    gold = cv.inRange(hsv, lowerG, upperG)
    goldBlur = cv.GaussianBlur(gold,(9,9),50)
    im,contours,_ = cv.findContours(goldBlur, mode=cv.RETR_CCOMP, method=cv.CHAIN_APPROX_NONE)
    sorted(contours, key=cv.contourArea, reverse=True)

    if not contours:
        cx,cy = 0,0
    else:
        M = cv.moments(contours[0])
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0
    cv.circle(frame, (cx,cy), 2, (255,0,0), thickness=80)

    
    y,x,_ = frame.shape
    position = 0
    if(cx >= 0 and cx < (x/3)):
        position = 1
    elif (cx >= (x/3) and cx < (2*(x/3))):
        position = 2
    else:
        position = 3
    

    print("GOLD: %s %s     %s" %(cx,cy,position))


    cv.imshow("Gold", im)
    cv.imshow('Image',frame)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
