import cv2 as cv
import numpy as np






# img = cv.imread('data/webcam29.jpg',)
# cv.imshow('imshow',img)
# cv.waitKey(0)
# P = [[198.947681327768,0,316.226600670122],
#      [0,199.176416744225,244.142825317895],
#      [0,0,1]]
# K = [0.279986422119938,-0.251753777158067,0,0]
# img1 = cv.undistort(img, np.array(P), np.array(K))
# cv.imshow('imshow',img1)
# cv.waitKey(0)


def undistort(img,P,K):
    return cv.undistort(img,np.array(P),np.array(K))