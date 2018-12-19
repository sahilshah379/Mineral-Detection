import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def images(img1,img2):
	img1 = cv.resize(img1, (0,0), fx=0.5, fy=0.5)
	img2 = cv.resize(img2, (0,0), fx=0.5, fy=0.5)
	while True:
		images = np.concatenate((img1, img2), axis=1)
		cv.imshow('images', images)
		k = cv.waitKey(30) & 0xff
		if k == 27:
			break

def balance(img):
	lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
	lab[:,:,1] = lab[:,:,1]-((np.average(lab[:,:,1])-128)*(lab[:,:,0]/255.0)*1.1)
	lab[:,:,2] = lab[:,:,2]-((np.average(lab[:,:,2])-128)*(lab[:,:,0]/255.0)*1.1)
	new = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
	return new

if __name__ == "__main__":
	img1 = cv.imread('img1.jpg', 1)
	img2 = balance(img1)
	images(img1,img2)