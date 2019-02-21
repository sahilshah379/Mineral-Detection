import cv2 as cv
import numpy as np

def nothing(x):
    pass

def clahe(img, limit, grid):
	lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
	l,a,b = cv.split(lab)
	clahe = cv.createCLAHE(clipLimit=limit, tileGridSize=(grid,grid))
	cl = clahe.apply(l)
	lab1 = cv.merge((cl,a,b))
	new = cv.cvtColor(lab1, cv.COLOR_LAB2BGR)
	return new

if __name__ == "__main__":
	cv.namedWindow('Clahe');
	cv.createTrackbar('Clip Limit', 'Clahe', 3, 100, nothing)
	cv.createTrackbar('Grid Size', 'Clahe', 8, 100, nothing)
	
	img = cv.imread('ftc2.jpg', 1)
	img = cv.warpAffine(img, cv.getRotationMatrix2D((img.shape[1]/2,img.shape[0]/2), 180, 1.0), (img.shape[1], img.shape[0])) # rotate 180
	img = img[round(img.shape[0]*.7):img.shape[0], 0:img.shape[1]] # crop at 30%
	while True:
		limit = cv.getTrackbarPos('Clip Limit', 'Clahe')
		grid = cv.getTrackbarPos('Grid Size', 'Clahe')
		if limit < 1:
			limit = 1
		if grid < 1:
			grid = 1
		img1 = clahe(img.copy(), limit, grid)
		claheImages = np.concatenate((img,img1), axis=0)
		cv.imshow('Clahe', claheImages)

		k = cv.waitKey(30) & 0xff
		if k == 27:
			break
