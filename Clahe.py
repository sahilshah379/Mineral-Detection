import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def images(img1,img2):
	# while True:
	cv.imshow('old', img1)
	cv.imshow('new',img2)
		# plt.show()
		# k = cv.waitKey(30) & 0xff
		# if k == 27:
		# 	break

def hist1(img1):
	hist,bins = np.histogram(img1.flatten(),256,[0,256])
	cdf = hist.cumsum()
	cdf_normalized = cdf * hist.max()/ cdf.max()
	hist1 = plt.figure(1)
	plt.plot(cdf_normalized, color = 'b')
	plt.hist(img1.flatten(),256,[0,256], color = 'r')
	plt.xlim([0,256])
	plt.legend(('cdf','histogram1'), loc = 'upper left')
	hist1.show()

def hist2(img2):
	hist,bins = np.histogram(img2.flatten(),256,[0,256])
	cdf = hist.cumsum()
	cdf_normalized = cdf * hist.max()/ cdf.max()
	hist2 = plt.figure(2)
	plt.plot(cdf_normalized, color = 'b')
	plt.hist(img2.flatten(),256,[0,256], color = 'r')
	plt.xlim([0,256])
	plt.legend(('cdf','histogram2'), loc = 'upper left')
	hist2.show()

if __name__ == "__main__":
	cap = cv.VideoCapture(0)
	_,frame = cap.read()
	img1 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	img1 = cv.imread('img2.jpg', 0)
	# img2 = cv.equalizeHist(img1)
	img2 = 
	images(img1,img2)
	hist1(img1)
	hist2(img2)
	input()

# hist,bins = np.histogram(img.flatten(),256,[0,256])
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max()/ cdf.max()
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()