import cv2 as cv

img = cv.imread('6.tif',cv.IMREAD_GRAYSCALE)

img2 = cv.equalizeHist(img)
cv.imshow("Using cv.equalizeHist()",img2)
cv.imwrite("equalizeHist.png",img2)
cv.waitKey(0)