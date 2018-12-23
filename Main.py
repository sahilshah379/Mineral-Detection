import time
import numpy as np
import cv2 as cv
import WhiteBalance

cap = cv.VideoCapture(0)
#def nothing(x):
#     pass
#cv.namedWindow('Gold');
#cv.createTrackbar('H', 'Gold', 10, 255, nothing)
#cv.createTrackbar('S', 'Gold', 75, 255, nothing)
#cv.createTrackbar('V', 'Gold', 200, 255, nothing)
#cv.createTrackbar('X', 'Gold', 25, 255, nothing)
#cv.createTrackbar('Y', 'Gold', 135, 255, nothing)
#cv.createTrackbar('Z', 'Gold', 255, 255, nothing)

start = int(round(time.time() * 1000))
end = int(round(time.time() * 1000))

sum = 0
count = 0

while((end-start) < 5000):
    ret,frame = cap.read()
    img = WhiteBalance.gray_world(frame)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    dp = 2
    min_dist = 20
    param1 = 2;
    param2 = 20;
    
    lowerG = np.array([10,75,200])
    upperG = np.array([25,135,255])
#    lowerG = np.array([cv.getTrackbarPos('H', 'Gold'),cv.getTrackbarPos('S', 'Gold'),cv.getTrackbarPos('V', 'Gold')])
#    upperG = np.array([cv.getTrackbarPos('X', 'Gold'),cv.getTrackbarPos('Y', 'Gold'),cv.getTrackbarPos('Z', 'Gold')])

    gold = cv.inRange(hsv, lowerG, upperG)
    goldBlur = cv.GaussianBlur(gold,(9,9),50)
    im,contours,_ = cv.findContours(goldBlur, mode=cv.RETR_CCOMP, method=cv.CHAIN_APPROX_NONE)
    sorted(contours, key=cv.contourArea, reverse=True)
    print(len(contours))
    if not contours:
        cx,cy = 0,0
    else:
        M = cv.moments(contours[0])
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0
    cv.circle(img, (cx,cy), 2, (255,0,0), thickness=80)

    
    y,x,_ = img.shape
    position = 0
    if(cx >= 0 and cx < (x/3)):
        position = 1
    elif (cx >= (x/3) and cx < (2*(x/3))):
        position = 2
    else:
        position = 3
    

#    print("GOLD: %s %s     %s" %(cx,cy,position))
    sum += position
    count += 1
    end = int(round(time.time() * 1000))

    cv.imshow('Gold', im)
    cv.imshow('Balanced',img)
    cv.imshow('Normal',frame)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
avg = round(sum/count)
print(avg)
