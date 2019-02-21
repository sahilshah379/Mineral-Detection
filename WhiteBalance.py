import cv2 as cv
import numpy as np

def display(img):

	while True:
		images = np.concatenate(img, axis=0)
		cv.imshow('images', images)
		k = cv.waitKey(30) & 0xff
		if k == 27:
			break

def gray_world(img):
	lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
	l = 0.0
	a = 0.0
	b = 0.0
	count = 0
	for x in range(0,len(lab)):
		for y in range(0,len(lab[x])):
			l += lab[x][y][0]
			a += lab[x][y][1]
			b += lab[x][y][2]
			count += 1
	l /= count
	a /= count
	b /= count

	for x in range(0,len(lab)):
		for y in range(0,len(lab[x])):
			lab[x][y][1] = lab[x][y][1] - round((a-128)*(lab[x][y][0]/255))
			lab[x][y][2] = lab[x][y][2] - round((b-128)*(lab[x][y][0]/255))
	print("balanced!")
	new = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
	return new

def true_white(img):
	lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
	lowerW = np.array([190,0,0])
	upperW = np.array([255,256,256])
	gray = cv.inRange(lab, lowerW, upperW)
	erode = cv.erode(gray, np.ones((5,5), np.uint8), iterations=1)

	blur = cv.GaussianBlur(erode,(9,9),50)
	unboundContours,_ = cv.findContours(blur, mode=cv.RETR_CCOMP, method=cv.CHAIN_APPROX_NONE)
	deviation = 0.35
	contours = []
	for c in range(0,len(unboundContours)):
		cont = unboundContours[c]
		x,y,w,h = cv.boundingRect(cont)
		ratio = max(w,h)/min(w,h)
		if (ratio < (1+deviation)) and (ratio > (1-deviation)):
			contours.append(unboundContours[c])
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
	white = lab[cy,cx].copy()
	for y in range(0,len(lab)):
		for x in range(0,len(lab[y])):
			lab[y][x][1] = round(lab[y][x][1] - ((white[1]-128)*(lab[y][x][0]/255.0)))
			lab[y][x][2] = round(lab[y][x][2] - ((white[2]-128)*(lab[y][x][0]/255.0)))
	print("balanced!")
	new = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
	cv.circle(new, (cx,cy), 10, (255, 0, 0), 5)
	return new

if __name__ == "__main__":
	img = cv.imread('ftc1.jpg', 1)
	img = img[round(img.shape[0]*.45):img.shape[0], 0:img.shape[1]]
	img1 = gray_world(img)
	img2 = true_white(img)
	display((img,img1,img2))
