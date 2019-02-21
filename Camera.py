import cv2 as cv
# import subprocess

def nothing(x):
    pass
cv.namedWindow('Image');
cv.createTrackbar('Exposure', 'Image', 1, 100, nothing)

cap = cv.VideoCapture(0)

while True:
	exposure = cv.getTrackbarPos('Exposure', 'Image')
	if exposure < 1:
		exposure = 1
	# subprocess.check_call("v4l2-ctl -d /dev/video0 -c exposure_absolute=" + str(exposure),shell=True)
	cap.set(cv.CAP_PROP_EXPOSURE, exposure)
	ret,frame = cap.read()
	cv.imshow('Image',frame)
	k = cv.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv.destroyAllWindows()